
import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication
from resources import resources_rc

from ui.todoMainWindow2 import Ui_MainWindow

basedir = os.path.dirname(__file__)

tick = QImage(os.path.join(basedir, "resources/tick.png"))


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        # The .todos is our data store
        self.todos = todos or []

    # data() and rowCount() are standard Model
    # methods we must implement for a list model
    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick
    # This is requested by the view
    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui from Ui_MainWindow
        self.setupUi(self)
        # Pre-populate the widget with some todo´s
        self.data = [(True, "Be really Awesome!"), (False, "Go to Cánada"), (True, "Buy a monitor")]
        # Fill the model with the data
        self.model = TodoModel(self.data)

        # Fill the view with the model
        self.listView.setModel(self.model)
        # Some extra button configuration
        icon = QtGui.QPixmap(":/icons/skullIcon.png")
        self.pushButton.setIcon(QtGui.QIcon(icon))
        self.pushButton.clicked.connect(self.add)
        #self.pushButton.clicked.connect(self._refresh)
        self.pushButton_2.pressed.connect(self.delete)
        self.pushButton_4.pressed.connect(self.complete)
        self.show()

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.lineEdit.text()
        # Remove the withe space  from the ends of the strings
        text.strip()

        # Don´t add empty strings
        if text:
            # Access the list via the model
            self.model.todos.append((False, text))
            # Trigger refresh
            self.model.layoutChanged.emit()
            # Empty the input
            self.lineEdit.setText("")

    # My attempt to add items to the view :)
    # def _refresh(self):
    #     self.model.todos.append((True, "A new Item here!"))
    #     self.model.layoutChanged.emit()
    #     print(self.data)

    def complete(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            # This needs to be overridden because tuples are immutable
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # For a single selection
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid)
            self.listView.clearSelection()

        print("Complete!")

    def delete(self):
        indexes = self.listView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid)
            self.listView.clearSelection()

        print("Delete!")



# Entry Point
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle("Fusion")
    app.exec()
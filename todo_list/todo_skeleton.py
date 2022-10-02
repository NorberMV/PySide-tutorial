
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication
from resources import resources_rc


from ui.todoMainWindow2 import Ui_MainWindow


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        # The .todos is our data store
        self.todos = todos or []
    # data() and rowCount() are standard Model
    # methods we must implement for a list model
    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
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
        self.show()

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        text = self.lineEdit.text()
        text.strip() #Remove the withe space  from the ends of the strings

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





# Entry Point
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle("Fusion")
    app.exec()
# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
# More widgets from: https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes[QWidget%20documentation]
# This connect the widgets QLineEdit and QLabel, any text typed in the input inmediately appears on the label

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys
from random import choice

# Subclass QMainWindow to customize the application´s main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central Widget of the window
        self.setCentralWidget(container)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
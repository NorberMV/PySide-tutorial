# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider

# Subclass QMainWindow to customize the application´s main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Widget Demo App!')
        widget = QSlider()
        # Set the central widget of the window.
        self.setCentralWidget(widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
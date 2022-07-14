# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
# More widgets from: https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes[QWidget%20documentation]

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider

# Subclass QMainWindow to customize the application´s main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Widget Demo App!')
        # Try other widgets
        widget = QSlider()
        # Fixed size window
        self.setFixedSize(QSize(400, 300))
        # Set the central widget of the window.
        self.setCentralWidget(widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
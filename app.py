# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
# More widgets from: https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes[QWidget%20documentation]

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton

# Subclass QMainWindow to customize the application´s main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.checked_status = True

        self.setWindowTitle('Widget Demo App!')
        # Try other widgets
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.setChecked(self.checked_status)
        # Set the central widget of the window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self, checked):
        """
        A custom slot to receive the
        signal from the button.
        """
        self.checked_status = checked
        print(f'Clicked!, checked state: {checked}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
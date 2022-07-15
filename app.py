# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
# More widgets from: https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes[QWidget%20documentation]
# If a widget does not provide  a signal that  send the current state, you will need to retrieve the value from the
# widget directly by using .isChecked()

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
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.checked_status)
        # Set the central widget of the window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        """
        A custom slot to receive the
        signal from the button.
        """
        self.checked_status = self.button.isChecked()
        print(f'The button was released, checked state: {self.checked_status}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
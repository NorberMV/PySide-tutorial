# The developer sandbox to try new things with PySide before officially push it to GH
# Adding a Simple QLabel widget

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox, QSlider


# Subclass QMainWindow to customize your application´s main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Dev App")

        widget = QSlider()
        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setSingleStep(3)


        # Signal
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        # Set the central widget of the window
        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("Position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released!")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()



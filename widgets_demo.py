# The developer sandbox to try new things with PySide before officially push it to GH
# Adding a Simple QLabel widget

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox


# Subclass QMainWindow to customize your application´s main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Dev App")

        widget = QComboBox()
        widget.addItems(["Nintendo Switch", "Steam Deck", "Nintendo Switch Lite"])

        # Signal
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        # Set the central widget of the window
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()



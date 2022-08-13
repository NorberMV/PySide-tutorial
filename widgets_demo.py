# The developer sandbox to try new things with PySide before officially push it to GH
# Adding a Simple QLabel widget

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


# Subclass QMainWindow to customize your application´s main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Dev App")

        #
        widget = QLabel("My App")
        # We also can setup the text with
        # the method .setText()
        widget.setText("Norber App!")
        # You also can adjust font parameters
        font = widget.font()
        font.setPointSize(20)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # Set the central widget of the window
        self.setCentralWidget(widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()



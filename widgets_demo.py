# The developer sandbox to try new things with PySide before officially push it to GH
# Adding a Simple QLabel widget

import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox


# Subclass QMainWindow to customize your application´s main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Dev App")

    
        widget = QCheckBox("This is a checkbox!")
        widget.setCheckState(Qt.Checked)
        # Signal
        widget.stateChanged.connect(self.show_state)



        # Set the central widget of the window
        self.setCentralWidget(widget)

    def show_state(self, state):
        print(state == Qt.Checked)
        print(state)
        print(Qt.Checked)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()



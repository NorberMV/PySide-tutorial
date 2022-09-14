
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox, QSlider, QDial, QToolBar
from PySide6.QtGui import QAction



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App!")
        label = QLabel("Hello!")
        label.setAlignment(
            Qt.AlignCenter
        )
        self.setCentralWidget(label)
        toolbar = QToolBar("My Main Toolbar!")
        self.addToolBar(toolbar)

        # Add action
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button!")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # Set Action to the toolbar
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        print("Click!", s)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

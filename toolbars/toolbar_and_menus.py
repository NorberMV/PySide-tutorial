
# import sys
# from PySide6.QtCore import QSize, Qt
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QComboBox, QSlider, QDial, QToolBar, QStatusBar
# from PySide6.QtGui import QAction, QIcon

import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QMenuBar,
    QMenu,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game App")
        # Configure the label
        label = QLabel("Choose a character!")
        label.setAlignment(
            Qt.AlignCenter
        )
        self.setCentralWidget(label)

        # Configure the toolbar
        toolbar = QToolBar("My main toolbar")
        # Set the toolbar size
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("./resources/icons/skull-mad.png"), self.tr("&Your button"), self)
        button_action.setStatusTip(self.tr("This is your button"))
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.setChecked(True)

        toolbar.addAction(button_action)
        toolbar.addWidget(QLabel("Hell Skull!"))
        toolbar.addSeparator()

        button_action2 = QAction(QIcon("./resources/icons/animal-dog.png"), self.tr("Your &button2"), self)
        button_action2.setStatusTip(self.tr("This is your button2"))
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hell Dog!"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()


        file_menu = menu.addMenu(self.tr("&Game Settings!"))
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)


    def onMyToolBarButtonClick(self, s):
        print("click", s)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

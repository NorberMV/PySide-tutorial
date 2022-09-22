
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction #, QApplication, QLabel, QMainWindow, QMenu
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())

    def mousePressEvent(self, e):
        print(e)
        

# Entry Point
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

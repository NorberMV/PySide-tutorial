import sys
import random
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel




class Chamaleon(QtWidgets.QWidget):
    """ Chamaleon Widget."""
    def __init__(self):
        super().__init__()
        # size Size Policy
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        # Color count
        self.count = 0
        # Color background array
        self.color = ["black", "purple", "orange"]
        self.lay = QVBoxLayout()
        self._add_label("AmazeApp!")
        self._add_button("MyCoolButton!")
        # Alignment
        self.lay.setAlignment(
            Qt.AlignHCenter,
        )
        self.setLayout(self.lay)
        # Button clicked signal
        self.button.clicked.connect(self.trigger_refresh)

    def sizeHint(self):
        return QtCore.QSize(220, 320)

    def paintEvent(self, e):
        # Pick background Color
        if self.count != len(self.color):
            color = self.color[self.count]
            self.count += 1
            print(self.count)
        else:
            # black color by default and Reset count
            color = "green"
            self.count = 0

        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(color))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

    def _add_label(self, label_text):
        # Label settings
        label = QLabel(label_text)
        label.setAlignment(
            Qt.AlignTop | Qt.AlignHCenter,
        )
        label.setStyleSheet("border: 1.5px solid purple;")
        self.lay.addWidget(label)

    def _add_button(self, button_name):
        self.button = QPushButton(button_name)
        self.lay.addWidget(self.button)

    def trigger_refresh(self):
        self.update()


class MyWid(QtWidgets.QWidget):

    # This wid that will be
    # displayed.

    def __init__(self):
        super().__init__()
        wid = Chamaleon()
        lay = QVBoxLayout()
        lay.addWidget(wid)
        self.setLayout(lay)



# Entry Point
if __name__=="__main__":

    app = QApplication(sys.argv)
    MyWid = MyWid()
    MyWid.show()
    app.exec()

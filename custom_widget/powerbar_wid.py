
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel


class _Bar(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )

    def sizeHint(self):
        return QtCore.QSize(200, 240)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get the current state

        # Accessing the PowerBar widget
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QtGui.QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Times")
        font.setPointSize(18)
        painter.setFont(font)

        painter.drawText(25, 25, "{}-->{}<--{}".format(vmin, value, vmax))
        painter.end()

    def trigger_refresh(self):
        self.update()

class PowerBar(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound  and custom-drawn widget.
    """

    def __init__(self, step=5):
        super().__init__()
        # Create the layout
        layout = QtWidgets.QVBoxLayout()
        # Call our custom _Bar() widget
        self._bar = _Bar()
        # Add our custom _Bar() widget
        # to the layout
        layout.addWidget(self._bar)
        # Call the built-in QDial() widget
        self._dial = QtWidgets.QDial()
        self._dial.valueChanged.connect(self._bar.trigger_refresh)
        # Add it to our layout
        layout.addWidget(self._dial)
        # Apply the layout to the widget
        self.setLayout(layout)

# Entry Point
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    volume = PowerBar()
    volume.show()
    app.exec_()
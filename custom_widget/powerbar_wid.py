
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

        # Obtain a number between 0 - 6 from the
        # dial.
        pc = ((value - vmin)/(vmax - vmin))
        n_steps_to_draw = int(pc * 6)

        # Padding dimensions
        padding = 5

        # Define the bars canvas
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)

        # Layout
        # Break up our d_height into 5 equal parts.
        # one for each block.
        step_size = d_height / 6
        bar_height = step_size * 0.6
        bar_spacer = step_size * 0.4 / 2

        # Draw
        brush.setColor(QtGui.QColor("red"))

        for n in range(n_steps_to_draw):
            rect = QtCore.QRect(
                padding,
                padding + d_height - ((n + 1) * step_size) + bar_spacer,
                d_width,
                bar_height,
            )
            painter.fillRect(rect, brush)
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
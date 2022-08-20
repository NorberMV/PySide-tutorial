
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel


class _Bar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        lab = QLabel("My Custom App")
        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(lab)
        self.setLayout(lay)


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
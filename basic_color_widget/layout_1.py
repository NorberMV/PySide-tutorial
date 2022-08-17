
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # List a few colors for the widgets
        colors = ["orange", "yellow", "red"]
        # Create the layout and add widgets to it
        widget = self.add_more_colors(colors=colors)

        self.setCentralWidget(widget)


    def add_more_colors(self, colors="orange"):
        """A simple function to add
        the Color widgets to a Vertical
        layout.
        """
        # In order to add the layout we
        # need to Create a dummy widget
        widget = QWidget()
        # Create the vertical layout
        lay = QVBoxLayout()

        for color in colors:
            lay.addWidget(Color(color))
        widget.setLayout(lay)

        return widget


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
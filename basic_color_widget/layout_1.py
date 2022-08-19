
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

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
        the Color widget by nesting layouts.
        """
        # In order to add the layout we
        # need to Create a dummy widget
        widget = QWidget()
        # Create the layouts
        lay_1 = QHBoxLayout()
        lay_2 = QVBoxLayout()
        lay_3 = QHBoxLayout()

        layouts = [lay_2, lay_1, lay_3]

        for lay in layouts:
            for color in colors:
                lay.addWidget(Color(color))
            # Nest the layout
            lay_1.addLayout(lay)
        widget.setLayout(lay_1)

        return widget


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
# Following this tutorial here: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/
# More widgets from: https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes[QWidget%20documentation]
#  In this code we subclass QWidget to create our own custom widget "Color".
# we accept a single parameter  when creating the widget --color(a str).
# we first set .setAutoFillBackground to True to tell the widget to automatically fill it´s background with
# the new color.
# Next we change the  widget`s QPalette.Window color to a new QColor described by the value color we passed in.
# So you can create a solid-filled red widget by with the following code-- ```Color('red')

from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)



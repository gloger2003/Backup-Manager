from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Styles


class ScrollFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.STYLE = Styles.ScrollFrameStyle(self)
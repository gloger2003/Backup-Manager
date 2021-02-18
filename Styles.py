from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ControlFrameStyle:
    def __init__(self, control_frame: QFrame):
        self.control_frame = control_frame

        self.DEFAULT_STYLE = """
                background-color: rgb(30, 30, 30);
                border-top: 2px solid rgb(30, 250, 20);
            """
        self.control_frame.setStyleSheet(self.DEFAULT_STYLE)

        self.control_frame.shadow = QGraphicsDropShadowEffect()
        self.control_frame.shadow.setColor(QColor(QColorConstants.Black))
        self.control_frame.shadow.setOffset(0, -5)
        self.control_frame.shadow.setBlurRadius(100)
        self.control_frame.setGraphicsEffect(self.control_frame.shadow)
    pass


class ControlFrameStyle:
    def __init__(self, control_frame: QFrame):
        self.control_frame = control_frame

        self.DEFAULT_STYLE = """
                background-color: rgb(30, 30, 30);
                border-top: 2px solid rgb(30, 250, 20);
            """
        self.control_frame.setStyleSheet(self.DEFAULT_STYLE)

        self.control_frame.shadow = QGraphicsDropShadowEffect()
        self.control_frame.shadow.setColor(QColor(QColorConstants.Black))
        self.control_frame.shadow.setOffset(0, -5)
        self.control_frame.shadow.setBlurRadius(100)
        self.control_frame.setGraphicsEffect(self.control_frame.shadow)
    pass



class ScrollFrameStyle:
    def __init__(self, scroll_frame: QFrame):
        self.scroll_frame = scroll_frame

        self.DEFAULT_STYLE = """
                background-color: rgb(20, 20, 20);
            """
        self.scroll_frame.setStyleSheet(self.DEFAULT_STYLE)
    pass


class PathLineEditStyle:
    def __init__(self, path_line_edit: QLineEdit):
        self.path_line_edit = path_line_edit

        self.DEFAULT_FONT = QFont('', 15)
        self.DEFAULT_STYLE = """
            background-color: rgb(20, 20, 20);
            border: 1px solid rgb(230, 150, 0);
            border-radius: 5px;
            color: white;
            padding: 10px;
        """
    
        self.path_line_edit.setStyleSheet(self.DEFAULT_STYLE)
        self.path_line_edit.setFont(self.DEFAULT_FONT)

        self.path_line_edit.shadow = QGraphicsDropShadowEffect()
        self.path_line_edit.shadow.setColor(QColor(QColorConstants.Black))
        self.path_line_edit.shadow.setOffset(0, 0)
        self.path_line_edit.shadow.setBlurRadius(10)
        self.path_line_edit.setGraphicsEffect(self.path_line_edit.shadow)
        pass


class DialogButtonStyle:
    def __init__(self, dialog_button: QToolButton):
        self.dialog_button = dialog_button

        self.DEFAULT_STYLE = """
            background-color: rgb(20, 20, 20);
            border-radius: 5px;
            border: 1px solid rgb(230, 150, 0);
            color: white;
            font-size: 20px;
        """
        self.dialog_button.setStyleSheet(self.DEFAULT_STYLE)
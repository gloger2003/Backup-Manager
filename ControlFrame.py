from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Styles


class DirDialogButton(QToolButton):
    def __init__(self, parent=None, path_line_edit=QLineEdit):
        super().__init__(parent)
        self.path_line_edit = path_line_edit
        self.setMinimumHeight(50)
        self.STYLE = Styles.DialogButtonStyle(self)
        self.setText("Добавить папку")
        self.clicked.connect(self.open_dialog_window)

    def open_dialog_window(self):
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.DirectoryOnly)
        url = self.dialog.getExistingDirectoryUrl(None, "Выберите папку")
        print(url.toString().lstrip('file:///'))
        pass



class FileDialogButton(QToolButton):
    def __init__(self, parent=None, path_line_edit=QLineEdit):
        super().__init__(parent)
        self.path_line_edit = path_line_edit
        self.setMinimumHeight(50)
        self.STYLE = Styles.DialogButtonStyle(self)
        self.setText("Добавить файл")
        self.clicked.connect(self.open_dialog_window)

    def open_dialog_window(self):
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        url = self.dialog.getOpenFileUrl(None, "Выберите файл")
        print(url[0].toString().lstrip('file:///'))
        pass


class PathLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.STYLE = Styles.PathLineEditStyle(self)
        self.setFixedHeight(50)
        pass


class ControlFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(150)
        self.STYLE = Styles.ControlFrameStyle(self)

        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setContentsMargins(50, 20, 50, 20)
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        self.load_gui()
        pass


    def load_gui(self):
        self.file_dialog_button = FileDialogButton(self)
        self.main_layout.addWidget(self.file_dialog_button)

        self.dir_dialog_button = DirDialogButton(self)
        self.main_layout.addWidget(self.dir_dialog_button)
        pass

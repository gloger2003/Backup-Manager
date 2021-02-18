from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Styles
from ControlFrameButton import DialogFileButton, DialogFolderButton


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
        self.file_dialog_button = DialogFileButton.DialogFileButton(self)
        self.main_layout.addWidget(self.file_dialog_button)

        self.folder_dialog_button = DialogFolderButton.DialogFolderButton(self)
        self.main_layout.addWidget(self.folder_dialog_button)
        pass

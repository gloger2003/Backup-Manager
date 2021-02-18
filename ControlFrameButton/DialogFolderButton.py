from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Styles


class DialogFolderButton(QToolButton):
    """
    Открывает диалоговое окно с выбором папки

    """
    def __init__(self, parent=None, **params):
        super().__init__(parent)
        self.setMinimumHeight(50)
        self.STYLE = Styles.DialogButtonStyle(self)
        self.setText("Добавить папку")
        self.clicked.connect(self.open_dialog_window)

    def open_dialog_window(self):
        """
        Открывает диалоговое окно выбора папки и возвращает адрес выбранной папки
        
        """
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.DirectoryOnly)
        url = self.dialog.getExistingDirectoryUrl(None, "Выберите папку").toString().lstrip('file:///')
        print(url)
        return url
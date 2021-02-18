from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Styles


class DialogFileButton(QToolButton):
    """
    Кнопка для выбора файла

    """
    def __init__(self, parent=None, **params):
        super().__init__(parent)
        self.setMinimumHeight(50)
        self.STYLE = Styles.DialogButtonStyle(self)
        self.setText("Добавить файл")
        self.clicked.connect(self.open_dialog_window)

    def open_dialog_window(self):
        """
        Открывает диалоговое окно выбора файла и возвращает адрес выбранного файла

        """
        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.AnyFile)
        url = self.dialog.getOpenFileUrl(None, "Выберите файл")[0].toString().lstrip('file:///')
        print(url)
        return url
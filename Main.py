import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ControlFrame
import ScrollFrame

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumSize(640, 480)
        self.resize(1280, 720)
        self.setWindowTitle('Backup Manager 0.0.1')
        
        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("background-color: rgb(30, 30, 30)")
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(self.main_layout)

        self.load_gui()
    
    def load_scroll_frame_gui(self):
        self.scroll_frame = ScrollFrame.ScrollFrame(self.central_widget)
        self.main_layout.addWidget(self.scroll_frame)
        pass

    def load_control_frame_gui(self):
        self.control_frame = ControlFrame.ControlFrame(self.central_widget)
        self.main_layout.addWidget(self.control_frame)
        pass

    def load_gui(self):
        self.load_scroll_frame_gui()
        self.load_control_frame_gui()
        self.main_layout.setStretch(0, 8)
        self.main_layout.setStretch(1, 2)
        pass



if __name__ == "__main__":
    APP = QApplication([])
    WINDOW = Window()
    WINDOW.show()
    APP.exec()
    sys.exit()
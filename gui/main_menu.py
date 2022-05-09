# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
# Other programmed files :


class MainMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        # 'Application' object.
        self.app = app
        # Setup frame properties :
        self.setStyleSheet("background-color: #303030")
        # Launching frame items :
        self.init_frame_items()

    def init_frame_items(self):
        play_button = QPushButton(self)
        play_button.setText("Play !")
        play_button.setGeometry(150, 200, 150, 50)
        play_button.setStyleSheet('font-family: Lucida Handwriting; font-size: 26px; color: #303030;'
                                  'background-color: darkgrey; border-radius: 14px;')
        play_button.setCursor(QCursor(Qt.PointingHandCursor))
        play_button.clicked.connect(self.launchGameMenu)

    def launchGameMenu(self):
        self.app.stacked.setCurrentIndex(1)


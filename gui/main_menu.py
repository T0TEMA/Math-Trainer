# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
# Other programmed files :


class MainMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        # 'Application' object.
        self.app = app
        # Launching frame items :
        self.init_frame_items()

    def init_frame_items(self):
        x = 190  # Horizontal position
        y = 110  # Vertical position
        # Title label:
        title_label = QLabel(self)
        title_label.setText("Math Trainer")
        title_label.setGeometry(x, y, 405, 100)
        title_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 52px; color: lightgrey;')
        # Rights label:
        rights_label = QLabel(self)
        rights_label.setText("Totema's projects (2022)")
        rights_label.setGeometry(10, 430, 120, 15)
        rights_label.setStyleSheet('color: grey;')
        # Play button :
        play_button = QPushButton(self)
        play_button.setText("Play !")
        play_button.setGeometry(x, y+140, 400, 50)
        play_button.setStyleSheet(open("gui/button.css").read())
        play_button.setCursor(QCursor(Qt.PointingHandCursor))
        play_button.clicked.connect(self.app.launchGameMenu)
        # Settings button :
        settings_button = QPushButton(self)
        settings_button.setText("Settings")
        settings_button.setGeometry(x, y+80, 195, 50)
        settings_button.setStyleSheet(open("gui/button.css").read())
        settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        settings_button.clicked.connect(self.app.launchSettingsMenu)
        # Profile button :
        profile_button = QPushButton(self)
        profile_button.setText("Profile")
        profile_button.setGeometry(x+205, y+80, 195, 50)
        profile_button.setStyleSheet(open("gui/button.css").read())
        profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_button.clicked.connect(self.app.launchProfileMenu)

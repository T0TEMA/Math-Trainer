"""
"Set Object Name" is used in the '.css' file to assign a part of the styling sheet to a given item
in the window.
"""
# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt
# Other programmed files :


class MainMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        # 'Application' object.
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Launching frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Title label:
        title_label = QLabel(self)
        title_label.setText("Math Trainer")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setGeometry(0, 20, w, 120)
        title_label.setObjectName("title_label")
        title_label.setFont(QFont("", 50))
        title_label.setStyleSheet(self.app.css)
        # Rights label:
        rights_label = QLabel(self)
        rights_label.setText("Totema's projects (2022)")
        rights_label.setAlignment(Qt.AlignLeft)
        rights_label.setGeometry(10, h-20, w-10, 20)
        rights_label.setObjectName("rights_label")
        rights_label.setFont(QFont("", 10))
        rights_label.setStyleSheet(self.app.css)
        # Settings button :
        settings_button = QPushButton(self)
        settings_button.setText("Settings")
        settings_button.setGeometry((w//2)-300, (h//2)-60, 290, 100)
        settings_button.setFont(QFont("", 30))
        settings_button.setStyleSheet(self.app.css)
        settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        settings_button.clicked.connect(self.app.launchSettingsMenu)
        # Profile button :
        profile_button = QPushButton(self)
        profile_button.setText("Profile")
        profile_button.setGeometry((w//2)+10, (h//2)-60, 290, 100)
        profile_button.setFont(QFont("", 30))
        profile_button.setStyleSheet(self.app.css)
        profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_button.clicked.connect(self.app.launchProfileMenu)
        # Play button :
        play_button = QPushButton(self)
        play_button.setText("Play !")
        title_label.setAlignment(Qt.AlignCenter)
        play_button.setGeometry((w//2)-300, (h//2)+60, 600, 100)
        play_button.setFont(QFont("", 30))
        play_button.setStyleSheet(self.app.css)
        play_button.setCursor(QCursor(Qt.PointingHandCursor))
        play_button.clicked.connect(self.app.launchGameMenu)

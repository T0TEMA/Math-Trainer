# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QSizePolicy
from PyQt5.QtGui import QCursor
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
        x = self.app.width()    # Horizontal position
        y = self.app.height()   # Vertical position
        # Title label:
        title_label_x = 190
        title_label_y = 110
        title_label = QLabel(self)
        title_label.setText("Math Trainer")
        title_label.setGeometry(title_label_x, title_label_y, 405, 100)
        title_label.setObjectName("title_label") # ObjectName is used in CSS file
        title_label.setStyleSheet(self.app.css)
        # Rights label:
        rights_label = QLabel(self)
        rights_label.setText("Totema's projects (2022)")
        rights_label.setGeometry(10, y-20, 150, 15)
        rights_label.setObjectName("rights_label")
        rights_label.setStyleSheet(self.app.css)
        # Play default.css :
        play_button = QPushButton(self)
        play_button.setText("Play !")
        play_button.setGeometry(title_label_x, title_label_y+140, 400, 50)
        play_button.setStyleSheet(self.app.css)
        play_button.setCursor(QCursor(Qt.PointingHandCursor))
        play_button.clicked.connect(self.app.launchGameMenu)
        # Settings default.css :
        settings_button = QPushButton(self)
        settings_button.setText("Settings")
        settings_button.setGeometry(title_label_x, title_label_y+80, 195, 50)
        settings_button.setStyleSheet(self.app.css)
        settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        settings_button.clicked.connect(self.app.launchSettingsMenu)
        # Profile default.css :
        profile_button = QPushButton(self)
        profile_button.setText("Profile")
        profile_button.setGeometry(title_label_x+205, title_label_y+80, 195, 50)
        profile_button.setStyleSheet(self.app.css)
        profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_button.clicked.connect(self.app.launchProfileMenu)

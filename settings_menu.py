# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt
# Other programmed files :


class SettingsMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Frame data structures :
        self.resolutions = ['800x450', '1280x720', '1920x1080', '2560x1440']
        self._themes = ['default', 'bright']  # Used in the '.txt' file.
        self.themes = ['Default', 'Bright']   # Used in the GUI.
        # Modified settings :
        self.resolution = self.resolutions.index(self.app.settings.content['resolution'])
        self.theme = self._themes.index(self.app.settings.content['theme'])
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Title label :
        title_label = QLabel(self)
        title_label.setText("Settings")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setGeometry(0, 10, w, 120)
        title_label.setFont(QFont("", 50))
        title_label.setObjectName("title_label")
        title_label.setStyleSheet(self.app.css)
        # Back to main menu :
        back_button = QPushButton(self)
        back_button.setText("<")
        back_button.setGeometry(30, 30, 70, 70)
        back_button.setFont(QFont("Arial", 20))
        back_button.setStyleSheet(self.app.css)
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.clicked.connect(self.app.launchMainMenu)
        # Resolution label :
        res_label = QLabel(self)
        res_label.setText("  Resolution  :")
        res_label.setAlignment(Qt.AlignVCenter)
        res_label.setGeometry(20, 140, w-40, 90)
        res_label.setFont(QFont("", 30))
        res_label.setObjectName("setting_frames")
        res_label.setStyleSheet(self.app.css)
        # Resolution ComboBox :
        res_box = QComboBox(self)
        res_box.setGeometry(425, 145, w-455, 80)
        res_box.setFont(QFont('', 20))
        res_box.addItems(self.resolutions)
        res_box.setCurrentIndex(self.resolution)
        res_box.setCursor(QCursor(Qt.PointingHandCursor))
        res_box.setStyleSheet(self.app.css)
        res_box.currentIndexChanged.connect(self.changed_resolution)
        # Theme label :
        theme_label = QLabel(self)
        theme_label.setText("  Theme :")
        theme_label.setAlignment(Qt.AlignVCenter)
        theme_label.setGeometry(20, 240, w-40, 90)
        theme_label.setFont(QFont("", 30))
        theme_label.setObjectName("setting_frames")
        theme_label.setStyleSheet(self.app.css)
        # Theme ComboBox :
        theme_box = QComboBox(self)
        theme_box.setGeometry(425, 245, w-455, 80)
        theme_box.setFont(QFont('', 20))
        theme_box.addItems(self.themes)
        theme_box.setCurrentIndex(self.theme)
        theme_box.setCursor(QCursor(Qt.PointingHandCursor))
        theme_box.setStyleSheet(self.app.css)
        theme_box.currentIndexChanged.connect(self.changed_theme)
        # Save button :
        save_button = QPushButton(self)
        save_button.setText("Save")
        save_button.setGeometry(20, h-110, w-40, 90)
        save_button.setFont(QFont("", 30))
        save_button.setCursor(QCursor(Qt.PointingHandCursor))
        save_button.setStyleSheet(self.app.css)
        save_button.clicked.connect(self.save_changes)

    def changed_resolution(self, i):
        self.resolution = i

    def changed_theme(self, i):
        self.theme = i

    def save_changes(self):
        self.app.settings.content['resolution'] = self.resolutions[self.resolution]
        self.app.settings.content['theme'] = self._themes[self.theme]
        self.app.settings.save()
        self.app.reload_window_items()

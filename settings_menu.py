# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QComboBox
from PyQt5.QtGui import QCursor
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
        # Back to main menu :
        back_button = QPushButton(self)
        back_button.setText("<")
        back_button.setGeometry(20, 20, 60, 60)
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.setStyleSheet(self.app.css)
        back_button.clicked.connect(self.app.launchMainMenu)
        # Title label :
        title_label = QLabel(self)
        title_label.setText("Settings")
        title_label.setGeometry(270, 0, 300, 100)
        title_label.setObjectName("title_label")
        title_label.setStyleSheet(self.app.css)
        # Resolution ComboBox :
        res_box = QComboBox(self)
        res_box.setGeometry(190, 100, 400, 50)
        res_box.addItems(self.resolutions)
        res_box.setCurrentIndex(self.resolution)
        res_box.setCursor(QCursor(Qt.PointingHandCursor))
        res_box.setStyleSheet(self.app.css)
        res_box.currentIndexChanged.connect(self.changed_resolution)
        # GUI Skin ComboBox :
        skin_box = QComboBox(self)
        skin_box.setGeometry(190, 170, 400, 50)
        skin_box.addItems(self.themes)
        skin_box.setCurrentIndex(self.theme)
        skin_box.setCursor(QCursor(Qt.PointingHandCursor))
        skin_box.setStyleSheet(self.app.css)
        skin_box.currentIndexChanged.connect(self.changed_theme)
        # Save button :
        save_button = QPushButton(self)
        save_button.setText("Save")
        save_button.setGeometry(190, 240, 400, 50)
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

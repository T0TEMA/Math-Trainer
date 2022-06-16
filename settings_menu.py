# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
# Other programmed files :
from item_creator import create_button, create_label, create_combobox


class SettingsMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Frame data structures :
        self.themes = ['Default', 'Bright', 'Dark', 'None']
        # Modified settings :
        self.selected_theme = self.themes.index(self.app.settings.content['theme'])
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Title label :
        create_label(self, "Settings", 0, 10, w, 120, 1, Qt.AlignCenter, "title_label", self.app.css)
        # Back to main menu :
        create_button(self, "<", 20, 20, 100, 100, 1, "", self.app.css, self.app.launchMainMenu, "Esc")
        # Theme label :
        create_label(self, "  Theme :", 20, 240, w-40, 90, 1, Qt.AlignVCenter, "setting_frames", self.app.css)
        # Theme ComboBox :
        create_combobox(self, self.themes, self.selected_theme, 425, 245, w-455, 80, 1, "", self.app.css, self.changed_theme)
        # Save button :
        create_button(self, "Save", 20, h-110, w-40, 90, 1, "", self.app.css, self.save_changes)

    def changed_theme(self, i):
        self.selected_theme = i

    def save_changes(self):
        self.app.settings.content['theme'] = self.themes[self.selected_theme]
        self.app.settings.save()
        self.app.reload_window_items()

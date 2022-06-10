"""
Author : Totema
"""
# Standard libraries :
import sys
# Downloaded libraries :
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon
# Other programmed files :
from main_menu import MainMenu
from game_menu import GameMenu
from settings_menu import SettingsMenu
from data.manage_file import Settings
from profile_menu import ProfileMenu
from results_menu import RecapMenu
from game import Game


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup window properties :
        self.setWindowTitle("Math Trainer")
        self.setWindowIcon(QIcon("icon.png"))
        # Setup settings :
        self.settings = Settings()
        self.css = open(f"gui/{self.settings.content['theme']}.css").read()
        self.load_settings()
        # Stacking menus (that never has to reset (except at settings reload) :
        self.stacked = QStackedWidget(self)
        self.stacked.insertWidget(0, MainMenu(self))
        self.stacked.insertWidget(1, SettingsMenu(self))
        self.stacked.insertWidget(2, ProfileMenu(self))
        self.stacked.setCurrentIndex(0)
        self.setCentralWidget(self.stacked)

    def load_settings(self):
        resolution = self.settings.content['resolution'].split('x')
        self.setFixedSize(int(resolution[0]), int(resolution[1]))
        self.setStyleSheet(self.css)

    def reload_window_items(self):
        """
        Reloads all the GUI.
        Is used when changed the settings.
        """
        # Reloading settings :
        self.settings = Settings()
        self.css = open(f"gui/{self.settings.content['theme']}.css").read()
        self.load_settings()
        # Re-stacking menus :
        self.stacked.insertWidget(0, MainMenu(self))
        self.stacked.insertWidget(1, SettingsMenu(self))
        self.stacked.insertWidget(2, ProfileMenu(self))
        self.stacked.setCurrentIndex(1)

    def launchMainMenu(self):
        self.stacked.setCurrentIndex(0)

    def launchSettingsMenu(self):
        self.stacked.setCurrentIndex(1)

    def launchProfileMenu(self):
        self.stacked.setCurrentIndex(2)

    def launchGameMenu(self):
        self.stacked.insertWidget(3, GameMenu(self))
        self.stacked.setCurrentIndex(3)

    def launchRecapMenu(self, game_data):
        self.stacked.insertWidget(4, RecapMenu(self, game_data))
        self.stacked.setCurrentIndex(4)


if '__main__' == __name__:
    application = QApplication([])
    game_app = Application()
    game_app.show()
    sys.exit(application.exec_())

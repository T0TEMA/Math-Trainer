"""
Author : Totema
"""
# Standard libraries :
import sys
# Downloaded libraries :
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QStyleFactory
from PyQt5.QtGui import QIcon
# Other programmed files :
from main_menu import MainMenu
from game_menu import GameMenu
from settings_menu import SettingsMenu
from data.manage_file import Settings
from profile_menu import ProfileMenu
from results_menu import RecapMenu


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup window properties :
        self.setWindowTitle("Math Trainer")
        self.setWindowIcon(QIcon("icon.png"))
        self.w = None  # Window width
        self.h = None  # Window height
        self.tc = None  # Text coefficient (changes the font size depending on window size)
        self.css = None
        # Setup settings :
        self.settings = Settings()
        self.load_settings()
        # Stacking menus (that never has to reset (except at settings reload) :
        self.stacked = QStackedWidget(self)
        self.stacked.insertWidget(0, MainMenu(self))
        self.stacked.insertWidget(1, SettingsMenu(self))
        self.stacked.insertWidget(2, ProfileMenu(self))
        self.stacked.setCurrentIndex(0)
        self.setCentralWidget(self.stacked)

    def load_settings(self):
        """
        Loading all the settings at starting of program, also when changing settings.
        """
        theme = self.settings.content['theme']
        self.css = open(f"gui/{theme[0].lower()}{theme[1:]}.css").read()
        screen = self.settings.content['screen']
        if screen == "Fullscreen":
            size = self.screen().size()
            self.setGeometry(0, 0, size.width(), size.height())
        elif screen == "Windowed":
            resolution = self.settings.content['resolution'].split('x')
            self.setGeometry(0, 34, int(resolution[0]), int(resolution[1]))
        self.w = self.width()
        self.h = self.height()
        self.setStyleSheet(self.css)

    def reload_window_items(self):
        """
        Reloads all the GUI.
        Is used when changed the settings.
        """
        # Reloading settings :
        self.settings = Settings()
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
    #print(QStyleFactory.keys())
    #application.setStyle('Fusion')
    game_app = Application()
    game_app.show()
    sys.exit(application.exec_())

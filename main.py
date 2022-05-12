# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
# Other programmed files :
from main_menu import MainMenu
from game_menu import GameMenu
from settings_menu import SettingsMenu
from profile_menu import ProfileMenu
from results_menu import RecapMenu


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup window properties :
        self.setWindowTitle("Math Trainer")
        self.setFixedSize(800, 450)
        self.setStyleSheet("background-color: #303030;")
        # Stacking menus (that never has to reset) :
        self.stacked = QStackedWidget(self)
        self.stacked.insertWidget(0, MainMenu(self))
        self.stacked.insertWidget(1, SettingsMenu(self))
        self.stacked.insertWidget(2, ProfileMenu(self))
        self.stacked.setCurrentIndex(0)
        self.setCentralWidget(self.stacked)

    def launchMainMenu(self):
        self.stacked.setCurrentIndex(0)

    def launchSettingsMenu(self):
        self.stacked.setCurrentIndex(1)

    def launchProfileMenu(self):
        self.stacked.setCurrentIndex(2)

    def launchGameMenu(self):
        """
        Reinstancing the game menu to relaunch a new game.
        ! Instead of relaunching all the item (even the GUI) could make a game class
        which would be the the only one to reload.
        """
        self.stacked.insertWidget(3, GameMenu(self))
        self.stacked.setCurrentIndex(3)

    def launchRecapMenu(self, game_data):
        self.stacked.insertWidget(4, RecapMenu(self, game_data))
        self.stacked.setCurrentIndex(4)


if '__main__' == __name__:
    application = QApplication([])
    game_app = Application()
    game_app.show()
    exit(application.exec_())

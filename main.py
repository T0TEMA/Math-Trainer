# Standard libraries :
from sys import argv
# Downloaded libraries :
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
# Other programmed files :
from gui.main_menu import MainMenu
from gui.game_menu import GameMenu


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup window properties :
        self.setWindowTitle("Math Trainer")
        self.setFixedSize(800, 450)
        # Instanciation of other menus :
        self.main_menu = MainMenu(self)
        self.game_menu = GameMenu(self)
        # Stacking menus :
        self.stacked = QStackedWidget(self)
        self.stacked.insertWidget(0, self.main_menu)
        self.stacked.insertWidget(1, self.game_menu)
        self.stacked.setCurrentIndex(0)
        self.setCentralWidget(self.stacked)


if '__main__' == __name__:
    application = QApplication(argv)
    game_app = Application()
    game_app.show()
    exit(application.exec_())

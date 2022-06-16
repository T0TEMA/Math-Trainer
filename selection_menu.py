# Standard libraries :
from functools import partial
import random
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtCore import QRect, Qt, QTimer
from PyQt5.QtGui import QCursor, QFont
# Other programmed files :
from game import Game
from item_creator import create_button


class SelectionMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Selection menu :
        # todo
        # Start game button:
        create_button(self, "Start !",  20, h-110, w-40, 90, 1, "", self.app.css, self.start_game)

    def start_game(self):
        self.app.launchGameMenu(Game("Multiply", "Easy"))

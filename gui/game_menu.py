# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame
# Other programmed files :


class GameMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app

# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton
from PyQt5.QtCore import QRect
# Other programmed files :


class GameMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        # Launching frame items :
        self.init_frame_items()

    def init_frame_items(self):
        numpad = QFrame(self)
        numpad.setGeometry(QRect(0, 0, 190, 260))
        numpad.setStyleSheet("background-color: white")
        numpad_values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '<-', '0', 'V')
        for i in range(4):
            for j in range(3):
                button = QPushButton(numpad)
                button.setText(numpad_values[i*j])
                button.setGeometry((i*60)+10, (j*60)+10, 50, 50)

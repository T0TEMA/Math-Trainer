# Standard libraries :
import sys
from functools import partial
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtCore import QRect, Qt
# Other programmed files :
sys.path.append("../game")
from game import Game


class GameMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        # Input label :
        self.input_label = QLabel(self)
        self.input_label_value = ""
        # Launching frame items :
        self.init_frame_items()
        self.game = Game()

    def init_frame_items(self):
        # Numpad frame :
        numpad_frame = QFrame(self)
        numpad_frame.setGeometry(QRect(10, 10, 330, 432))
        numpad_frame.setStyleSheet("background-color: lightgrey; border-radius: 12px; font-size: 56px")
        # Numpad buttons :
        numpad_values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '<', '0', 'V')
        for i in range(4):
            for j in range(3):
                n = i*3+j
                button = QPushButton(numpad_frame)
                button.setStyleSheet(open("gui/button.css").read())
                button.setText(numpad_values[n])
                button.setGeometry((j*105)+10, (i*105)+10, 100, 100)
                button.setShortcut(numpad_values[n])
                if n <= 8 or n == 10:
                    button.clicked.connect(partial(self.input_number, eval(numpad_values[i*3+j])))
                    if n == 0:
                        button.setShortcut("&")
                    elif n == 1:
                        button.setShortcut("é")
                    elif n == 2:
                        button.setShortcut('"')
                    elif n == 3:
                        button.setShortcut("'")
                    elif n == 4:
                        button.setShortcut("(")
                    elif n == 5:
                        button.setShortcut("-")
                    elif n == 6:
                        button.setShortcut("è")
                    elif n == 7:
                        button.setShortcut("_")
                    elif n == 8:
                        button.setShortcut("ç")
                elif n == 9:
                    button.clicked.connect(partial(self.input_backspace))
                    button.setShortcut(Qt.Key_Backspace)
                elif n == 11:
                    button.clicked.connect(partial(self.input_enter))
                    button.setShortcut(Qt.Key_Space)
        # Input label :
        self.input_label.setText(self.input_label_value)
        self.input_label.setGeometry(350, 340, 440, 100)
        self.input_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                       "font-family: Lucida Handwriting; font-size: 56px")
        self.input_label.setAlignment(Qt.AlignCenter)
        # Question label :
        question_label = QLabel(self)
        question_label.setGeometry(350, 10, 440, 320)
        question_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                     "font-family: Lucida Handwriting; font-size: 68px")

    def input_number(self, number):
        self.input_label_value += str(number)
        self.input_label.setText(self.input_label_value)

    def input_backspace(self):
        self.input_label_value = self.input_label_value[:-1]
        self.input_label.setText(self.input_label_value)

    def input_enter(self):
        self.game.answer(eval(self.input_label_value))
        self.input_label_value = ""
        self.input_label.setText(self.input_label_value)

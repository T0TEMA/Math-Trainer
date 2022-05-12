# Standard libraries :
from functools import partial
import random
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtCore import QRect, Qt, QTimer
from PyQt5.QtGui import QCursor
# Other programmed files :


class GameMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        # Input label :
        self.input_label = QLabel(self)
        self.input_label_value = ""
        # Game values :
        self.correct = 0
        self.bad = 0
        self.time_left = 5
        self.question_res = None
        self.question_number = 0
        self.question = ""
        # Launching global items (as attributes) :
        self.time_left_label = QLabel(str(self.time_left)+'s', self)
        self.question_number_label = QLabel(str(self.question_number), self)
        self.question_label = QLabel(str(self.question), self)
        # Launching frame items :
        self.init_frame_items()
        # Start game button :
        self.start_game_button = QPushButton(self)
        self.start_game_button.setText("Ready ?")
        self.start_game_button.setGeometry(0, 0, 800, 450)
        self.start_game_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_game_button.setStyleSheet("background-color: none; font-family: Lucida Handwriting;"
                                             "font-size: 100px")
        self.start_game_button.clicked.connect(self.start_game)
        # Timer
        self.timer = QTimer()

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
        # Question number label:
        self.question_number_label.setGeometry(350, 10, 215, 40)
        self.question_number_label.setAlignment(Qt.AlignCenter)
        self.question_number_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                                 "font-family: Lucida Handwriting; font-size: 34px")
        # Time left label:
        self.time_left_label.setGeometry(575, 10, 215, 40)
        self.time_left_label.setAlignment(Qt.AlignCenter)
        self.time_left_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                           "font-family: Lucida Handwriting; font-size: 34px")
        # Question label :
        self.question_label.setGeometry(350, 60, 440, 270)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                          "font-family: Lucida Handwriting; font-size: 100px")
        # Input label :
        self.input_label.setText(self.input_label_value)
        self.input_label.setGeometry(350, 340, 440, 100)
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setStyleSheet("background-color: lightgrey; border-radius: 12px;"
                                       "font-family: Lucida Handwriting; font-size: 62px")

    def input_number(self, number):
        self.input_label_value += str(number)
        self.input_label.setText(self.input_label_value)

    def input_backspace(self):
        self.input_label_value = self.input_label_value[:-1]
        self.input_label.setText(self.input_label_value)

    def input_enter(self):
        self.answer(self.input_label_value)
        self.input_label_value = ""
        self.input_label.setText(self.input_label_value)

    def start_game(self):
        self.start_game_button.hide()
        self.timer.timeout.connect(self.time_passed)
        self.timer.start(1000)
        self.make_question()

    def time_passed(self):
        self.time_left -= 1
        if self.time_left >= 0:
            self.time_left_label.setText(str(self.time_left) + 's')
            return
        self.timer.stop()
        self.app.launchRecapMenu((self.question_number-1, self.correct, self.bad))

    def make_question(self):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        self.question_res = x*y
        self.question = f"{x}x{y}"
        self.question_label.setText(str(self.question))
        self.question_number += 1
        self.question_number_label.setText(str(self.question_number))

    def answer(self, value):
        if int(value) == int(self.question_res):
            self.correct += 1
        elif int(value) != int(self.question_res):
            self.bad += 1
        self.make_question()

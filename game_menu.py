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


class GameMenu(QFrame):
    def __init__(self, app, game):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app

        self.right_frame = QFrame(self)
        self.right_frame.setObjectName("game_frames")
        # Input label :
        self.input_label = QLabel(self.right_frame)
        self.input_label_value = ""
        # Game values :
        self.game = game
        self.correct = 0
        self.bad = 0
        self.time_left = 30
        self.question_res = None
        self.question_number = 0
        self.question = ""
        # Launching global items (as attributes) :
        self.time_left_label = QLabel(str(self.time_left)+'s', self.right_frame)
        self.question_number_label = QLabel(str(self.question_number), self.right_frame)
        self.question_label = QLabel(str(self.question), self.right_frame)
        # Launching frame items :
        self.init_frame_items()
        # Start game default.css :
        self.start_game_button = QPushButton(self)
        self.start_game_button.setText("Ready ?")
        self.start_game_button.setGeometry(0, (self.app.h//2)-((self.app.h//2)//2), self.app.w, self.app.h//2)
        self.start_game_button.setFont(QFont("", 100))
        self.start_game_button.setObjectName("start_button")
        self.start_game_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_game_button.setStyleSheet(self.app.css)
        self.start_game_button.clicked.connect(self.start_game)
        # Timer
        self.timer = QTimer()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Numpad frame :
        numpad_frame = QFrame(self)
        numpad_frame.setGeometry(QRect(10, 10, (w//2)-20, h-20))
        numpad_frame.setObjectName("game_frames")
        numpad_frame.setStyleSheet(self.app.css)
        # Numpad buttons :
        numpad_values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '<', '0', 'V')
        numpad_frame_size = numpad_frame.size()
        numpad_w = numpad_frame_size.width()
        numpad_h = numpad_frame_size.height()
        for i in range(4):
            for j in range(3):
                n = i*3+j
                button = QPushButton(numpad_frame)
                button.setFont(QFont("", 100))
                button.setStyleSheet(self.app.css)
                button.setText(numpad_values[n])
                button.setGeometry((j*numpad_w//3)+10, (i*numpad_h//4)+10, (numpad_w//3)-20, (numpad_h//4)-20)
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
                    elif n == 10:
                        button.setShortcut("à")
                elif n == 9:
                    button.clicked.connect(partial(self.input_backspace))
                    button.setShortcut(Qt.Key_Backspace)
                elif n == 11:
                    button.clicked.connect(partial(self.input_enter))
                    button.setShortcut(Qt.Key_Space)
        # Right frame :
        self.right_frame.setGeometry(QRect((w//2)+10, 10, (w//2)-20, h-20))
        self.right_frame.setStyleSheet(self.app.css)
        right_frame_size = self.right_frame.size()
        frame_w = right_frame_size.width()
        frame_h = right_frame_size.height()
        # Question number label:
        self.question_number_label.setGeometry(10, 10, (frame_w//2)-15, frame_h//4)
        self.question_number_label.setAlignment(Qt.AlignCenter)
        self.question_number_label.setFont(QFont("", 30))
        self.question_number_label.setObjectName("game_labels")
        self.question_number_label.setStyleSheet(self.app.css)
        # Time left label:
        self.time_left_label.setGeometry((frame_w//2)+5, 10, (frame_w//2)-15, frame_h//4)
        self.time_left_label.setAlignment(Qt.AlignCenter)
        self.time_left_label.setFont(QFont("", 30))
        self.time_left_label.setObjectName("game_labels")
        self.time_left_label.setStyleSheet(self.app.css)
        # Question label :
        self.question_label.setGeometry(10, (frame_h//4)+20, frame_w-20, (frame_h//2)-20)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setFont(QFont("", 100))
        self.question_label.setObjectName("game_labels")
        self.question_label.setStyleSheet(self.app.css)
        # Input label :
        self.input_label.setText(self.input_label_value)
        self.input_label.setGeometry(10, ((frame_h//4)*3)+10, frame_w-20, (frame_h//4)-20)
        self.input_label.setFont(QFont("", 30))
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_label.setObjectName("game_labels")
        self.input_label.setStyleSheet(self.app.css)

    def input_number(self, number):
        self.input_label_value += str(number)
        self.input_label.setText(self.input_label_value)

    def input_backspace(self):
        self.input_label_value = self.input_label_value[:-1]
        self.input_label.setText(self.input_label_value)

    def input_enter(self):
        if self.input_label_value == '':
            return
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
        self.question = f"{x}×{y}"
        self.question_label.setText(str(self.question))
        self.question_number += 1
        self.question_number_label.setText(str(self.question_number))

    def answer(self, value):
        if int(value) == int(self.question_res):
            self.correct += 1
        elif int(value) != int(self.question_res):
            self.bad += 1
        self.make_question()

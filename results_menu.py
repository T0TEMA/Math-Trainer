# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
# Other programmed files :


class RecapMenu(QFrame):
    def __init__(self, app, game_data):
        super().__init__()
        self.app = app
        self.data = game_data
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        # Back to main menu :
        back_button = QPushButton("<", self)
        back_button.setGeometry(20, 20, 60, 60)
        back_button.setStyleSheet(open("gui/button.css").read())
        back_button.clicked.connect(self.app.launchMainMenu)
        # Title label:
        title_label = QLabel("Results", self)
        title_label.setGeometry(290, 0, 405, 100)
        title_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 52px; color: lightgrey;')
        # Result_frame :
        result_frame = QFrame(self)
        result_frame.setGeometry(20, 100, 760, 330)
        result_frame.setStyleSheet('background-color: darkgrey; border-radius: 12px')
        # Number of questions answered label :
        n_questions_label = QLabel("Questions : "+str(self.data[0]), result_frame)
        n_questions_label.setGeometry(20, 20, 720, 25)
        n_questions_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 32px; color: black;')
        # Correct answers :
        n_correct_label = QLabel("Correct : "+str(self.data[1]), result_frame)
        n_correct_label.setGeometry(20, 140, 720, 25)
        n_correct_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 32px; color: black;')
        # Bad answers :
        n_bad_label = QLabel("Bad : "+str(self.data[2]), result_frame)
        n_bad_label.setGeometry(20, 280, 720, 25)
        n_bad_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 32px; color: black;')

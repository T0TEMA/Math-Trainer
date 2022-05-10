# Standard libraries :
# Downloaded libraries :
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
# Other programmed files :


class SettingsMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        # Back to main menu :
        back_button = QPushButton(self)
        back_button.setText("<")
        back_button.setGeometry(10, 10, 40, 40)
        back_button.setStyleSheet(open("gui/button.css").read())
        back_button.clicked.connect(self.app.launchMainMenu)
        # Title label:
        title_label = QLabel(self)
        title_label.setText("Settings")
        title_label.setGeometry(270, 0, 400, 100)
        title_label.setStyleSheet('font-family: Lucida Handwriting; font-size: 52px; color: lightgrey;')

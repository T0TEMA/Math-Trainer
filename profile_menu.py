# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
# Other programmed files :


class ProfileMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        # Back to main menu :
        back_button = QPushButton(self)
        back_button.setText("<")
        back_button.setGeometry(20, 20, 60, 60)
        back_button.setStyleSheet(self.app.css)
        back_button.clicked.connect(self.app.launchMainMenu)
        # Title label:
        title_label = QLabel(self)
        title_label.setText("Profile")
        title_label.setGeometry(290, 0, 405, 100)
        title_label.setObjectName("title_label")
        title_label.setStyleSheet(self.app.css)

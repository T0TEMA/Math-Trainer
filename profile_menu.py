# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
# Other programmed files :
from data.manage_file import UserData
from item_creator import create_button, create_label, create_frame


class ProfileMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Load user data :
        self.userdata = UserData()
        # Launch frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        info = self.userdata.content
        create_label(self, "Profile", 0, 10, w, 120, 1, Qt.AlignCenter, "title_label", self.app.css)    # Title label
        create_button(self, "<", 20, 20, 100, 100, 1, "", self.app.css, self.app.launchMainMenu, "Esc") # Back to main menu
        frame = create_frame(self, 10, (h//4)-10, w-20, ((h//4)*3)-20, self.app.css)
        frame_w = frame.size().width()
        frame_h = frame.size().height()
        create_label(frame, info['games'], 10, 10, frame_w-10, (frame_h//4)-10, 1, Qt.AlignLeft, "", self.app.css)     # Total games played
        create_label(frame, info['question'], 10, (frame_h//4)+20, frame_w-10, (frame_h//4)-10, 1, Qt.AlignLeft, "", self.app.css)  # Total question answered
        create_label(frame, info['correct'], 10, ((frame_h//4)*2)+30, frame_w-10, (frame_h//4)-10, 1, Qt.AlignLeft, "", self.app.css)   # Total correct answers
        create_label(frame, info['bad'], 10, ((frame_h//4)*3)+40, frame_w-10, (frame_h//4)-10, 1, Qt.AlignLeft, "", self.app.css)       # Total bad answers


"""
"Set Object Name" is used in the '.css' file to assign a part of the styling sheet to a given item
in the window.
"""
# Standard libraries :
# Downloaded libraries :
import PyQt5
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
# Other programmed files :
from item_creator import create_button, create_label


class MainMenu(QFrame):
    def __init__(self, app):
        super().__init__()
        # 'Application' object.
        self.app: PyQt5.QtWidgets.QMainWindow = app
        # Launching frame items :
        self.init_frame_items()

    def init_frame_items(self):
        w = self.app.w
        h = self.app.h
        # Title label:
        create_label(self, "Math Trainer", 0, 0, w, h//2, 0.5, Qt.AlignCenter, "title_label", self.app.css)
        # Settings button :
        create_button(self, "Settings", (w//2)-300, (h//2)-60, 290, 100, 0.75, "", self.app.css, self.app.launchSettingsMenu)
        # Profile button :
        create_button(self, "Profile", (w//2)+10, (h//2)-60, 290, 100, 0.75, "", self.app.css, self.app.launchProfileMenu)
        # Play button :
        create_button(self, "Play !", (w//2)-300, (h//2)+60, 600, 100, 1, "", self.app.css, self.app.launchSelectionMenu)
        # Rights label:
        create_label(self, "Totema's projects (2022)", 10, h-30, w-10, 30, 1, Qt.AlignLeft, "rights_label", self.app.css)

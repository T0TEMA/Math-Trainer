"""
Author : Totema

File containing the functions that create Qt items.
"""
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFont


def create_button(dock, text: str, x: int, y: int, w: int, h: int, cx: float, name: str, style, action, shortcut=None):
    item = QPushButton(dock)
    item.setText(text)
    item.setGeometry(x, y, w, h)
    item.setFont(QFont("", int(calculate_font_size(w, h)*cx)))
    item.setObjectName(name)
    item.setStyleSheet(style)
    item.setCursor(QCursor(Qt.PointingHandCursor))
    item.clicked.connect(action)
    if shortcut is not None:
        item.setShortcut(shortcut)
    return item


def create_label(dock, text: str, x: int, y: int, w: int, h: int, cx: float, alignment: Qt.Alignment, name: str, style):
    item = QLabel(dock)
    item.setText(text)
    item.setGeometry(x, y, w, h)
    item.setFont(QFont("", int(calculate_font_size(w, h)*cx)))
    item.setAlignment(alignment)
    item.setObjectName(name)
    item.setStyleSheet(style)
    return item


def create_combobox(dock, items: list, index: int, x: int, y: int, w: int, h: int, cx: float, name: str, style, action):
    item = QComboBox(dock)
    item.addItems(items)
    item.setCurrentIndex(index)
    item.setGeometry(x, y, w, h)
    item.setFont(QFont("", int(calculate_font_size(w, h)*cx)))
    item.setObjectName(name)
    item.setStyleSheet(style)
    item.currentIndexChanged.connect(action)
    return item


def create_frame(dock, x: int, y: int, w: int, h: int, style):
    item = QFrame(dock)
    item.setGeometry(x, y, w, h)
    item.setStyleSheet(style)
    return item


def calculate_font_size(w, h):
    if w <= h:
        size = w*0.45
    else:
        size = h*0.45
    return size

import json

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget, QTextBrowser, QVBoxLayout

from util.config_loader import ConfigLoader

CHAR_SETTINGS_URL = "/home/toni/Projects/TextGatherer/config/char_settings.json"


class DisplayWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.display_window = QTextBrowser()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._init_ui()

    def _init_ui(self):
        self.display_window.setFont(ConfigLoader.get_font())
        self.layout.addWidget(self.display_window)

    def set_text(self, plain_text: str):
        with open(CHAR_SETTINGS_URL, "r") as f:
            conv = json.load(f)

        for char in conv:
            plain_text = plain_text.replace(f"\\{char}", conv[char])

        self.display_window.setText(plain_text)

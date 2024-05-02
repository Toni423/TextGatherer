import json

from PyQt6.QtWidgets import QLabel, QWidget, QTextBrowser, QVBoxLayout

CHAR_SETTINGS_URL = "/home/toni/Projects/TextGatherer/char_settings.json"


class DisplayWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.display_window = QTextBrowser()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._init_ui()

    def _init_ui(self):
        header = QLabel()
        header.setText("Display")
        self.layout.addWidget(header)

        self.layout.addWidget(self.display_window)

    def set_text(self, plain_text: str):
        with open(CHAR_SETTINGS_URL, "r") as f:
            conv = json.load(f)

        for char in conv:
            plain_text = plain_text.replace(f"\\{char}", conv[char])

        self.display_window.setText(plain_text)

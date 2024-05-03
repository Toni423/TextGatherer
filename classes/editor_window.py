from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget, QTextEdit, QVBoxLayout

from util.config_loader import ConfigLoader


class EditorWindow(QWidget):

    def __init__(self, text):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.edit_window = QTextEdit()
        self.edit_window.setPlainText(text)
        self._init_ui()

    def _init_ui(self):
        self.edit_window.setFont(ConfigLoader.get_font())
        self.layout.addWidget(self.edit_window)

    @property
    def plain_text(self) -> str:
        return self.edit_window.toPlainText()

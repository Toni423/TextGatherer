from PyQt6.QtWidgets import QTextEdit, QVBoxLayout

from src.classes.numbered_text_edit import NumberedTextEdit
from src.util.config_loader import ConfigLoader


class EditorWindow(QTextEdit):

    def __init__(self, text):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.edit_window = NumberedTextEdit()
        self.edit_window.setPlainText(text)
        self._init_ui()

    def _init_ui(self):
        self.edit_window.setFont(ConfigLoader.get_font())
        self.layout.addWidget(self.edit_window)

    @property
    def plain_text(self) -> str:
        return self.edit_window.toPlainText()

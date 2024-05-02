from PyQt6.QtWidgets import QLabel, QWidget, QTextEdit, QVBoxLayout

DOCUMENT_URL = "/home/toni/Projects/TextGatherer/document"


class EditorWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.edit_window = QTextEdit()
        with open(DOCUMENT_URL, "r") as f:
            self.edit_window.setPlainText(f.read())
        self._init_ui()

    def _init_ui(self):
        header = QLabel()
        header.setText("Editor")
        self.layout.addWidget(header)

        self.layout.addWidget(self.edit_window)

    @property
    def plain_text(self) -> str:
        return self.edit_window.toPlainText()

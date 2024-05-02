from PyQt6.QtWidgets import QStackedWidget

from classes.display_window import DisplayWindow
from classes.editor_window import EditorWindow


class TextStack(QStackedWidget):

    def __init__(self):
        super().__init__()
        self.editor_window = EditorWindow()
        self.addWidget(self.editor_window)
        self.display_window = DisplayWindow()
        self.addWidget(self.display_window)


    def change_display_mode(self):
        if self.currentIndex() == 1:
            self.setCurrentIndex(0)
            return

        self.display_window.set_text(self.editor_window.plain_text)
        self.setCurrentIndex(1)

    @property
    def plain_text(self) -> str:
        return self.editor_window.plain_text

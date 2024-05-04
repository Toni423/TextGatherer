import json
from pathlib import Path

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

import project
from src.classes.text_stack import TextStack
from src.util.plus_tab_widget import PlusTabWidget


class TabGatherer(QWidget):

    def __init__(self):
        super().__init__()
        self._display_mode = 0
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._header = QLabel()
        self._header.setText("Editor")
        self.layout.addWidget(self._header)

        self.tabs = PlusTabWidget()
        self.layout.addWidget(self.tabs)

    def change_display_mode(self):
        if self._display_mode == 1:
            for ind in range(self.tabs.count()):
                self.tabs.widget(ind).to_edit_mode()
            self._display_mode = 0
            self._header.setText("Editor")
            return

        for ind in range(self.tabs.count()):
            self.tabs.widget(ind).to_display_mode()
        self._header.setText("Display")
        self._display_mode = 1


    def load_files(self):
        self.tabs.clear()
        with open(Path(project.STORAGE_PATH) / "file.json", "r") as f:
            data = json.load(f)

        for file in data:
            stack = TextStack(data[file])
            self.tabs.addTab(stack, file)

    def save_files(self):
        data = {}

        for ind in range(self.tabs.count()):
            data.update({self.tabs.tabText(ind): self.tabs.widget(ind).plain_text})

        with open(Path(project.STORAGE_PATH) / "file.json", "w") as f:
            json.dump(data, f)

import json
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, \
    QMainWindow, QStackedWidget

from classes.text_stack import TextStack

DOCUMENT_URL = "/home/toni/Projects/TextGatherer/document"
CHAR_SETTINGS_URL = "/home/toni/Projects/TextGatherer/char_settings.json"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_stack = TextStack()
        self.init_ui()

    def init_ui(self):
        # Create a central widget and set the main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create buttons layout
        buttons_layout = QHBoxLayout()


        # Add buttons to the buttons layout
        button1 = QPushButton("Save")
        button1.clicked.connect(lambda x: self.save_button_clicked(self.text_stack.plain_text))
        button2 = QPushButton("Change display")
        button2.clicked.connect(self.text_stack.change_display_mode)
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)


        # Add layouts and widgets to the main layout
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.text_stack)

        # Set window title and size
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 600, 400)

    @staticmethod
    def save_button_clicked(text: str):
        with open(DOCUMENT_URL, 'w') as f:
            f.write(text)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

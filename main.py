import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QMainWindow

from classes.tab_gatherer import TabGatherer

CHAR_SETTINGS_URL = "/home/toni/Projects/TextGatherer/config/char_settings.json"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tab_gatherer = TabGatherer()
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
        button1.clicked.connect(self.tab_gatherer.save_files)
        button2 = QPushButton("Change display")
        button2.clicked.connect(self.tab_gatherer.change_display_mode)
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)


        # Add layouts and widgets to the main layout
        main_layout.addLayout(buttons_layout)
        self.tab_gatherer.load_files()
        main_layout.addWidget(self.tab_gatherer)

        # Set window title and size
        self.setWindowTitle("TextGatherer")
        self.setGeometry(1200, 300, 800, 800)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

import configparser

from PyQt6.QtGui import QFont

CONFIG_URL = "/home/toni/Projects/TextGatherer/config/config.ini"


class ConfigLoader:
    @staticmethod
    def get_settings():
        config = configparser.ConfigParser()
        config.read(CONFIG_URL)
        return config['Settings']

    @staticmethod
    def get_setting(name: str):
        return ConfigLoader.get_settings()[name]

    @staticmethod
    def get_font() -> QFont:
        font = QFont()
        font.setPointSize(int(ConfigLoader.get_setting("text_size")))
        return font

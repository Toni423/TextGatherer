import os
from pathlib import Path



def project_root() -> str:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.exists(Path(current_dir) / 'project.py'):
            return current_dir
        # Move up one directory
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            # Reached the filesystem root, project.py not found
            raise FileNotFoundError("project.py not found in project directory")
        current_dir = parent_dir


CHAR_SETTINGS_PATH = Path(project_root()) / "config" / "char_settings.json"
CONFIG_PATH = Path(project_root()) / "config" / "config.ini"
STORAGE_PATH = Path(project_root()) / "storage"

if __name__ == "__main__":
    project_config = project_root()
    print("Project configuration loaded:", project_config)

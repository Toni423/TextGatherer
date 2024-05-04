from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QTabWidget, QPushButton, QTabBar, QLineEdit, QVBoxLayout

from classes.text_stack import TextStack


class PlusTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        # Create a custom tab bar
        self.setTabBar(EditableTabBar(self))

        self.addButton = QPushButton()
        self.addButton.setText("+")
        self.addButton.font().setBold(True)
        self.setCornerWidget(self.addButton)
        self.addButton.clicked.connect(self.add_new_tab)

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(lambda x: self.removeTab(x))
        # Add initial tab
        self.add_new_tab()

    tabBarDoubleClicked = pyqtSignal(int)

    def add_new_tab(self):
        # Create a new tab
        new_tab_index = self.count()
        new_tab = TextStack("")
        self.insertTab(new_tab_index, new_tab, f"Tab {new_tab_index + 1}")



class EditableTabBar(QTabBar):
    def __init__(self, parent: PlusTabWidget):
        super().__init__(parent)
        self._parent = parent

    tabDoubleClicked = pyqtSignal(int)

    def mouseDoubleClickEvent(self, event):
        tab_index = self.tabAt(event.pos())
        self.tabDoubleClicked.emit(tab_index)
        self.start_rename(tab_index)

    def start_rename(self, tab_index):
        self.__edited_tab = tab_index
        rect = self.tabRect(tab_index)
        top_margin = 3
        left_margin = 6
        self.__edit = QLineEdit(self)
        self.__edit.show()
        self.__edit.move(rect.left() + left_margin, rect.top() + top_margin)
        self.__edit.resize(rect.width() - 2 * left_margin, rect.height() - 2 * top_margin)
        self.__edit.setText(self.tabText(tab_index))
        self.__edit.selectAll()
        self.__edit.setFocus()
        self.__edit.editingFinished.connect(self.finish_rename)

    @pyqtSlot()
    def finish_rename(self):
        self.setTabText(self.__edited_tab, self.__edit.text())
        self.__edit.deleteLater()


from PyQt6.QtGui import QPainter, QPalette, QColor
from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import Qt, QRect


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor: NumberedTextEdit = editor

    def paintEvent(self, event):
        painter = QPainter(self)
        block = self.editor.firstVisibleBlock()
        block_number = block.blockNumber()
        height = self.editor.height()
        font_metrics = painter.fontMetrics()
        top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
        bottom = top + height



        painter.setFont(self.editor.font())
        painter.setPen(Qt.GlobalColor.lightGray)

        while block.isValid() and top <= bottom:
            height = self.editor.blockBoundingRect(block).height()
            if block.isVisible() and top + height >= 0:
                number = str(block_number + 1)
                painter.drawText(0, int(top), self.width(), font_metrics.height(),
                                 Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, number)
            top += height
            block = block.next()
            block_number += 1

        painter.end()

    def width(self):
        max_digits = max(1, len(str(self.editor.blockCount())))
        return 3 + self.editor.fontMetrics().horizontalAdvance('9') * max_digits


class NumberedTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.line_number_area = LineNumberArea(self)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Highlight, QColor(200, 180, 255))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("black"))
        self.setPalette(palette)


        self.setViewportMargins(self.line_number_area.width(), 0, 0, 0)
        self.update_line_number_area_width()

        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)

    def update_line_number_area_width(self):
        self.setViewportMargins(self.line_number_area.width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.line_number_area.width(), cr.height()))


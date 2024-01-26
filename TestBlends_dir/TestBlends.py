from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter, QImage, QPixmap
from PyQt6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QApplication,
    QGraphicsRectItem,
    QGraphicsRotation,
    QGraphicsEllipseItem,
    QWidget,
    QLabel,
    QVBoxLayout,
)
import numpy
from blend_modes import soft_light


class TestBlends:
    def __init__(self):
        self.height = 100
        self.width = 200
        self.start1 = 500
        self.start2 = self.start1 + self.width - 20
        self.start3 = self.start2 + self.width - 20

        self.canvas = QtGui.QPixmap(1440, 900)
        # self.canvas = QImage(1440, 900, QImage.Format.Format_RGB888)
        self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        # self.label.setPixmap(QPixmap.fromImage(self.canvas))
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, 1440, 900)
        self.label.setWindowTitle("Rotating Shapes")
        self.label.show()

    def start(self):
        self.painter = QPainter(self.canvas)
        self.painter.begin(self.canvas)

        brush = QBrush()
        # brush.setColor(QtGui.QColor('green'))
        self.painter.setCompositionMode(
            QPainter.CompositionMode.CompositionMode_Multiply
        )
        brush.setColor(QtGui.QColor("yellow"))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.painter.setBrush(brush)

        self.painter.drawRect(self.start1, 300, self.width, self.height)

        brush.setColor(QtGui.QColor("red"))
        self.painter.setBrush(brush)

        self.painter.drawRect(self.start2, 300, self.width, self.height)

        brush.setColor(QtGui.QColor("blue"))
        self.painter.setBrush(brush)
        self.painter.drawRect(self.start3, 300, self.width, self.height)

        self.painter.save()
        self.painter.restore()
        self.painter.end()

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
from main_utility_functions.utility import get_screen_corner_distance


class TestBlends:
    def __init__(self):
        self.canvasHeight = 900
        self.canvasWidth = 1440
        self.height = 100
        self.width = 200
        self.startx = 100
        self.starty = 0
        self.loopRadius = get_screen_corner_distance(
            self.canvasWidth / 2, self.canvasHeight / 2
        )  # self.canvasWidth / 2 - self.width / 2
        self.shapeCount = 50
        self.rotationIncrement = 360 / self.shapeCount
        self.curRotationAngle = 0

        self.canvas = QtGui.QPixmap(self.canvasWidth, self.canvasHeight)
        self.canvas.fill(QtGui.QColor("black"))
        self.start()

        self.label = QLabel()
        # self.label.setPixmap(QPixmap.fromImage(self.canvas))
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvasWidth, self.canvasHeight)
        self.label.setWindowTitle("Rotating Shapes")
        self.label.show()

    def start(self):
        self.painter = QPainter(self.canvas)
        self.painter.begin(self.canvas)

        pen = QPen()
        # brush.setColor(QtGui.QColor('green'))

        pen.setColor(QtGui.QColor("yellow"))
        pen.setWidth(3)
        self.painter.setPen(pen)

        self.painter.translate(self.canvasWidth / 2, self.canvasHeight / 2)
        # self.painter.save()

        while self.shapeCount > 1:
            self.painter.save()
            self.painter.rotate(self.curRotationAngle)

            inputWidth = -self.width / 2
            inputHeight = self.height / 2 + self.loopRadius - 100
            print(inputWidth, inputHeight)
            self.painter.translate(inputWidth, inputHeight)

            self.painter.drawRect(0, 0, self.width, self.height)
            self.curRotationAngle += self.rotationIncrement

            self.painter.restore()
            self.shapeCount -= 1

        # self.painter.save()
        # self.painter.restore()
        self.painter.end()

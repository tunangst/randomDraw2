from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point
from Mandala_dir.Mandala import Mandala
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QTransform
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem
import sys
import math


class Rotating_shapes(Mandala):
    def __init__(self):
        super().__init__()
        print('~~~~~ in Rotating_shapes_style ~~~~~~~~')

        self.graphic_scene = QGraphicsScene(
            0, 0, self.canvas_width, self.canvas_height)
        # print(self.center_point)
        self.start()

    def start(self):
        current_degrees = 0
        # loop over number of circles chosen
        while self.number_of_replication_circles > 0:
            circles_index = self.number_of_replication_circles - 1
            print(circles_index)
            # loop over number of shape counts chosen
            while self.shape_count_array[circles_index] > 0:

                shape_width = 100
                shape_height = 10
                shape_center = get_shape_center_point(
                    shape_width, shape_height)
                rotation_center = get_shape_center_rotation_point(
                    self.shape_depth_array[circles_index], self.center_point)
                # build shape at graph origin
                ellipse = QGraphicsEllipseItem(0, 0, shape_width, shape_height)
                # set center to shape center for initial move
                ellipse.setTransformOriginPoint(
                    QPointF(shape_center[0], shape_center[1]))
                # move shape to width center at chosen depth
                ellipse.setPos(
                    QPointF(self.center_point[0], self.shape_depth_array[circles_index]))
                # set transformation point to center based on new shape initialized position
                ellipse.setTransformOriginPoint(
                    QPointF(rotation_center[0], rotation_center[1]))
                # print(rotation_center)
                ellipse.setRotation(current_degrees)
                current_degrees += self.shape_rotation_array[circles_index]

                brush = QBrush(Qt.GlobalColor.blue)
                ellipse.setBrush(brush)
                self.graphic_scene.addItem(ellipse)
                self.shape_count_array[circles_index] -= 1
            self.number_of_replication_circles -= 1
        # ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        # brush = QBrush(Qt.GlobalColor.blue)
        # ellipse.setBrush(brush)
        self.rotating_shapes_board = QGraphicsView(self.graphic_scene)
        self.rotating_shapes_board.setWindowTitle(
            "randomDraw2 Canvas")
        self.rotating_shapes_board.showMaximized()
        self.rotating_shapes_board.show()
        return self.rotating_shapes_board

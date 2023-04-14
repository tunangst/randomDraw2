from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color
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
            shape = self.shape_object_array[circles_index]
            print(circles_index)
            print(shape)
            # loop over number of shape counts chosen
            selected_color = None
            if self.is_same_color_loops:
                selected_color = self.get_chosen_loop_color()
            while shape['chosen_count'] > 0:
                shape_center = get_shape_center_point(
                    shape['chosen_width'], shape['chosen_height'])
                rotation_center = get_shape_center_rotation_point(
                    shape['chosen_depth'], self.canvas_center_point)
                # build shape at graph origin
                ellipse = QGraphicsEllipseItem(
                    0, 0, shape['chosen_width'], shape['chosen_height'])
                # set center to shape center for initial move
                ellipse.setTransformOriginPoint(
                    QPointF(shape_center[0], shape_center[1]))
                # move shape to width center at chosen depth
                ellipse.setPos(
                    QPointF(self.canvas_center_point[0], shape['chosen_depth']))
                # set transformation point to center based on new shape initialized position
                ellipse.setTransformOriginPoint(
                    QPointF(rotation_center[0], rotation_center[1]))
                # print(rotation_center)
                ellipse.setRotation(current_degrees)
                current_degrees += shape['chosen_angle']

                if self.is_same_color_loops == False:
                    selected_color = self.get_chosen_loop_color()

                fill = QBrush(QtGui.QColor(
                    selected_color['r'], selected_color['g'], selected_color['b']))
                ellipse.setBrush(fill)

                # stroke = QPen(Qt.GlobalColor.blue)
                stroke = QPen(QtGui.QColor(
                    self.color_theme[0]['r'], self.color_theme[0]['g'], self.color_theme[0]['b']))
                stroke.setWidth(shape['chosen_stroke'])
                ellipse.setPen(stroke)
                # fill = QBrush(Qt.GlobalColor.blue)
                # ellipse.setBrush(fill)
                self.graphic_scene.addItem(ellipse)
                shape['chosen_count'] -= 1
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

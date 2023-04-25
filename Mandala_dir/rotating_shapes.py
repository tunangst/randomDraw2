from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color
from Mandala_dir.Mandala import Mandala
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem, QWidget, QLabel, QVBoxLayout
import sys
import math
from pprint import pprint


class Rotating_shapes(Mandala):
    def __init__(self):
        super().__init__()
        print('~~~~~ in Rotating_shapes_style ~~~~~~~~')

        self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle('Rotating Shapes')
        self.label.show()

    def start(self):
        circles_index = self.number_of_replication_circles - 1
        shape = self.shape_object_array[circles_index]
        shape_center = get_shape_center_point(
            shape['chosen_width'], shape['chosen_height'])

        self.current_degrees = 0

        painter = QPainter(self.canvas)

        temp_index = 1
        # loop over number of circles chosen
        while temp_index > 0:
            # while self.number_of_replication_circles > 0:
            temp_index -= 1

            painter.translate(
                self.canvas_center_point[0], self.canvas_center_point[1])
            painter.save()

            circles_index = self.number_of_replication_circles - 1
            shape = self.shape_object_array[circles_index]

            # shape['chosen_width'] = 200
            # shape['chosen_height'] = 100
            # shape['chosen_depth'] = 200
            # shape['chosen_count'] = 20
            # shape['chosen_angle'] = 360/shape['chosen_count']

            self.shape_center = get_shape_center_point(
                shape['chosen_width'], shape['chosen_height'])

            # painter.translate(
            #     self.canvas_center_point[0], shape['chosen_depth'])
            # painter.translate(
            #     self.canvas_center_point[0] - shape_center[0], shape['chosen_depth'] - shape_center[1])
            while shape['chosen_count'] > 0:

                # painter.setRenderHint(QPainter.Antialiasing)
                # pen = QtGui.QPen()
                # pen.setWidth(15)
                # pen.setColor(QtGui.QColor('blue'))
                # painter.setPen(pen)

                painter.drawLine(0, 0, 10, 10)

                # print(current_degrees)
                # print(shape['chosen_count'])
                self.draw_shape(painter, shape)

                # painter.drawEllipse(
                #     0, 0, shape['chosen_width'], shape['chosen_height'])
                self.current_degrees += shape['chosen_angle']

                shape['chosen_count'] -= 1
            painter.restore()
        painter.end()

    def draw_shape(self, painter, shape):
        print('shape width: ', shape['chosen_width'])
        print('half shape width: ', self.shape_center[0])
        print('shape height: ', shape['chosen_height'])
        print('half shape height: ', self.shape_center[1])

        print(-self.shape_center[0],
              self.shape_center[1] - shape['chosen_depth'])
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        print(self.current_degrees)
        print(shape['chosen_count'])

        # painter.translate(
        #     self.canvas_center_point[0] - shape_center[0], shape['chosen_depth'] - shape_center[1])
        # painter.translate(
        #     self.canvas_center_point[0], self.canvas_center_point[1])
        # print(shape_center, shape['chosen_depth'])
        # print(-int(shape['chosen_width']/2), -int(shape['chosen_height']/2),
        #       int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        painter.save()
        painter.rotate(self.current_degrees)
        painter.translate(-self.shape_center[0],
                          self.shape_center[1] - shape['chosen_depth'])
        # painter.translate(-100, -shape['chosen_depth'])
        painter.drawEllipse(
            0, 0, shape['chosen_width'], shape['chosen_height'])
        painter.restore()
        # painter.drawEllipse(0, 0, 200, 100)
        # painter.drawEllipse(
        #     -int(shape['chosen_width']/2), -int(shape['chosen_height']/2), int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        # painter.drawEllipse(
        #     0, 0, shape['chosen_width'], shape['chosen_height'])

# # depth + 1/2 shape height - 1/2 canvas height
#                 # stroke = QPen(Qt.GlobalColor.blue)
#                 stroke = QPen(QtGui.QColor(
#                     self.color_theme[0]['r'], self.color_theme[0]['g'], self.color_theme[0]['b']))
#                 stroke.setWidth(shape['chosen_stroke'])
#                 ellipse.setPen(stroke)
#                 # fill = QBrush(Qt.GlobalColor.blue)
#                 # ellipse.setBrush(fill)
#                 self.graphic_scene.addItem(ellipse)
#                 ellipse = None
#                 shape['chosen_count'] -= 1
#             self.number_of_replication_circles -= 1

        # self.rotating_shapes_board = QGraphicsView(self.graphic_scene)
        # self.rotating_shapes_board.setWindowTitle(
        #     "randomDraw2 Canvas")
        # self.rotating_shapes_board.showMaximized()
        # self.rotating_shapes_board.show()
        # return self.rotating_shapes_board

    # def updateTransform(self , target: QGraphicsSvgItem , newValue: Any):

    # def find_y_transformation_to_canvas_center(self, shape_depth, shape_center_y):
    #     cp = self.canvas_center_point[1]
    #     d = shape_depth
    #     sh = shape_center_y
    #     result = None
    #     if d + sh < cp:
    #         result = cp - (d + sh)
    #     elif d < cp and d+sh > cp:
    #         result = (cp - (d+sh))*-1
    #     elif d < 0 and (d + sh) > 0:
    #         result = cp - (d+sh)*-1
    #     elif d < 0 and (d+sh) < 0:
    #         result = cp - (d+sh)
    #     else:
    #         print('out of scope in find_y_transformation_to_canvas_center')
    #     return result

    # def updateTransform(self, target: QGraphicsEllipseItem, newValue):
    #     origin = target.transformOriginPoint()
    #     transform = QTransform().translate(origin.x(), origin.y())
    #     # transform.scale(newValue[0], newValue[1])
    #     transform.translate(-origin.x(), -origin.y())
    #     target.setTransform(transform)

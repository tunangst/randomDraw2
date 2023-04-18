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
        # self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle('Rotating Shapes')
        self.label.show()

    def start(self):
        from random import randint
        painter = QPainter(self.canvas)
        # painter.setRenderHint(QPainter.Antialiasing)
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(
            QtCore.QPoint(100, 100),
            QtCore.QPoint(300, 200)
        )
        painter.end()

        # self.addLayout(self.pixmap)
        # painter = QPainter(self.container.pixmap())
        # stroke = QPen(QtGui.QColor('red'))
        # stroke.setWidth(10)
        # painter.setPen(stroke)

        # # painter.begin(self)
        # painter.drawLine(10, 10, 300, 200)

        # painter.end()

        # painter.show()
        # return self

#         current_degrees = 0
#         # loop over number of circles chosen
#         temp_index = 1
#         while temp_index > 0:
#             # while self.number_of_replication_circles > 0:
#             temp_index -= 1
#             circles_index = self.number_of_replication_circles - 1
#             shape = self.shape_object_array[circles_index]
#             shape['chosen_height'] = 200
#             shape['chosen_depth'] = 200
#             shape['chosen_angle'] = 36
#             shape['chosen_count'] = 10
#             print(circles_index)
#             print(shape)
#             print('depth, canvas y, shape height')
#             print(shape['chosen_depth'],
#                   self.canvas_center_point[1], shape['chosen_height'])
#             # loop over number of shape counts chosen
#             selected_color = None
#             if self.is_same_color_loops:
#                 selected_color = self.get_chosen_loop_color()
#             while shape['chosen_count'] > 0:
#                 # temp_index = 6
#                 # while temp_index > 0:
#                 shape_center = get_shape_center_point(
#                     shape['chosen_width'], shape['chosen_height'])
#                 print('shape x center, shape y center: ', shape_center)
#                 print('shape width, height: ',
#                       shape['chosen_width'], shape['chosen_height'])
#                 # rotation_center = get_shape_center_rotation_point(
#                 #     shape['chosen_depth'], self.canvas_center_point)
#                 # build shape at graph origin
#                 ellipse = QGraphicsEllipseItem(
#                     0, 0, shape['chosen_width'], shape['chosen_height'])

#                 ellipse.setPos(
#                     QPointF(self.canvas_center_point[0] - shape_center[0], shape['chosen_depth']))

#                 ellipse.setTransformOriginPoint(
#                     shape_center[0], self.find_y_transformation_to_canvas_center(shape['chosen_depth'], shape_center[1] + shape_center[1]/2))
#                 ellipse.setRotation(current_degrees)
#                 current_degrees += shape['chosen_angle']

#                 if self.is_same_color_loops == False:
#                     selected_color = self.get_chosen_loop_color()

#                 fill = QBrush(QtGui.QColor(
#                     selected_color['r'], selected_color['g'], selected_color['b']))
#                 ellipse.setBrush(fill)


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

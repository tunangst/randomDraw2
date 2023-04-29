from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color, get_random_rgb_color, get_chosen_theme_color
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
        self.shape_color = None

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
        # shape_center = get_shape_center_point(
        #     shape['chosen_width'], shape['chosen_height'])

        self.current_degrees = 0

        self.painter = QPainter(self.canvas)
        if self.color_of_loops != 1:
            self.shape_color = self.draw_color(self.painter)

        temp_index = 1
        # loop over number of circles chosen
        while temp_index > 0:
            # while self.number_of_replication_circles > 0:
            temp_index -= 1
            # translate the canvas to middle of screen and save
            self.painter.translate(
                self.canvas_center_point[0], self.canvas_center_point[1])
            self.painter.save()

            circles_index = self.number_of_replication_circles - 1
            shape = self.shape_object_array[circles_index]
            # force controls
            shape['chosen_width'] = 200
            shape['chosen_height'] = 100
            shape['chosen_depth'] = 200
            shape['chosen_count'] = 20
            shape['chosen_angle'] = 360/shape['chosen_count']
            # shape['chosen_random_loop_color'] =

            self.shape_center = get_shape_center_point(
                shape['chosen_width'], shape['chosen_height'])

            while shape['chosen_count'] > 0:
                if (shape['chosen_random_loop_color']):
                    pass
                self.draw_color(shape)
                # selected_color = get_random_theme_color(self.color_theme)
                self.draw_shape(shape)

                # self.painter.drawEllipse(
                #     0, 0, shape['chosen_width'], shape['chosen_height'])
                self.current_degrees += shape['chosen_angle']

                shape['chosen_count'] -= 1
            self.painter.restore()
        self.painter.end()

    def draw_shape(self, shape):
        # print('shape width: ', shape['chosen_width'])
        # print('half shape width: ', self.shape_center[0])
        # print('shape height: ', shape['chosen_height'])
        # print('half shape height: ', self.shape_center[1])

        # print(-self.shape_center[0],
        #       self.shape_center[1] - shape['chosen_depth'])
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('blue'))
        self.painter.setPen(pen)
        # print(self.current_degrees)
        # print(shape['chosen_count'])

        # painter.translate(
        #     self.canvas_center_point[0] - shape_center[0], shape['chosen_depth'] - shape_center[1])
        # painter.translate(
        #     self.canvas_center_point[0], self.canvas_center_point[1])
        # print(shape_center, shape['chosen_depth'])
        # print(-int(shape['chosen_width']/2), -int(shape['chosen_height']/2),
        #       int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        self.painter.save()
        self.painter.rotate(self.current_degrees)
        self.painter.translate(-self.shape_center[0],
                               self.shape_center[1] - shape['chosen_depth'])
        # self.painter.translate(-100, -shape['chosen_depth'])
        self.painter.drawEllipse(
            0, 0, shape['chosen_width'], shape['chosen_height'])
        self.painter.restore()
        # self.painter.drawEllipse(0, 0, 200, 100)
        # self.painter.drawEllipse(
        #     -int(shape['chosen_width']/2), -int(shape['chosen_height']/2), int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        # self.painter.drawEllipse(
        #     0, 0, shape['chosen_width'], shape['chosen_height'])

    def draw_color(self, shape):
        color = None
        # loop_of_random_shape_color = True/False
        loop_of_random_shape_color = shape['chosen_random_loop_color']
        loop_index = shape['chosen_loop_index']
        # color_count 1=full random, 2=dual, 3=tri, 4=quad, 5=cint)
        # theme_type (1=random theme color, 2= cycle theme color)
        # self.theme_type
        self.color_count = 5

        match self.color_count:
            case 1:
                # full random, return random color every time
                color = get_random_rgb_color()

            case 2 | 3 | 4 | 5:
                print('in 2,3,4,5 draw_color')
                # not full random
                # is theme_type random or incremental?
                # if random, get_random_theme_color
                # if incremental, get random color
                self.theme_type = 2
                if (self.theme_type == 1):
                    # random pull
                    color = get_random_theme_color(self.color_theme)
                else:
                    # incremental
                    print('loop index', loop_index)
                    color = get_chosen_theme_color(
                        self.color_theme, loop_index)
                print(color)

                pass
            case _:
                print('out of scope in draw_color')

        brush = QtGui.QBrush()
        # brush.setColor(QtGui.QColor('green'))
        brush.setColor(QtGui.QColor(
            color['r'], color['g'], color['b']
        ))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.painter.setBrush(brush)
        return
        # if self.color_count == 1:
        #     color_dict = get_random_rgb_color()
        #     # pen = QtGui.QPen()
        #     # pen.setWidth(5)WS
        #     # pen.setColor(QtGui.QColor('blue'))
        #     # painter.setPen(pen)

        #     brush = QtGui.QBrush()
        #     # brush.setColor(QtGui.QColor('green'))
        #     brush.setColor(QtGui.QColor(
        #         color_dict['r'], color_dict['g'], color_dict['b']
        #     ))
        #     brush.setStyle(Qt.BrushStyle.SolidPattern)
        #     self.painter.setBrush(brush)
        #     return
        # # color_of_loops
        # #   1=full random
        # #   2=random theme shapes
        # #   3=random theme color rings
        # #   4=rings of same color
        # #   5=some rings random, some same, some themed random

        # selected_color = get_random_theme_color(self.color_theme)

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

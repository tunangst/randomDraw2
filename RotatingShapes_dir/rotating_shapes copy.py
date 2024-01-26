# solid colors with stroke after
# solid colors, no stroke, blending mode


from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color
from Mandala_dir.Mandala import Mandala
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QTransform
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem
import sys
import math
from pprint import pprint


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
        temp_index = 1
        while temp_index > 0:
            # while self.number_of_replication_circles > 0:
            temp_index -= 1
            circles_index = self.number_of_replication_circles - 1
            shape = self.shape_object_array[circles_index]

            shape['chosen_height'] = 400
            shape['chosen_depth'] = 600
            shape['chosen_angle'] = 36
            shape['chosen_count'] = 10
            print(circles_index)
            print(shape)
            print('depth, canvas y, shape height')
            print(shape['chosen_depth'],
                  self.canvas_center_point[1], shape['chosen_height'])
            # loop over number of shape counts chosen
            # selected_color = None
            if self.is_same_color_loops:
                selected_color = self.get_chosen_loop_color()

            shape_center = get_shape_center_point(
                shape['chosen_width'], shape['chosen_height'])
            shape_transformation_center = (shape_center[0], self.find_y_transformation_to_canvas_center(
                shape['chosen_depth'], shape_center[1]))

            while shape['chosen_count'] > 0:
                # temp_index = 6
                # while temp_index > 0:

                print('shape x center, shape y center: ', shape_center)
                print('shape width, height: ',
                      shape['chosen_width'], shape['chosen_height'])
                # rotation_center = get_shape_center_rotation_point(
                #     shape['chosen_depth'], self.canvas_center_point)
                # build shape at graph origin
                ellipse = QGraphicsEllipseItem(
                    0, 0, shape['chosen_width'], shape['chosen_height'])
                # set center to shape center for initial move

                # self.updateTransform(ellipse, self.canvas_center_point)
                # ellipse.setTransformOriginPoint(
                #     ellipse.boundingRect().center())
                # ellipse.setTransformOriginPoint(
                #     QPointF(shape_center[0], shape_center[1]))
                # move shape to width center at chosen depth
                ellipse.setPos(
                    QPointF(self.canvas_center_point[0] - shape_center[0], shape['chosen_depth'] - shape_center[1]))
                # QPointF(self.canvas_center_point[0] - shape_center[0], shape['chosen_depth'] + shape_center[1]))
                # set transformation point to center based on new shape initialized position
                # ellipse.setTransformOriginPoint(
                #     QPointF(rotation_center[0], rotation_center[1]))
                ellipse.setTransformOriginPoint(
                    shape_transformation_center[0], shape_transformation_center[1])

                ellipse.setRotation(current_degrees)
                current_degrees += shape['chosen_angle']

                if self.is_same_color_loops == False:
                    selected_color = self.get_chosen_loop_color()

                fill = QBrush(QtGui.QColor(
                    selected_color['r'], selected_color['g'], selected_color['b']))
                stroke = QPen(QtGui.QColor(
                    self.color_theme[0]['r'], self.color_theme[0]['g'], self.color_theme[0]['b']))
                stroke.setWidth(shape['chosen_stroke'])

                ellipse.setBrush(fill)
                ellipse.setPen(stroke)
                # fill = QBrush(Qt.GlobalColor.blue)
                # ellipse.setBrush(fill)
                self.graphic_scene.addItem(ellipse)
                # ellipse = None
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
        # return self.rotating_shapes_board

    # def updateTransform(self , target: QGraphicsSvgItem , newValue: Any):

    def find_y_transformation_to_canvas_center(self, shape_depth, shape_center_y):
        cp = self.canvas_center_point[1]
        d = shape_depth
        sh = shape_center_y
        result = cp - (d - sh)
        # if d + sh < cp:
        #     # result = cp - (d + sh)
        #     result = cp - (d - sh)
        # elif d < cp and d+sh > cp:
        #     result = (cp - (d+sh))*-1
        # # elif d < 0 and (d + sh) > 0:
        # #     result = cp - (d+sh)*-1
        # # elif d < 0 and (d+sh) < 0:
        # #     result = cp - (d+sh)
        # else:
        #     print('out of scope in find_y_transformation_to_canvas_center')
        return result

    def updateTransform(self, target: QGraphicsEllipseItem, newValue):
        origin = target.transformOriginPoint()
        transform = QTransform().translate(origin.x(), origin.y())
        # transform.scale(newValue[0], newValue[1])
        transform.translate(-origin.x(), -origin.y())
        target.setTransform(transform)

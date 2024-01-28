from main_utility_functions.utility import (
    get_shape_center_point,
    get_shape_center_rotation_point,
    get_random_theme_color,
    get_random_rgb_color,
    get_chosen_theme_color,
)
from RotatingShapes_dir.RotatingShapesBase import RotatingShapesBase
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter
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
import sys
import math
from pprint import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ class variables ~~~~~~~~~~~~~~~~~~~~
# self.shape_color
# self.canvas
# self.label
# self.painter
# self.current_shape_rotation_angle
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ class variables ~~~~~~~~~~~~~~~~~~~~


class RotatingShapesPainter(RotatingShapesBase):
    def __init__(self):
        super().__init__()
        print("~~~~~ in Rotatingshapes ~~~~~~~~")
        self.shape_color = None

        self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle("Rotating Shapes")
        self.label.show()

    def start(self):
        self.current_shape_rotation_angle = 0

        self.painter = QPainter(self.canvas)
        self.painter.begin(self.canvas)

        self.painter.translate(self.canvas_center_point[0], self.canvas_center_point[1])

        current_loop_number = len(self.design_loop_array) - 1

        # loop over number of rings
        while current_loop_number >= 0:
            self.painter.save()
            print("current loop number", current_loop_number)

            current_loop = self.design_loop_array[current_loop_number]
            print(current_loop["shape_array"][0]["chosen_shape"])
            print(current_loop["shape_array"][0]["chosen_shape_height"])
            print(current_loop["chosen_loop_radius"])
            # build shape fill
            current_shape_number = len(current_loop["shape_array"]) - 1
            blend_mode = current_loop["chosen_loop_blending_mode"]
            blend_mode = "screen"
            self.set_blend_mode(blend_mode)
            if blend_mode == "screen":
                self.canvas.fill(QtGui.QColor("black"))
            while current_shape_number >= 0:
                current_shape = current_loop["shape_array"][current_shape_number]

                # self.set_blend_mode(current_loop["chosen_loop_blending_mode"])

                self.draw_shape(
                    current_shape, current_loop["chosen_loop_radius"], False
                )

                self.current_shape_rotation_angle += current_shape[
                    "chosen_shape_rotation_angle"
                ]
                current_shape_number -= 1
            self.painter.restore()
            # self.painter.save()

            # build shape stroke
            current_shape_number = len(current_loop["shape_array"]) - 1
            self.set_blend_mode(False)
            while current_shape_number >= 0:
                current_shape = current_loop["shape_array"][current_shape_number]

                self.draw_shape(current_shape, current_loop["chosen_loop_radius"], True)

                self.current_shape_rotation_angle += current_shape[
                    "chosen_shape_rotation_angle"
                ]
                current_shape_number -= 1

            current_loop_number -= 1
        self.painter.end()

    def set_blend_mode(self, blendMode):
        match blendMode:
            case "multiply":
                # self.painter.compositionMode_Multiply
                self.painter.setCompositionMode(
                    QPainter.CompositionMode.CompositionMode_Multiply
                )
            case "screen":
                self.painter.setCompositionMode(
                    QPainter.CompositionMode.CompositionMode_Screen
                )
            case _:
                self.painter.setCompositionMode(
                    QPainter.CompositionMode.CompositionMode_SourceOver
                )
                print("out of scope in set_blend_mode")

    def draw_shape(self, shape, loop_radius, stroke=False):
        color = self.use_color(shape)
        if stroke:
            pen = QtGui.QPen()
            pen.setWidth(1)
            pen.setColor(QtGui.QColor("white"))
            self.painter.setPen(pen)
        else:
            brush = QtGui.QBrush()
            brush.setColor(QtGui.QColor(color["r"], color["g"], color["b"]))
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            self.painter.setBrush(brush)

        shape_center = shape["chosen_shape_center"]

        self.painter.save()
        self.painter.rotate(self.current_shape_rotation_angle)
        self.painter.translate(-shape_center[0], shape_center[1] - loop_radius)
        # self.painter.translate(-100, -shape['chosen_depth'])

        self.build_shape_wrapper(shape)
        self.painter.restore()
        # self.painter.drawEllipse(0, 0, 200, 100)
        # self.painter.drawEllipse(
        #     -int(shape['chosen_width']/2), -int(shape['chosen_height']/2), int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        # self.painter.drawEllipse(
        #     0, 0, shape['chosen_width'], shape['chosen_height'])

    def build_shape_wrapper(self, shape):
        # ("line", "ellipse", "circle", "rectangle", "square")
        match shape["chosen_shape"]:
            case "line":
                self.painter.drawLine(
                    0, 0, shape["chosen_shape_width"], shape["chosen_shape_height"]
                )
            case "ellipse" | "circle":
                self.painter.drawEllipse(
                    0, 0, shape["chosen_shape_width"], shape["chosen_shape_height"]
                )
            case "rectangle" | "square":
                self.painter.drawRect(
                    0, 0, shape["chosen_shape_width"], shape["chosen_shape_height"]
                )
            case _:
                print("out of scope in rotating_shapes build_shape_wrapper")

    def use_color(self, shape):
        return_color = shape["chosen_shape_color"]
        # loop_of_random_shape_color = True/False
        # loop_of_random_shape_color = shape['chosen_shape_color']
        # loop_index = shape['chosen_loop_index']
        # color_count 1=full random, 2=dual, 3=tri, 4=quad, 5=cint)
        # theme_type (1=random theme color, 2= cycle theme color)
        # self.theme_type
        self.color_count = 6

        match self.color_count:
            case 1:
                # full random, return random color every time
                return_color = get_random_rgb_color()

            case 2 | 3 | 4 | 5:
                # print('in 2,3,4,5 use_color')
                # not full random
                # is theme_type random or incremental?
                # if random, get_random_theme_color
                # if incremental, get random color
                self.theme_type = 2
                if self.theme_type == 1:
                    # random pull
                    return_color = get_random_theme_color(self.color_theme)
                else:
                    # incremental
                    # print('loop index', loop_index)
                    # color = get_chosen_theme_color(
                    #     self.color_theme, loop_index)
                    # print(color)
                    pass
            case _:
                pass
                # print("out of scope in use_color")
        return return_color
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

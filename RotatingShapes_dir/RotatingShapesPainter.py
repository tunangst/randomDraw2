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
# self.pen
# self.brush
# self.current_shape_rotation_angle
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ class variables ~~~~~~~~~~~~~~~~~~~~


class RotatingShapesPainter(RotatingShapesBase):
    def __init__(self):
        super().__init__()
        print("~~~~~ in Rotatingshapes ~~~~~~~~")
        self.shape_color = None
        self.current_shape_rotation_angle = 0

        self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle("Rotating Shapes")
        self.label.show()

    def start(self):
        self.painter = QPainter(self.canvas)
        self.painter.begin(self.canvas)

        current_loop_number = len(self.design_loop_array) - 1

        # set initial translation (center screen) and save it
        self.painter.translate(self.canvas_center_point[0], self.canvas_center_point[1])
        # self.painter.save()

        # loop over number of rings
        while current_loop_number >= 0:
            print("current loop number", current_loop_number)

            current_loop = self.design_loop_array[current_loop_number]
            print("shape count", current_loop["chosen_shape_count"])

            # print(current_loop["shape_array"][0]["chosen_shape"])
            # print(current_loop["shape_array"][0]["chosen_shape_height"])
            # print(current_loop["chosen_loop_radius"])
            # print(current_loop)

            # build shape fill
            current_shape_number = len(current_loop["shape_array"]) - 1
            # blend_mode = current_loop["chosen_loop_blending_mode"]
            # blend_mode = "screen"
            # self.set_blend_mode(blend_mode)
            # if blend_mode == "screen":
            #     self.canvas.fill(QtGui.QColor("black"))

            # translate the grid based on loop dimentions
            # self.painter.translate(0, current_loop["chosen_loop_radius"])
            # self.painter.rotate(current_loop["chosen_rotation_angle"])

            # self.painter.translate(0, current_loop["chosen_loop_radius"])
            self.painter.save()
            # reset the saved rotation angle (if not the first pass)
            self.current_shape_rotation_angle = 0
            # loop over the shape radius
            while current_shape_number >= 0:
                current_shape = current_loop["shape_array"][current_shape_number]

                # translate the grid based on loop radius, shape size, rotation
                widthInput = -current_shape["chosen_shape_width"] / 2
                heightInput = current_shape["chosen_shape_height"] / 2

                # self.painter.translate(0, current_loop["chosen_loop_radius"])

                # self.painter.translate(widthInput, heightInput)
                self.painter.save()
                self.painter.rotate(self.current_shape_rotation_angle)

                self.setBlendMode(current_shape)
                self.defineStrokeFill(current_shape)

                self.drawShape(current_shape, current_loop["chosen_loop_radius"])

                # add to rotation angle for next shape
                self.current_shape_rotation_angle += current_shape[
                    "chosen_shape_rotation_angle"
                ]
                # increment shape loop
                self.painter.restore()
                current_shape_number -= 1

            # self.painter.save()

            # build shape stroke
            # current_shape_number = len(current_loop["shape_array"]) - 1
            # self.setBlendMode(False)
            # while current_shape_number >= 0:
            #     current_shape = current_loop["shape_array"][current_shape_number]

            #     self.defineStrokeFill(
            #         current_shape, current_loop["chosen_loop_radius"], True
            #     )

            #     self.current_shape_rotation_angle += current_shape[
            #         "chosen_shape_rotation_angle"
            #     ]
            #     current_shape_number -= 1

            self.painter.restore()
            current_loop_number -= 1
        # self.painter.restore()
        self.painter.end()

    def setBlendMode(self, shape):
        blendMode = shape["chosen_shape_blending_mode"]
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

    def defineStrokeFill(self, shape, stroke=False):
        color = self.use_color(shape)
        if stroke:
            self.pen = QtGui.QPen()
            self.pen.setWidth(1)
            self.pen.setColor(QtGui.QColor("white"))
            self.painter.setPen(self.pen)
        else:
            self.brush = QtGui.QBrush()
            self.brush.setColor(QtGui.QColor(color["r"], color["g"], color["b"]))
            self.brush.setStyle(Qt.BrushStyle.SolidPattern)
            self.painter.setBrush(self.brush)

        # shape_center = shape["chosen_shape_center"]

        # self.painter.save()
        # self.painter.rotate(self.current_shape_rotation_angle)
        # self.painter.translate(-shape_center[0], shape_center[1] - loop_radius)

        # self.build_shape_wrapper(shape)
        # self.painter.drawEllipse(0, 0, 200, 100)
        # self.painter.drawEllipse(
        #     -int(shape['chosen_width']/2), -int(shape['chosen_height']/2), int(shape['chosen_width']/2), int(shape['chosen_height']/2))
        # self.painter.drawEllipse(
        #     0, 0, shape['chosen_width'], shape['chosen_height'])

    def drawShape(self, shape, loopRadius):
        # ("line", "ellipse", "circle", "rectangle", "square")
        xStartValue = int(-shape["chosen_shape_width"] / 2)
        yStartValue = int(loopRadius - shape["chosen_shape_height"] / 2)
        xEndValue = int(shape["chosen_shape_width"] / 2)
        yEndValue = int(loopRadius + shape["chosen_shape_height"] / 2)
        match shape["chosen_shape"]:
            case "line":
                self.painter.drawLine(xStartValue, yStartValue, xEndValue, yEndValue)
            case "ellipse" | "circle":
                self.painter.drawEllipse(xStartValue, yStartValue, xEndValue, yEndValue)
            case "rectangle" | "square":
                self.painter.drawRect(xStartValue, yStartValue, xEndValue, yEndValue)
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

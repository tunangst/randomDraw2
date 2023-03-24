from main_utility_functions import utility

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem
import sys
import math


DEFAULT_DESIGN = 'square'
# CONTROL_SIZE = DEFAULT_WIDTH if DEFAULT_WIDTH > DEFAULT_HEIGHT else DEFAULT_HEIGHT
# DEFAULT_COUNT = utility.find_closest_box_count(
#     CONTROL_SIZE, 100)
# WIDTH = math.floor(CONTROL_SIZE/DEFAULT_COUNT)
# HEIGHT = WIDTH
# print(DEFAULT_COUNT)


class Mosaic_style():
    def __init__(self, cwidth, cheight):
        super().__init__()
        print('~~~~~ in Mosaic_style ~~~~~~~~')
        self.random_color = False
        self.control_size = cwidth if cwidth > cheight else cheight
        # will default to 80 on default sizes
        self.shape_count = utility.get_closest_box_count(
            self.control_size, 100)
        # only currently for square
        self.shape_width = math.floor(self.control_size/self.shape_count)
        # only currently for square
        self.shape_height = self.shape_width

        print(self.shape_width, self.shape_height)
        self.canvas_width = cwidth
        self.canvas_height = cheight

        self.app = QApplication(sys.argv)
        self.scene = QGraphicsScene(0, 0,
                                    self.canvas_width, self.canvas_height)

        # self.label = QtWidgets.QLabel()
        # self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        # self.canvas.fill(Qt.GlobalColor.black)
        # self.label.setPixmap(self.canvas)
        # self.setCentralWidget(self.label)

    def squares(self):
        cur_x_coord = 0
        cur_y_coord = 0
        while cur_y_coord < self.canvas_height:
            rect = QGraphicsRectItem(
                cur_x_coord, cur_y_coord, self.shape_width, self.shape_height)
            # rect.setPos(cur_x_coord, cur_y_coord)
            # fill
            fill = QBrush(Qt.GlobalColor.blue)
            rect.setBrush(fill)
            # border
            border = QPen(Qt.GlobalColor.lightGray)
            border.setWidth(3)
            rect.setPen(border)
            # add to scene
            self.scene.addItem(rect)

            # loop over x and y length based on shape size
            cur_x_coord += self.shape_width
            if cur_x_coord > self.canvas_width:
                cur_x_coord = 0
                cur_y_coord += self.shape_height

        # show the scene
        view = QGraphicsView(self.scene)
        view.show()
        # keep the scene open
        self.app.exec()


# If we don't set this on creation, we can set it later with .setSceneRect


# app = QtWidgets.QApplication(sys.argv)
# window = Main_Window()
# window.show()
# window.squares()
# app.exec()

# print(2560 % 100)
# print(100 + 2560 % 100)
# print(100 - 2560 % 100)
# print(2560 / 64)

# loop runs an increment starting at 0 and runs to half of the suggested count.
# each increment it will check if width/count+increment and width/count-increment is 0 to see which is closer


# print(find_closest_box_count(2560, 100))
# print(2560 % 80)
# print(2560 / 80)

# print(DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_DESIGN,
#   CONTROL_SIZE, DEFAULT_COUNT, WIDTH, HEIGHT)

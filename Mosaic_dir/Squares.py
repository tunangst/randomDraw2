from main_utility_functions import utility

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem
import sys
import math


# DEFAULT_DESIGN = 'square'
# CONTROL_SIZE = DEFAULT_WIDTH if DEFAULT_WIDTH > DEFAULT_HEIGHT else DEFAULT_HEIGHT
# DEFAULT_COUNT = utility.find_closest_box_count(
#     CONTROL_SIZE, 100)

# class variables
# canvas_width
# canvas_height
# control_size ????
# shape_size
# shape_count
# scene
# app
# fill


class Square(QGraphicsView):
    def __init__(self, cwidth, cheight, size, count, color_theme):
        super().__init__()
        print('~~~~~ in Square_style ~~~~~~~~')
        # print(locals())
        self.canvas_width = cwidth
        self.canvas_height = cheight
        self.shape_size = size
        self.shape_count = count
        self.color_theme = color_theme
        # self.scene = scene
        self.squares_board = None

        self.graphic_scene = QGraphicsScene(
            0, 0, self.canvas_width, self.canvas_height)
        self.start()

    def start(self):
        print('starting Square build')
        self.squares()

    def squares(self):
        cur_x_coord = 0
        cur_y_coord = 0
        selected_color = None
        while cur_y_coord < self.canvas_height:
            rect = QGraphicsRectItem(
                cur_x_coord, cur_y_coord, self.shape_size, self.shape_size)
            # rect.setPos(cur_x_coord, cur_y_coord)
            # fill
            selected_color = utility.get_random_theme_color(self.color_theme)
            # print('selected color ', selected_color)
            # NEED TO SET RGB IN DICTIONARY MODE
            fill = QBrush(QtGui.QColor(
                selected_color['r'], selected_color['g'], selected_color['b']))
            rect.setBrush(fill)
            # border is the background color or first in array
            border = QPen(QtGui.QColor(
                self.color_theme[0]['r'], self.color_theme[0]['g'], self.color_theme[0]['b']))
            border.setWidth(3)
            rect.setPen(border)
            # add to scene
            self.graphic_scene.addItem(rect)

            # loop over x and y length based on shape size
            cur_x_coord += self.shape_size
            if cur_x_coord > self.canvas_width:
                cur_x_coord = 0
                cur_y_coord += self.shape_size

        # show the scene
        self.squares_board = QGraphicsView(self.graphic_scene)
        # self.squares_board.show()
        return self.squares_board
        # return squares
        # keep the scene open
        # self.app.exec()


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

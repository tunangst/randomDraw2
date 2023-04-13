from main_utility_functions import utility
from randomDraw2 import randomDraw2
# from .Squares import Square
from pprint import pprint

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QApplication,
    QGraphicsRectItem,
    QWidget
)
import sys
import math

DEFAULT_COUNT = 100
# class variables
# canvas_width
# canvas_height
# control_size
# design
# shape_count
# shape_width
# shape_height
# app
# scene


class Mosaic(randomDraw2):
    def __init__(self):
        super().__init__()
        print("~~~~~ in Mosaic_style ~~~~~~~~")
        self.control_size = self.canvas_width if self.canvas_width > self.canvas_height else self.canvas_height
        # will default to 80 on default sizes
        self.shape_count = utility.get_closest_box_count(
            self.control_size, 100
        )
        # only currently for square
        self.shape_width = math.floor(self.control_size / self.shape_count)
        # only currently for square
        self.shape_height = self.shape_width

        # self.squares_painting = None

        # self.app = QApplication(sys.argv)
        # self.graphic_scene = QGraphicsScene(
        #     0, 0, self.canvas_width, self.canvas_height)

        # self.start()

    def start(self):
        # if self.design == 2:
        #     self.squares_painting = Square(
        #         self.canvas_width,
        #         self.canvas_height,
        #         self.shape_width,
        #         self.shape_count,
        #         self.color_theme
        #     )
        print('Mosaic vars for square')
        # pprint(vars(self.squares_painting))
        # pprint(vars(squares_painting.squares_view))
        # print('~~~~~~squares painting')
        # pprint(squares_painting.squares_view)
        # print('~~~~~~view')
        # return self.squares_painting

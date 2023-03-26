from main_utility_functions import utility
from .Squares import Square

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem
import sys
import math


DEFAULT_DESIGN = 'square'

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


class Mosaic():
    def __init__(self, cwidth, cheight, design, color_theme):
        super().__init__()
        print('~~~~~ in Mosaic_style ~~~~~~~~')
        self.canvas_width = cwidth
        self.canvas_height = cheight
        self.control_size = cwidth if cwidth > cheight else cheight
        self.design = design
        self.color_theme = color_theme
        # will default to 80 on default sizes
        self.shape_count = utility.get_closest_box_count(
            self.control_size, 100)
        # only currently for square
        self.shape_width = math.floor(self.control_size/self.shape_count)
        # only currently for square
        self.shape_height = self.shape_width

        self.app = QApplication(sys.argv)
        self.scene = QGraphicsScene(0, 0,
                                    self.canvas_width, self.canvas_height)
        
        if(self.design == 2): 
            self.start()

    def start(self):
        if(self.design == 2):
            Square(self.canvas_width, self.canvas_height, self.shape_width, self.shape_count, self.color_theme, self.scene, self.app)

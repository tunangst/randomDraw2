from Mosaic_dir.Mosaic import Mosaic
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color, get_random_rgb_color, get_chosen_theme_color
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem, QWidget, QLabel, QVBoxLayout
import sys
import math
from pprint import pprint


class ReflectingTiles(Mosaic):
    def __init__(self):
        super().__init__()
        print('~~~~~ in ReflectingTiles ~~~~~~~~')
        self.shape_color = None

        self.max_number_of_horizontal_tiles = 10
        self.min_number_of_horizontal_tiles = 1

        self.max_number_of_veritcal_tiles = 10
        self.min_number_of_vertical_tiles = 1

        self.max_number_of_horizontal_boxes = 10
        self.min_number_of_horizontal_boxes = 2

        self.max_number_of_veritical_boxes = 10
        self.min_number_of_vertical_boxes = 2

        self.number_of_horizontal_tiles = 2
        self.number_of_vertical_tiles = 2
        self.number_of_horizontal_boxes = 4
        self.number_of_veritical_boxes = 2

        # if self.number_of_horizontal_boxes == self.number_of_veritical_boxes
        #   eligible for rotation method
        #   patterns: random, clone, reflect, {rotate}

        self.tile_width = self.canvas_width / self.number_of_horizontal_tiles
        self.tile_height = self.canvas_height / self.number_of_vertical_tiles
        self.box_width = self.tile_width / self.number_of_horizontal_tiles
        self.box_height = self.tile_height / self.number_of_vertical_tiles

        self.tile_x_start_position = 0
        self.tile_y_start_position = 0

        self.tiles_left = self.number_of_horizontal_tiles * self.number_of_vertical_tiles

        self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        self.canvas.fill(QtGui.QColor("white"))
        self.tile_canvas = QtGui.QPixmap(self.tile_width, self.tile_height)
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle('Reflecting Tiles')
        self.label.show()

    def start(self):
        # start at 0,0
        # create pattern
        #   loop self.tiles_left

        self.tile_pattern = QPainter(self.tile_canvas)
        self.tile_pattern.begin(self.tile_canvas)

        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('blue'))
        self.tile_pattern.setPen(pen)

        self.tile_pattern.drawRect(
            0, 0, 10, 10)
        self.draw_template()
        self.tile_pattern.end()

        self.painter = QPainter(self.canvas)
        self.painter.begin(self.canvas)

        # self.painter.translate(
        #     self.canvas_center_point[0], self.canvas_center_point[1])

        # loop over number of rings
        # while current_loop_number >= 0:
        #     self.painter.save()

        #     while current_shape_number >= 0:

        #         self.draw_color(current_shape)
        #         self.draw_shape(
        #             current_shape, current_loop['chosen_loop_radius'])

        #         current_shape_number -= 1
        #     self.painter.restore()
        #     current_loop_number -= 1
        self.painter.end()

    def draw_template(self):
        y = self.number_of_vertical_tiles
        x = self.number_of_horizontal_tiles
        box_matrix = []

        starting_x = 0
        starting_y = 0
        ending_x = self.box_width
        ending_y = self.box_height
        while y > 0:
            row_array = []
            starting_x = 0

            while x > 0:
                box = {}
                box['color'] = 'green'
                box['starting_x'] = starting_x
                box['starting_y'] = starting_y
                box['ending_x'] = ending_x
                box['ending_y'] = ending_y

                starting_x += self.box_width
                row_array.append(box)
                x -= 1
            box_matrix.append(row_array)
            starting_y += self.box_height
            ending_y += self.box_height
            y -= 1
        pprint(box_matrix)


# test = ReflectingTiles()

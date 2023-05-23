from Mosaic_dir.Mosaic import Mosaic
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color, get_random_rgb_color, get_chosen_theme_color
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem, QWidget, QLabel, QVBoxLayout
import sys
import math
from pprint import pprint


class ReflectingTiles():
    def __init__(self):
        super().__init__()
        self.canvas_width = 40
        self.canvas_height = 40
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
        self.number_of_horizontal_boxes = 2
        self.number_of_vertical_boxes = 2
        # don't let boxes exceed width/height
        # don't let tiles exceed self.canvas_width/height/2

        # if self.number_of_horizontal_boxes == self.number_of_veritical_boxes
        #   eligible for rotation method
        #   patterns: random, clone, reflect, {rotate}

        self.tile_width = self.canvas_width / self.number_of_horizontal_tiles
        self.tile_height = self.canvas_height / self.number_of_vertical_tiles
        self.box_width = self.tile_width / self.number_of_horizontal_tiles
        self.box_height = self.tile_height / self.number_of_vertical_tiles
        # print(self.tile_width, self.tile_height,
        #       self.box_width, self.box_height)

        self.tile_x_start_position = 0
        self.tile_y_start_position = 0

        self.tiles_left = self.number_of_horizontal_tiles * self.number_of_vertical_tiles

        # self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        # self.canvas.fill(QtGui.QColor("white"))
        # self.tile_canvas = QtGui.QPixmap(self.tile_width, self.tile_height)
        self.start()

        # self.label = QLabel()
        # self.label.setPixmap(self.canvas)
        # self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        # self.label.setWindowTitle('Reflecting Tiles')
        # self.label.show()

    def start(self):
        # start at 0,0
        # create pattern
        #   loop self.tiles_left

        # self.tile_pattern = QPainter(self.tile_canvas)
        # self.tile_pattern.begin(self.tile_canvas)

        # pen = QtGui.QPen()
        # pen.setWidth(5)
        # pen.setColor(QtGui.QColor('blue'))
        # self.tile_pattern.setPen(pen)

        # self.tile_pattern.drawRect(
        #     0, 0, 10, 10)
        self.draw_template()
        # self.tile_pattern.end()

        # self.painter = QPainter(self.canvas)
        # self.painter.begin(self.canvas)

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
        # self.painter.end()

    def draw_template(self):
        tile_x = self.number_of_horizontal_tiles
        tile_y = self.number_of_vertical_tiles
        tile_index = 0

        tile_matrix = []

        starting_tile_x_pos = 0
        starting_tile_y_pos = 0
        ending_tile_x_pos = self.tile_width
        ending_tile_y_pos = self.tile_height
        while tile_y > 0:
            tile_x = self.number_of_horizontal_tiles
            starting_tile_x_pos = 0
            ending_tile_x_pos = self.tile_width
            tile_x_array = []
            while tile_x > 0:
                starting_tuple = (starting_tile_x_pos, starting_tile_y_pos)
                ending_tuple = (ending_tile_x_pos, ending_tile_y_pos)
                print(starting_tuple)
                print(ending_tuple)
                tile_object = self.build_tile(
                    tile_index, starting_tuple, ending_tuple)
                starting_tile_x_pos += self.tile_width
                ending_tile_x_pos += self.tile_width if ending_tile_x_pos <= self.canvas_width else 0
                tile_x_array.append(tile_object)
                tile_index += 1
                tile_x -= 1

            tile_matrix.append(tile_x_array)
            starting_tile_y_pos += self.tile_height
            ending_tile_y_pos += self.tile_height
            tile_y -= 1

        pprint(tile_matrix)

    def build_tile(self, index, start, end):
        box_x = self.number_of_horizontal_boxes
        box_y = self.number_of_vertical_boxes

        start_x = start[0]
        start_y = start[1]
        end_x = start_x + self.box_width
        end_y = start_y + self.box_height

        tile_obj = {}
        tile_obj['index'] = index
        tile_obj['box_matrix'] = []

        while box_y > 0:
            box_x = self.number_of_horizontal_boxes
            start_x = start[0]
            end_x = start_x + self.box_width
            row_array = []
            while box_x > 0:
                box = {}
                box['color'] = 'green'
                box['start_x'] = start_x
                box['start_y'] = start_y
                box['end_x'] = end_x
                box['end_y'] = end_y
                print(start_x, start_y)
                print(end_x, end_y)

                start_x += self.box_width
                end_x += self.box_width if end_x <= end[0] else 0
                row_array.append(box)

                box_x -= 1
            tile_obj['box_matrix'].append(row_array)
            start_y += self.box_height
            end_y += self.box_height
            box_y -= 1
        return tile_obj


test = ReflectingTiles()

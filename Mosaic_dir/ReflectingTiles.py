from Mosaic_dir.Mosaic import Mosaic
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from main_utility_functions.utility import get_shape_center_point, get_shape_center_rotation_point, get_random_theme_color, get_random_rgb_color, get_random_color_theme, get_chosen_theme_color, get_random
from PyQt6.QtGui import QBrush, QPen, QTransform, QPainter
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem, QGraphicsRotation, QGraphicsEllipseItem, QWidget, QLabel, QVBoxLayout
import sys
import math
import random
from copy import copy, deepcopy
from pprint import pprint


class ReflectingTiles(Mosaic):
    def __init__(self):
        super().__init__()
        # self.canvas_width = 40
        # self.canvas_height = 40
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
        self.number_of_horizontal_boxes = 5
        self.number_of_vertical_boxes = 5
        # don't let boxes exceed width/height
        # don't let tiles exceed self.canvas_width/height/2

        # if self.number_of_horizontal_boxes == self.number_of_veritical_boxes
        #   eligible for rotation method
        #   patterns: random, clone, reflect, {rotate}

        self.tile_width = self.canvas_width / self.number_of_horizontal_tiles
        self.tile_height = self.canvas_height / self.number_of_vertical_tiles
        self.box_width = self.tile_width / self.number_of_horizontal_boxes
        self.box_height = self.tile_height / self.number_of_vertical_boxes
        # print(self.tile_width, self.tile_height,
        #       self.box_width, self.box_height)

        self.tile_x_start_position = 0
        self.tile_y_start_position = 0

        self.tiles_left = self.number_of_horizontal_tiles * self.number_of_vertical_tiles

        self.canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        self.canvas.fill(QtGui.QColor("white"))
        self.start()

        self.label = QLabel()
        self.label.setPixmap(self.canvas)
        self.label.setGeometry(0, 0, self.canvas_width, self.canvas_height)
        self.label.setWindowTitle('Reflecting Tiles')
        self.label.show()

    def start(self):
        self.tile_matrix = self.draw_template()
        # pprint(tile_matrix[0][0])
        template_tile = self.tile_matrix[0][0]['box_matrix']
        self.color_template = self.color_template(template_tile)
        print(self.color_template)
        self.set_tile_colors()
        # start at 0,0
        # create pattern
        #   loop self.tiles_left

        self.painter = QPainter(self.canvas)

        stroke = QtGui.QPen()
        stroke.setWidth(3)
        stroke.setColor(QtGui.QColor('white'))
        self.painter.setPen(stroke)

        self.painter.begin(self.canvas)
        self.draw_tiles()
        self.painter.end()

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
                # print(starting_tuple)
                # print(ending_tuple)
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

        # pprint(tile_matrix)
        return tile_matrix

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
                box['start_x'] = int(start_x)
                box['start_y'] = int(start_y)
                box['end_x'] = int(end_x)
                box['end_y'] = int(end_y)
                # print(start_x, start_y)
                # print(end_x, end_y)

                start_x += self.box_width
                end_x += self.box_width if end_x <= end[0] else 0
                row_array.append(box)

                box_x -= 1
            tile_obj['box_matrix'].append(row_array)
            start_y += self.box_height
            end_y += self.box_height
            box_y -= 1
        return tile_obj

    def color_template(self, tile_matrix):
        self.color_count = 5
        self.color_theme = get_random_color_theme(
            2, self.color_count
        )
        chosen_colors = get_colors_array(
            self.color_count, self.color_theme)
        template = deepcopy(tile_matrix)
        for y in template:
            for x in y:
                del x['start_x']
                del x['start_y']
                del x['end_x']
                del x['end_y']

                # self.color_count
                # random_color_count (2=dual, 3=tri, 4=quad, 5=penta, 6=all random)
                # self.color_theme
                # hardcoding this until I fix it in randomDraw module

                x['color'] = random.choice(chosen_colors)
                print(x)
        return template

    def set_tile_colors(self):
        # self.color_template
        # self.tile_matrix
        design_type = 'clone'
        submit_design = design_type
        temp_pattern = {}
        # design_type:
        #   clone,
        #   ref_ver, ref_hor, ref_all,
        #   rot_row_(r/l), rot_col_(r/l), rot_row_(r/l)_rot_col_(r/l),
        #   rot_(r/l)_ref_(r/l), ref_(r/l)_rot_(r/l) [first is even, second is odd]

        for tile_idx_y, tiles_y in enumerate(self.tile_matrix):
            print(tile_idx_y)
            # set 0,0 value
            temp_pattern = deepcopy(self.color_template)
            for tile_idx_x, tiles_x in enumerate(tiles_y):
                print(tile_idx_x)
                tile_number = tiles_x['index']

                # new tile, find what design type to use, all clone in this case
                for box_idx_y, tile_y in enumerate(tiles_x['box_matrix']):

                    for box_idx_x, box in enumerate(tile_y):
                        # currently just clones the pattern for each box, need to decide how to split them up to look reflected
                        # print(self.color_design('clone', box_idx_y, box_idx_x))
                        # print(self.color_design(
                        #     'clone', box_idx_y, box_idx_x))

                        if tile_idx_y == 0 and tile_idx_x == 0:
                            # 0,0 is always a clone
                            submit_design = 'clone'
                        else:
                            match design_type:
                                case 'clone':
                                    submit_design = 'clone'
                                case 'ref_ver':
                                    # if x even: clone
                                    # if x odd: reflect_vertical
                                    if tile_idx_x % 2 == 0:
                                        submit_design = 'clone'
                                    else:
                                        submit_design = 'reflect_vertical'
                                case 'ref_hor':
                                    # if y even: clone
                                    # if y odd: reflect_horizontal
                                    if tile_idx_y % 2 == 0:
                                        submit_design = 'clone'
                                    else:
                                        submit_design = 'reflect_horizontal'
                                case 'ref_all':
                                    # if y even:
                                    #   if x even: clone
                                    #   if x odd: reflect_vertical
                                    # if y odd:
                                    #   if x even: reflect_horizontal
                                    #   if x odd: reflect_vertical, reflect_horizontal
                                    if is_even(tile_idx_y):
                                        if is_even(tile_idx_x):
                                            submit_design = 'clone'
                                        else:
                                            submit_design = 'reflect_vertical'
                                    else:
                                        if is_even(tile_idx_x):
                                            submit_design = 'reflect_horizontal'
                                        else:
                                            submit_design = 'reflect_vertical'
                                            temp_pattern = self.color_design(
                                                temp_pattern, submit_design, box_idx_y, box_idx_x, tile_idx_y, tile_idx_x)
                                            submit_design = 'reflect_horizontal'

                                    pass
                                case 'rot_row_r':
                                    # if x = 0: clone
                                    # rotate right index times
                                    submit_design = 'rotate_right'
                                    rot_count = get_pattern_transform_count(
                                        tile_idx_x)
                                    while rot_count > 0:
                                        temp_pattern = self.color_design(
                                            temp_pattern, submit_design, box_idx_y, box_idx_x, tile_idx_y, tile_idx_x)
                                        rot_count -= 1

                                case 'rot_row_l':
                                    # if x = 0: clone
                                    # rotate left index times
                                    submit_design = 'rotate_left'
                                    rot_count = get_pattern_transform_count(
                                        tile_idx_x)
                                    while rot_count > 0:
                                        temp_pattern = self.color_design(
                                            temp_pattern, submit_design, box_idx_y, box_idx_x, tile_idx_y, tile_idx_x)
                                        rot_count -= 1

                                case 'rot_col_r':
                                    pass
                                case 'rot_col_l':
                                    pass
                                case 'rot_row_r_rot_col_r':
                                    pass
                                case 'rot_row_r_rot_col_l':
                                    pass
                                case 'rot_row_l_rot_col_r':
                                    pass
                                case 'rot_row_l_rot_col_l':
                                    pass
                                case 'rot_r_ref_r':
                                    pass
                                case 'rot_r_ref_l':
                                    pass
                                case 'ref_l_rot_r':
                                    pass
                                case 'ref_l_rot_l':
                                    pass
                                case _:
                                    pass

                        box['color'] = self.color_design(
                            temp_pattern, box_idx_y, box_idx_x, tile_idx_y, tile_idx_x)

    def color_design(self, pattern, design, box_y, box_x, tile_y, tile_x):
        # design_type:
        #   clone,
        #   ref_ver, ref_hor, ref_all,
        #   rot_row_(r/l), rot_col_(r/l), rot_row_(r/l)_rot_col_(r/l),
        #   rot_(r/l)_ref_(r/l), ref_(r/l)_rot_(r/l) [first is even, second is odd]

        color_template_clone = deepcopy(pattern)
        color_result = None
        transform_x = None
        transform_y = None
        match design:
            case 'clone':
                transform_y = box_y
                transform_x = box_x
            case 'reflect_horizontal':
                transform_y = box_y
                transform_x = self.number_of_horizontal_boxes - 1 - box_x
                # transform_x = (len(x)-1)-x
            case 'reflect_vertical':
                # transform_y = (len(y)-1)-y
                transform_y = self.number_of_vertical_boxes - 1 - box_y
                transform_x = box_x
            case 'rotate_right':
                transform_y = box_x
                transform_x = self.number_of_horizontal_boxes - 1 - box_y
                # transform_x = (len(x)-1)-y
            case 'rotate_left':
                # transform_y = (len(y)-1)-x
                transform_y = self.number_of_vertical_boxes - 1 - box_x
                transform_x = box_y
            case _:
                print('out of scope in color_design in reflecting tiles')
        color_result = color_template_clone[transform_y][transform_x]['color']
        return color_result

    def draw_tiles(self):
        for tiles_y in self.tile_matrix:
            for tiles_x in tiles_y:
                tile_number = tiles_x['index']
                # new tile, find what design type to use, all clone in this case
                for idx_y, tile_y in enumerate(tiles_x['box_matrix']):
                    for idx_x, box in enumerate(tile_y):
                        print(idx_y, idx_x)
                        color = box['color']
                        r = color['r']
                        g = color['g']
                        b = color['b']
                        # print(self.color_template[idx_y][idx_x]['color'])
                        pprint(box)
                        brush = QtGui.QBrush()
                        brush.setColor(QtGui.QColor(r, g, b))
                        brush.setStyle(Qt.BrushStyle.SolidPattern)
                        self.painter.setBrush(brush)
                        self.painter.drawRect(
                            box['start_x'], box['start_y'], box['end_x'], box['end_y'])


def get_colors_array(count, theme):
    color_index_array = build_color_index_array(count)
    selected_colors = []
    while count > 0:
        roll = get_random(count - 1, 0)
        # get index of roll in array and remove from array
        chosen_color = color_index_array.pop(roll)
        # set color with index
        selected_colors.append(theme[chosen_color])
        count -= 1
    return selected_colors


def build_color_index_array(count):
    index_array = []
    count_index = count - 1
    while count_index >= 0:
        index_array.insert(0, count_index)
        count_index -= 1
    return index_array


def get_pattern_transform_count(idx):
    choice = idx / 4
    returned_choice = 0
    match choice:
        case 0:
            returned_choice = 0
        case .25:
            returned_choice = 1
        case .50:
            return_choice = 2
        case .75:
            return_choice = 3
    return returned_choice


def is_even(num):
    calc = num % 2
    answer = None
    if calc == 0:
        answer = True
    else:
        answer = False
    return answer

# test = ReflectingTiles()

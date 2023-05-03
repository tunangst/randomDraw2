from main_utility_functions.utility import get_random, get_shape_rotation_angle, get_random_theme_color, get_shape_center_point
from randomDraw2 import randomDraw2
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsRectItem
import sys
import math


class Mandala(randomDraw2):
    def __init__(self):
        super().__init__()
        print('~~~~~ in Mandala ~~~~~~~~')
        self.canvas_center_point = (self.canvas_width/2, self.canvas_height/2)
        self.focus_radius = self.canvas_center_point[
            0] if self.canvas_width > self.canvas_height else self.canvas_center_point[0]
        # between half of largest width and center point of height
        self.mandala_type = 'rotating_shapes'
        self.max_shape_count = self.focus_radius/2
        self.min_shape_count = 4
        self.max_shape_width = self.focus_radius
        self.min_shape_width = 10
        self.max_shape_height = self.focus_radius
        self.min_shape_height = 10
        # color_of_loops 1=full random 2=single color rings 3=rings of same color 4=some rings random, some same, some themed random
        # random_color_shapes 1=All random shape colors, 2.Random random shape colors, 3.Every other random shape colors, 4. No random shape colors
        # 1 will need to get new color every shape build, shape loops object to populate true for having random shape colors
        # 2 will need to add in the shape loops object to see if that will get populated with true or false value for random shape colors
        # 3 will need shape loops function to %2=0 to see if populating true or false
        # 4 will need shape loops to all be false for random shape color
        self.random_color_shapes = 1
        self.color_of_loops = 1
        # self.loop_color = None

        self.max_stroke = 3
        self.min_stroke = 0

        self.shape_object_array = []
        self.number_of_replication_circles = get_random(10, 3)

        # self.get_loop_array_counts()

        # design
        # self.design_loop_array = []
        # self.design_full_random_colors = True

        # loop
        self.loop_shape_array = []
        self.shape_count = None
        self.loop_radius = self.get_chosen_loop_radius()
        self.loop_blending_mode = None
        # self.loop_random_or_themed
        # loop_color_set (All Random, Random Random, Every Other Random, All Same, Random Theme, Incremental Theme)
        self.loop_color_set = "All Random"
        # loop_shape_set (All Random, Random Random, Every Other Random, All Same, Incremental)
        self.loop_shape_set = "All Random"
        # offset (-10, 10)
        self.shape_width_offset = 0
        self.shape_height_offset = 0
        self.shape_color_r_offset = 0
        self.shape_color_g_offset = 0
        self.shape_color_b_offset = 0

        # shape
        self.shape = None
        self.shape_width = None
        self.shape_height = None
        self.shape_color = None

        self.build_design()

    def build_design(self):
        self.design_loop_array = []
        self.loop_count = self.get_chosen_loop_count()
        print('loop count', self.loop_count)

        self.design_full_random_colors = True

        if self.design_full_random_colors:
            self.design_loop_array = self.build_loop(self.loop_count, True)
        else:
            self.design_loop_array = self.build_loop(self.loop_count)

    def build_loop(self, loop_count, all_random_colors=False):
        self.loop_shape_array = []

        while loop_count > 0:
            print(loop_count)
            loop_object = {}
            loop_object['chosen_loop_radius'] = self.get_chosen_loop_radius()
            loop_object['chosen_loop_blending_mode'] = self.get_chosen_blending_mode()
            loop_object['chosen_shape_count'] = self.get_chosen_shape_count()
            loop_object['chosen_shape_width_offset'] = self.get_chosen_offset()
            loop_object['chosen_shape_height_offset'] = self.get_chosen_offset()
            loop_object['chosen_shape_color_r_offset'] = self.get_chosen_offset()
            loop_object['chosen_shape_color_g_offset'] = self.get_chosen_offset()
            loop_object['chosen_shape_color_b_offset'] = self.get_chosen_offset()
            loop_object['shape_array'] = None

            if all_random_colors:
                loop_object['shape_array'] = self.build_shape(
                    loop_object['chosen_shape_count'], all_random_colors)
            else:
                loop_object['shape_array'] = self.build_shape(
                    loop_object['chosen_shape_count'])
            self.loop_shape_array.append(loop_object)
            loop_count -= 1
            # print(loop_object)
        # loop array
        print(len(self.loop_shape_array))
        return self.loop_shape_array

    def build_shape(self, shape_count, all_random_color=False):
        shape_array = []
        chosen_shape = self.get_chosen_shape()
        chosen_shape_width = self.get_chosen_dimention(
            self.max_shape_width, self.min_shape_width)
        chosen_shape_height = self.get_chosen_dimention(
            self.max_shape_height, self.min_shape_height)
        chosen_shape_center = get_shape_center_point(
            chosen_shape_width, chosen_shape_height)
        chosen_shape_rotation_angle = get_shape_rotation_angle(shape_count)
        chosen_shape_color = self.get_chosen_color()
        while shape_count > 0:
            shape_object = {}
            shape_object['chosen_shape'] = chosen_shape
            shape_object['chosen_shape_width'] = chosen_shape_width
            shape_object['chosen_shape_height'] = chosen_shape_height
            shape_object['chosen_shape_center'] = chosen_shape_center
            shape_object['chosen_shape_rotation_angle'] = chosen_shape_rotation_angle
            shape_object['chosen_shape_color'] = chosen_shape_color
# define types of color and blending etc
            shape_array.append(shape_object)
            shape_count -= 1
            # print(shape_object)

        return shape_array

# design functions
    def get_chosen_loop_count(self):
        max_shape_count = int(self.focus_radius/250)
        chosen_loop_count = get_random(max_shape_count)
        return chosen_loop_count

# loop functions
    def get_chosen_loop_radius(self):
        # from focus radius max to past origin 1/2 on the other side
        get_depth = get_random(
            self.focus_radius)

        if get_depth > self.canvas_center_point[1]:
            get_depth *= -1
        return get_depth

    def get_chosen_blending_mode(self):
        choice = 'none'
        return choice

    def get_chosen_shape_count(self):
        # self.max_shape_count = self.focus_radius/2
        # self.min_shape_count = 4
        return get_random(
            self.max_shape_count, self.min_shape_count)

# utility functions
    def get_chosen_offset(self):
        return get_random(10, -10)


# shape utility

    def get_chosen_shape(self):
        chosen_shape = None
        if self.mandala_type == 'rotating_shapes':
            chosen_shape = 'ellipse'
        return chosen_shape

    def get_chosen_dimention(self, max, min):
        # self.max_shape_width = self.focus_radius
        # self.min_shape_width = 10
        # self.max_shape_height = self.focus_radius
        # self.min_shape_height = 10
        return get_random(
            max, min)

    def get_chosen_height(self):
        return get_random(
            self.max_shape_height, self.min_shape_height)

    def get_chosen_color(self):
        return get_random_theme_color(self.color_theme)
# build

    def get_design_array_count(self):
        self.design_loop_array = []
        loop_object = {}
        self.design_full_random_colors = True
        if self.design_full_random_colors == True:
            loop_object = self.build_loop(True)
        pass

    def get_loop_array_counts(self):
        num_of_rep_cir = self.number_of_replication_circles
        while num_of_rep_cir > 0:

            # find shape count
            chosen_count = get_random(
                self.max_shape_count, self.min_shape_count)
            # find angle needed to rotate
            chosen_angle = get_shape_rotation_angle(chosen_count)
            # find depth for index
            chosen_depth = self.get_chosen_loop_radius()
            chosen_width = get_random(
                self.max_shape_width, self.min_shape_width)
            chosen_height = get_random(
                self.max_shape_height, self.min_shape_height)
            chosen_stroke = get_random(self.max_stroke, 0)
            # chosen_loop_color = self.get_chosen_loop_color()
            chosen_random_loop_color = self.get_random_loop_color()

            new_loop_obj = {
                'chosen_loop_index': num_of_rep_cir,
                'chosen_count': chosen_count,
                'chosen_angle': chosen_angle,
                'chosen_depth': chosen_depth,
                'chosen_width': chosen_width,
                'chosen_height': chosen_height,
                'chosen_stroke': chosen_stroke,
                'chosen_random_loop_color': chosen_random_loop_color
                # 'chosen_loop_color': chosen_loop_color

            }
            print('loop_obj', new_loop_obj['chosen_random_loop_color'])
            self.shape_object_array.append(new_loop_obj)
            num_of_rep_cir -= 1

    def get_random_loop_color(self):
        # random_color_shapes 1=All random shape colors, 2.Random random shape colors, 3.Every other random shape colors, 4. No random shape colors
        # 1 will need to get new color every shape build, shape loops object to populate true for having random shape colors
        # 2 will need to add in the shape loops object to see if that will get populated with true or false value for random shape colors
        # 3 will need shape loops function to %2=0 to see if populating true or false
        # 4 will need shape loops to all be false for random shape color
        self.random_color_shapes = 2
        match self.random_color_shapes:
            case 1:
                return True
            case 2:
                toggle = get_random(2)
                if (toggle == 1):
                    return True
                else:
                    return False
            case 3:
                toggle = len(self.shape_object_array) % 2
                print(toggle, ' toggle')
                if (toggle == 0):
                    return True
                else:
                    return False
            case 4:
                return False
            case _:
                print('out of scope in get_random_loop_color')
    # def get_chosen_loop_color(self):
    #     return get_random_theme_color(self.color_theme)

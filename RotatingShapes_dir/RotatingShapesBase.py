from main_utility_functions.utility import (
    get_random,
    get_shape_rotation_angle,
    get_random_theme_color,
    get_shape_center_point,
)
from randomDraw2 import randomDraw2
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QApplication,
    QGraphicsRectItem,
)
import sys
import random
import math
from pprint import pprint

# (random, same, incremental)
#   random loop, random shape
#       loop does not store a design
#       shape chooses a new shape each time
#   random loop, same shape
#       loop does not store a design
#       shape stores a random constant shape
#   random loop, incremental shape
#       loop does not store a design
#       shape starts a random shape at the start and chooses the next in line every shape
#   same loop, random shape
#       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape
#   same loop, same shape
#       random shape is chosen on the main loop and loop pushes it to forced shape on shape
#   same loop, incremental shape
#       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
#   incremental loop, random shape
#       will end up all random
#   incremental loop, same shape
#       loop starts at first shape and forces it to shape, each consecutive loop will need to grab the next shape in line
#   incremental loop, incremental shape
#       loop starts at first shape and forces it to shape, build shape will start with that shape then increment the remaining loop its'self
#       next loops start with the next shape in line and do the same to build shape.


class RotatingShapesBase(randomDraw2):
    def __init__(self):
        super().__init__()
        print("~~~~~ in Mandala ~~~~~~~~")
        self.canvas_center_point = (self.canvas_width / 2, self.canvas_height / 2)
        self.focus_radius = (
            self.canvas_center_point[0]
            if self.canvas_width > self.canvas_height
            else self.canvas_center_point[1]
        )
        print(
            self.canvas_center_point,
            self.canvas_center_point[0],
            self.canvas_center_point[1],
        )
        print("^^^^^^^^^^^^^^")
        # between half of largest width and center point of height
        self.mandala_type = "rotating_shapes"
        self.max_loop_count = int(self.focus_radius / 250)
        self.min_loop_count = 1
        self.max_shape_count = self.focus_radius / 2
        self.min_shape_count = 4
        self.max_shape_width = self.focus_radius
        self.min_shape_width = 10
        self.max_shape_height = self.focus_radius
        self.min_shape_height = 10
        self.offset_max = 10
        self.offset_min = -10
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
        self.design_loop_array = []
        # self.shape_object_array = []
        # self.number_of_replication_circles = get_random(10, 3)

        # self.get_loop_array_counts()

        # design
        # self.design_loop_array = []
        # self.design_full_random_colors = True

        # loop
        # self.loop_shape_array = []
        # self.shape_count = None
        # self.loop_radius = self.get_chosen_loop_radius()
        # self.loop_blending_mode = None
        # self.loop_random_or_themed

        # offset (-10, 10)
        # self.shape_width_offset = 0
        # self.shape_height_offset = 0
        # self.shape_color_r_offset = 0
        # self.shape_color_g_offset = 0
        # self.shape_color_b_offset = 0

        # shape
        # self.shape = None
        # self.shape_width = None
        # self.shape_height = None
        # self.shape_color = None

        self.build_design()

    def build_design(self):
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # (random, same, incremental)
        loops_design = get_design(True)
        # loops_design = "incremental"
        # (random, same, incremental)
        shapes_design = get_design(False)
        print(loops_design, shapes_design)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        loop_count = get_loop_count(self.max_loop_count, self.min_loop_count)
        # loop_color_set (All Random, Random Random, Every Other Random, All Same, Random Theme, Incremental Theme)
        self.design_loop_array = self.build_loop(
            loop_count, loops_design, shapes_design
        )

    def build_loop(self, starting_loop_count, loops_design, shapes_design):
        loop_shape_array = []

        # self.loop_shape_pattern_type = self.get_loop_shape_pattern_type(design_loop_shape_pattern_type, loop_count)
        forced_shape = None
        if loops_design == "same" or loops_design == "incremental":
            forced_shape = get_shape_type("random")
        # self.loop_shape_pattern_type = self.get_loop_shape_pattern_type(design_loop_shape_pattern_type, loop_count)
        loop_count = starting_loop_count
        while loop_count > 0:
            loop_count_tuple = (starting_loop_count, loop_count)
            chosen_shape_count = get_shape_count(
                self.max_shape_count, self.min_shape_count
            )
            chosen_shape_count = 10

            loop_object = {}
            loop_object["chosen_loop_radius"] = get_loop_radius(
                self.focus_radius, self.canvas_center_point[1]
            )
            loop_object["chosen_loop_blending_mode"] = get_blending_mode()
            loop_object["chosen_shape_count"] = chosen_shape_count
            # loop_object['chosen_shape_type'] = self.get_chosen_loop_shape_type()
            loop_object["chosen_shape_width_offset"] = get_offset(
                self.offset_max, self.offset_min
            )
            loop_object["chosen_shape_height_offset"] = get_offset(
                self.offset_max, self.offset_min
            )
            loop_object["chosen_shape_color_r_offset"] = get_offset(
                self.offset_max, self.offset_min
            )
            loop_object["chosen_shape_color_g_offset"] = get_offset(
                self.offset_max, self.offset_min
            )
            loop_object["chosen_shape_color_b_offset"] = get_offset(
                self.offset_max, self.offset_min
            )

            match loops_design:
                case "random":
                    #   random loop, random shape
                    #       loop does not store a design
                    #       shape chooses a new shape each time
                    #   random loop, same shape
                    #       loop does not store a design
                    #       shape stores a random constant shape
                    #   random loop, incremental shape
                    #       loop does not store a design
                    #       shape starts a random shape at the start and chooses the next in line every shape
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        None,
                    )
                    pass
                case "same":
                    if loops_design == "same" and shapes_design == "random":
                        forced_shape = get_shape_type("random")
                    #   same loop, random shape
                    #       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape.
                    #       shape is used for entire loop
                    #   same loop, same shape
                    #       random shape is chosen on the main loop and loop pushes it to forced shape on shape, shape uses the same for each shape
                    #       shape is same shape for everything
                    #   same loop, incremental shape
                    #       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
                    #       shape starts at same shape and iterates
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        forced_shape,
                    )
                case "incremental":
                    forced_shape = get_shape_type(
                        "incremental", loop_count_tuple, forced_shape
                    )
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        forced_shape,
                    )
                    pass
                case _:
                    print("out of scope in build loop in Mandala")

            loop_shape_array.append(loop_object)
            loop_count -= 1
            # if all_random_colors:
            #     loop_object['shape_array'] = self.build_shape(
            #         loop_object['chosen_shape_count'], self.design_loop_shape_pattern_type, (starting_loop_count, loop_count), all_random_colors)
            # else:
            #     loop_object['shape_array'] = self.build_shape(
            #         loop_object['chosen_shape_count'], self.design_loop_shape_pattern_type)
            # self.loop_shape_array.append(loop_object)
        # loop array
        return loop_shape_array

    def build_shape(
        self, loop_design, shape_count, shape_design, loop_count_tuple, force_shape=None
    ):
        starting_shape_count = shape_count
        chosen_shape_type = None

        if loop_design == "random" and shape_design == "same":
            chosen_shape_type = get_shape_type("random")
        elif loop_design == "random" and shape_design == "incremental":
            chosen_shape_type = get_shape_type("random")
        elif loop_design == "same":
            chosen_shape_type = force_shape
        elif loop_design == "incremental" and (
            shape_design == "same" or shape_design == "incremental"
        ):
            chosen_shape_type = get_shape_type(shape_design, None, None, force_shape)

        shape_array = []

        chosen_shape_width = get_dimension(self.max_shape_width, self.min_shape_width)
        chosen_shape_height = get_dimension(
            self.max_shape_height, self.min_shape_height
        )
        chosen_shape_center = get_shape_center_point(
            chosen_shape_width, chosen_shape_height
        )
        chosen_shape_rotation_angle = get_shape_rotation_angle(shape_count)
        chosen_shape_color = get_color(self.color_theme)
        while shape_count > 0:
            shape_count_tuple = (starting_shape_count, shape_count)

            shape_object = {}
            shape_object["chosen_shape"] = chosen_shape_type
            shape_object["chosen_shape_width"] = chosen_shape_width
            shape_object["chosen_shape_height"] = (
                chosen_shape_height
                if (chosen_shape_type != "square" or "circle")
                else chosen_shape_width
            )
            shape_object["chosen_shape_center"] = chosen_shape_center
            shape_object["chosen_shape_rotation_angle"] = chosen_shape_rotation_angle
            shape_object["chosen_shape_color"] = chosen_shape_color

            if loop_design == "random" and shape_design == "random":
                chosen_shape_type = get_shape_type(shape_design)
            elif loop_design == "random" and shape_design == "incremental":
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type
                )
            elif loop_design == "same" and shape_design == "incremental":
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type
                )
            elif loop_design == "incremental" and shape_design == "random":
                chosen_shape_type = get_shape_type(shape_design)
            elif loop_design == "incremental" and shape_design == "incremental":
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type
                )

            shape_object["chosen_shape"] = chosen_shape_type
            # define types of color and blending etc
            shape_array.append(shape_object)
            shape_count -= 1
            # print(shape_object)

        return shape_array


def get_design(type):
    # loop type == True; shape type == False
    design_tuple = ("random", "same", "incremental")
    choice = None
    roll = get_random(100)
    if type:
        # loop's criteria
        match roll:
            case _ if roll < 98:
                # 98% same
                choice = design_tuple[1]
            case _ if roll < 99:
                # 1% incremental
                choice = design_tuple[2]
            case _:
                # 1% random
                choice = design_tuple[0]
    else:
        match roll:
            case _ if roll < 48:
                # 48% same
                choice = design_tuple[1]
            case _ if roll < 96:
                # 48% random
                choice = design_tuple[0]
                # 2% incremental
            case _:
                choice = design_tuple[2]

    return choice


def get_loop_count(max, min):
    # self.max_loop_count = int(self.focus_radius/250)
    # self.min_loop_count = 1
    return get_random(max, min)


def get_shape_type(
    shape_design,
    shape_count_tuple=None,
    previous_chosen_shape_type=None,
    forced_shape=None,
):
    shape_tuple = ("line", "ellipse", "circle", "rectangle", "square")
    chosen_shape = None
    if shape_count_tuple:
        max_shape_count = shape_count_tuple[0]
        cur_shape_count = shape_count_tuple[1]
        if max_shape_count == cur_shape_count:
            return previous_chosen_shape_type

    # shape design (random, same, incremental)
    match shape_design:
        case "random":
            chosen_shape = random.choice(shape_tuple)
            pass
        case "same":
            chosen_shape = forced_shape
            pass
        case "incremental":
            # edge case for same loop
            if forced_shape:
                chosen_shape = forced_shape
            else:
                prev_shape_index = shape_tuple.index(previous_chosen_shape_type)
                new_shape_index = prev_shape_index + 1
                if new_shape_index > len(shape_tuple) - 1:
                    new_shape_index = 0
                chosen_shape = shape_tuple[new_shape_index]
        case _:
            print("out of scope in get_chose_shape in Mandala")
    return chosen_shape


def get_shape_count(max_shape_count, min_shape_count):
    # self.max_shape_count = self.focus_radius/2
    # self.min_shape_count = 4
    return get_random(max_shape_count, min_shape_count)


def get_loop_radius(focus_radius, canvas_center):
    # from focus radius max to past origin 1/2 on the other side
    radius = get_random(focus_radius)
    if radius > canvas_center:
        radius *= -1
    return radius


def get_offset(max, min):
    return get_random(max, min)


def get_dimension(max, min):
    # self.max_shape_width = self.focus_radius
    # self.min_shape_width = 10
    # self.max_shape_height = self.focus_radius
    # self.min_shape_height = 10
    return get_random(max, min)


def get_color(color_theme):
    return get_random_theme_color(color_theme)


def get_blending_mode():
    choice = "multiply"
    return choice


# def get_design_array_count(self):
#     self.design_loop_array = []
#     loop_object = {}
#     self.design_full_random_colors = True
#     if self.design_full_random_colors == True:
#         loop_object = self.build_loop(True)
#     pass

# def get_random_loop_color(self):
#     # random_color_shapes 1=All random shape colors, 2.Random random shape colors, 3.Every other random shape colors, 4. No random shape colors
#     # 1 will need to get new color every shape build, shape loops object to populate true for having random shape colors
#     # 2 will need to add in the shape loops object to see if that will get populated with true or false value for random shape colors
#     # 3 will need shape loops function to %2=0 to see if populating true or false
#     # 4 will need shape loops to all be false for random shape color
#     self.random_color_shapes = 2
#     match self.random_color_shapes:
#         case 1:
#             return True
#         case 2:
#             toggle = get_random(2)
#             if (toggle == 1):
#                 return True
#             else:
#                 return False
#         case 3:
#             toggle = len(self.shape_object_array) % 2
#             print(toggle, ' toggle')
#             if (toggle == 0):
#                 return True
#             else:
#                 return False
#         case 4:
#             return False
#         case _:
#             print('out of scope in get_random_loop_color')
# # def get_chosen_loop_color(self):
# #     return get_random_theme_color(self.color_theme)

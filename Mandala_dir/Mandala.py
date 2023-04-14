from main_utility_functions.utility import get_random, get_shape_rotation_angle, get_random_theme_color
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
        self.max_shape_count = self.focus_radius
        self.min_shape_count = 4
        self.max_shape_width = self.focus_radius
        self.min_shape_width = 10
        self.max_shape_height = self.canvas_height
        self.min_shape_height = 10

        self.is_same_color_loops = True
        self.loop_color = None

        self.max_stroke = 3
        self.min_stroke = 0

        self.shape_object_array = []
        self.number_of_replication_circles = get_random(10, 3)

        self.get_shape_count_array_counts()

    def get_shape_count_array_counts(self):
        num_of_rep_cir = self.number_of_replication_circles
        while num_of_rep_cir > 0:

            # find shape count
            chosen_count = get_random(
                self.max_shape_count, self.min_shape_count)
            # find angle needed to rotate
            chosen_angle = get_shape_rotation_angle(chosen_count)
            # find depth for index
            chosen_depth = self.get_chosen_depth()
            chosen_width = get_random(
                self.max_shape_width, self.min_shape_width)
            chosen_height = get_random(
                self.max_shape_height, self.min_shape_height)
            chosen_stroke = get_random(self.max_stroke, 0)
            chosen_loop_color = self.get_chosen_loop_color()

            new_shape_object = {
                'chosen_count': chosen_count,
                'chosen_angle': chosen_angle,
                'chosen_depth': chosen_depth,
                'chosen_width': chosen_width,
                'chosen_height': chosen_height,
                'chosen_stroke': chosen_stroke,
                'chosen_loop_color': chosen_loop_color

            }
            self.shape_object_array.append(new_shape_object)
            num_of_rep_cir -= 1

    def get_chosen_depth(self):
        # from focus radius max to past origin 1/2 on the other side
        return get_random(self.focus_radius, self.canvas_center_point[1] - self.focus_radius/2)

    def get_chosen_loop_color(self):
        return get_random_theme_color(self.color_theme)

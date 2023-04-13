from main_utility_functions.utility import get_random, get_shape_rotation_angle
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
        self.center_point = (self.canvas_width/2, self.canvas_height/2)
        self.focus_radius = self.center_point[0] if self.canvas_width > self.canvas_height else self.center_point[0]
        # between half of largest width and center point of height
        self.shape_depth_array = []
        self.number_of_replication_circles = get_random(10, 3)
        self.shape_count_array = []
        self.shape_rotation_array = []

        self.get_shape_count_array_counts()

        print(self.shape_count_array)
        print(self.shape_rotation_array)

    def get_shape_count_array_counts(self):
        num_of_rep_cir = self.number_of_replication_circles
        while num_of_rep_cir > 0:
            max_count = self.focus_radius
            min_count = 4
            # find shape count
            chosen_count = get_random(max_count, min_count)
            # find angle needed to rotate
            chosen_count_angle = get_shape_rotation_angle(chosen_count)
            # find depth for index
            chosen_depth = get_random(self.focus_radius, self.center_point[1])
            self.shape_count_array.append(chosen_count)
            self.shape_rotation_array.append(chosen_count_angle)
            self.shape_depth_array.append(chosen_depth)
            num_of_rep_cir -= 1

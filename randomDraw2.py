from Mosaic_dir.Mosaic import Mosaic
from main_utility_functions import utility
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
import sys

# default variables
DEFAULT_WIDTH = 2560
DEFAULT_HEIGHT = 1440
# # COLOR_CHOICE (1=random, 2=theme)
DEFAULT_COLOR_CHOICE = utility.get_random(2)
DEFAULT_RANDOM_COLOR_COUNT = utility.get_random(5, 2)
DEFAULT_COLOR_THEME = utility.get_random_color_theme(
    DEFAULT_COLOR_CHOICE, DEFAULT_RANDOM_COLOR_COUNT
)
# DESIGN (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
DEFAULT_DESIGN = 1

# class variables
# image_file_directory
# image_count
# color_choice (1=random, 2=theme)
# random_color_count (2=dual, 3=tri, 4=quad, 5=cint)
# random_color_theme (array )
# design (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
# canvas_width
# canvas_height

# ADD CHECKS ON USER INPUTS


class randomDraw2:
    def __init__(
        self,
        location="~/Pictures/randomDraw2",
        img_count=1,
        width=DEFAULT_WIDTH,
        height=DEFAULT_HEIGHT,
    ):
        super().__init__()
        self.image_file_directory = location
        self.image_count = img_count
        # color_choice (1=random, 2=theme)
        self.color_choice = DEFAULT_COLOR_CHOICE
        # random_color_count 2=dual, 3=tri, 4=quad, 5=cint)
        self.random_color_count = DEFAULT_RANDOM_COLOR_COUNT
        self.color_theme = DEFAULT_COLOR_THEME
        # design (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
        self.design = DEFAULT_DESIGN
        self.canvas_width = width
        self.canvas_height = height

    def set_design(self, choice):
        # design (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
        print("in set_design", choice)
        match (choice):
            case 1 | 2 | 3 | 4 | 5:
                self.design = choice
            case _:
                print("out of scope")
                return "Out of scope"

    def set_color_choice(self, choice):
        # color_choice (1=random, 2=theme)
        match (choice):
            case 1:
                self.color_choice = 1
                # random_color_count (2=dual, 3=tri, 4=quad, 5=cint)
                self.random_color_count = utility.get_random(5, 2)
                # background (1=random, 2=black, 3=white)
                self.color_theme = utility.get_random_color_theme(
                    self.color_choice, self.random_color_count
                )
            case 2:
                print("in randomDraw2, set_color_choice")
                self.color_choice = 2
                self.color_theme = utility.get_random_color_theme(
                    self.color_choice, self.random_color_count
                )
            case _:
                return "Out of scope"

    def set_image_count(self, count):
        self.image_count = count

    def set_image_size(self, width, height):
        self.width = width
        self.height = height

    def set_image_destination(self, location):
        self.image_file_directory = location

    def start(self):
        # utility.test()
        print("Starting to draw", self.design)
        match (self.design):
            case 2:
                print("in square design")
                Mosaic(
                    self.canvas_width, self.canvas_height, self.design, self.color_theme
                )
            case _:
                return "Out of scope"


test = randomDraw2()
# test.set_color_choice(2)
test.set_design(2)
test.start()

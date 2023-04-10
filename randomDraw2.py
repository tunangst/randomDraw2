# from Form_dir.main_form import Main_Form
from Mosaic_dir.Mosaic import Mosaic
from main_utility_functions import utility
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QMainWindow, QWidget, QVBoxLayout, QDialog
import sys
from pprint import pprint

# default variables
DEFAULT_WIDTH = 2560
DEFAULT_HEIGHT = 1440
# COLOR_CHOICE (1=random, 2=theme)
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
# random_color_count (2=dual, 3=tri, 4=quad, 5=penta)
# random_color_theme (array )
# design (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
# canvas_width
# canvas_height

# ADD CHECKS ON USER INPUTS
DEFAULT_IMAGE_COUNT = 100


class randomDraw2(QMainWindow):
    def __init__(
        self,
        cwidth=DEFAULT_WIDTH,
        cheight=DEFAULT_HEIGHT,
        design=DEFAULT_DESIGN,
        color_choice=DEFAULT_COLOR_CHOICE,
        color_count=DEFAULT_RANDOM_COLOR_COUNT,
        img_count=DEFAULT_IMAGE_COUNT,
        location="~/Pictures/randomDraw2"
    ):
        super().__init__()
        self.canvas_width = cwidth
        self.canvas_height = cheight
        self.design = design
        self.color_choice = color_choice
        self.color_count = color_count
        self.image_file_directory = location
        self.image_count = img_count
        # color_choice (1=random, 2=theme)
        # color_count 2=dual, 3=tri, 4=quad, 5=cint)
        self.color_theme = utility.get_random_color_theme(
            DEFAULT_COLOR_CHOICE, DEFAULT_RANDOM_COLOR_COUNT
        )
        # design (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
        self.mosaic_painting = None

        # self.canvas_widget = QWidget()
        # self.canvas_layout = QVBoxLayout()
        # self.canvas_widget.setLayout(self.main_container_layout)
        # self.setCentralWidget(self.canvas_widget)

        self.start()

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
                # color_count (2=dual, 3=tri, 4=quad, 5=cint)
                self.color_count = utility.get_random(5, 2)
                # background (1=random, 2=black, 3=white)
                self.color_theme = utility.get_random_color_theme(
                    self.color_choice, self.color_count
                )
            case 2:
                print("in randomDraw2, set_color_choice")
                self.color_choice = 2
                self.color_theme = utility.get_random_color_theme(
                    self.color_choice, self.color_count
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
        print('started')

        match (self.design):
            case 2:
                print("in square design")
                self.mosaic_painting = Mosaic(
                    self.canvas_width, self.canvas_height, self.design, self.color_theme
                )
                # mosaic_painting.show()
                print('randomDraw Mosaic_painting')
                pprint(vars(self.mosaic_painting))

                return self.mosaic_painting

            case _:
                return "Out of scope"

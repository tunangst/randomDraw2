import Mosaic.Mosaic as Mosaic
from main_utility_functions import utility
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
import sys

DEFAULT_WIDTH = 2560
DEFAULT_HEIGHT = 1440
DEFAULT_DESIGN = 'square'
FEATURE_CONTROL_SIZE = DEFAULT_WIDTH if DEFAULT_WIDTH > DEFAULT_HEIGHT else DEFAULT_HEIGHT


class randomDraw2():
    def __init__(self, location="~/Pictures/randomDraw2", img_count=1, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        super().__init__()
        self.image_file_directory = location
        self.image_count = img_count
        self.random_color = False
        self.canvas_width = width
        self.canvas_height = height

        # self.app = QApplication(sys.argv)
        # self.scene = QGraphicsScene(0, 0,
        #                             self.canvas_width, self.canvas_height)
        # self.view = QGraphicsView(self.scene)
        # # # show the scene
        # self.view.show()
        # # # keep the scene open
        # self.app.exec()

    def set_image_count(self, count):
        self.image_count = count

    def set_image_size(self, width, height):
        self.width = width
        self.height = height

    def set_image_destination(self, location):
        self.image_file_directory = location

    def start(self):
        print('Starting to draw')
        run = Mosaic.Mosaic_style(
            self.canvas_width, self.canvas_height)
        run.squares()
        # run.draw_something()
        # # show the scene
        # run.view = QGraphicsView(self.scene)
        # run.view.show()
        # # keep the scene open
        # self.app.exec()


test = randomDraw2()
test.start()

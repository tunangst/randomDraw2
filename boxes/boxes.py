from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
import sys
import math
import cairo

DEFAULT_WIDTH = 2560
DEFAULT_HEIGHT = 1440


# class Boxes:
#     def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
#         self.random_color = False
#         self.canvas_width = width
#         self.canvas_height = height

#     def create_canvas(self):
#         surface = cairo.ImageSurface(
#             cairo.FORMAT_ARGB32, self.canvas_width, self.canvas_height)
#         ctx = cairo.Context(surface)
#         ctx.scale(self.canvas_width, self.canvas_height)


app = QApplication(sys.argv)

# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)

view = QGraphicsView(scene)
view.show()
app.exec()


# test = Boxes(DEFAULT_WIDTH, DEFAULT_HEIGHT)
# print(test.random_color)
# print(test.canvas_width)
# print(test.canvas_height)
# test.create_canvas()

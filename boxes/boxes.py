from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
import sys
import math
import cairo


def find_closest_quantity(width, count):
    increment = 0
    while (increment < count/2):
        print(width, count, increment)
        if (width % (count+increment) == 0):
            return (count+increment)
        if (width % (count-increment) == 0):
            return (count-increment)
        increment += 1


DEFAULT_WIDTH = 2560
DEFAULT_HEIGHT = 1440
DEFAULT_DESIGN = 'square'
CONTROL_SIZE = DEFAULT_WIDTH if DEFAULT_WIDTH > DEFAULT_HEIGHT else DEFAULT_HEIGHT
DEFAULT_COUNT = find_closest_quantity(CONTROL_SIZE, 100)
WIDTH = math.floor(CONTROL_SIZE/DEFAULT_COUNT)
HEIGHT = WIDTH


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        super().__init__()
        self.random_color = False
        self.canvas_width = width
        self.canvas_height = height
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.canvas_width, self.canvas_height)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def create(self):
        app = QApplication(sys.argv)
        # Defining a scene rect, with it's origin at 0,0
        scene = QGraphicsScene(0, 0, self.canvas_width, self.canvas_height)
        view = QGraphicsView(scene)
        view.show()
        app.exec()

    def squares(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)

        cur_x_coord = 0
        cur_y_coord = 0
        while cur_y_coord < DEFAULT_HEIGHT:
            print(cur_x_coord, cur_y_coord, cur_y_coord, DEFAULT_HEIGHT)
            painter.drawRect(cur_x_coord, cur_y_coord,
                             WIDTH, HEIGHT)

            cur_x_coord += WIDTH
            if cur_x_coord > DEFAULT_WIDTH:
                cur_x_coord = 0
                cur_y_coord += HEIGHT

        painter.end()
        self.label.setPixmap(canvas)

# If we don't set this on creation, we can set it later with .setSceneRect


app = QtWidgets.QApplication(sys.argv)
window = Main_Window()
window.show()
window.squares()
app.exec()

# print(2560 % 100)
# print(100 + 2560 % 100)
# print(100 - 2560 % 100)
# print(2560 / 64)

# loop runs an increment starting at 0 and runs to half of the suggested count.
# each increment it will check if width/count+increment and width/count-increment is 0 to see which is closer


print(find_closest_quantity(2560, 100))
print(2560 % 80)
print(2560 / 80)

# print(DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_DESIGN,
#   CONTROL_SIZE, DEFAULT_COUNT, WIDTH, HEIGHT)

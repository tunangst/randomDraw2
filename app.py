import sys
from pprint import pprint
from Form_dir.main_form import Main_Form
from Mandala_dir.rotating_shapes import Rotating_shapes
# from randomDraw2 import randomDraw2
from Mosaic_dir.Squares import Square
from Mosaic_dir.ReflectingTiles import ReflectingTiles
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)


class app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_window = None
        self.canvas_window = None

        self.start()

    def start(self):
        self.form_window = Main_Form(parent=self)
        self.design = self.form_window.design_dropdown_value

        self.canvas_window = self.build_shape_class(5)
        # self.canvas_window = Square(self.form_window.canvas_width,
        #                             self.form_window.canvas_height,
        #                             self.form_window.design_dropdown_value,
        #                             self.form_window.color_choice_index,
        #                             self.form_window.color_count_index)
        self.form_window.show()
        # self.canvas_window.show()

    def refresh_received(self):
        self.canvas_window = self.build_shape_class(5)
        # print(self.canvas_window.__dict__)
        print('refreshed')

    def build_shape_class(self, design_number):
        # DESIGN (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
        design_number = 6
        match design_number:
            # case 2:
            #     return Square(
            #         self.form_window.canvas_width,
            #         self.form_window.canvas_height,
            #         self.form_window.design_dropdown_value,
            #         self.form_window.color_choice_index,
            #         self.form_window.color_count_index
            #     )
            # case 5:
            #     return Rotating_shapes()
            # case 6:
            #     return ReflectingTiles()
            case _:
                print('out of scope')
                return ReflectingTiles()


run_app = QApplication(sys.argv)

start_window = app()

sys.exit(run_app.exec())

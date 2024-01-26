import sys
from pprint import pprint
from Form_dir.main_form import Main_Form
from RotatingShapes_dir.RotatingShapesPainter import RotatingShapesPainter
from TestBlends_dir.TestBlends import TestBlends

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
    QWidget,
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ class variables ~~~~~~~~~~~~~~~~~~~~
# self.form_window
# self.canvas_window
# self.design
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ class variables ~~~~~~~~~~~~~~~~~~~~


class app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_window = None
        self.canvas_window = None

        self.start()

    def start(self):
        self.form_window = Main_Form(parent=self)
        self.design = self.form_window.design_dropdown_value
        self.canvas_window = self.choose_program(5)
        self.form_window.show()

    def refresh_received(self):
        self.canvas_window = self.choose_program(5)
        print("refreshed")

    def choose_program(self, design_number):
        # DESIGN (1=random, 2=square, 3=rectangle, 4=scales, 5=rotating shapes)
        design_number = 5
        match design_number:
            # case 2:
            #     return Square(
            #         self.form_window.canvas_width,
            #         self.form_window.canvas_height,
            #         self.form_window.design_dropdown_value,
            #         self.form_window.color_choice_index,
            #         self.form_window.color_count_index
            #     )
            case 5:
                return RotatingShapesPainter()
            # case 6:
            #     return ReflectingTiles()
            case 7:
                return TestBlends()
            case _:
                print("out of scope")
                return ReflectingTiles()


run_app = QApplication(sys.argv)
start_window = app()
sys.exit(run_app.exec())

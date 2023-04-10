import sys
from pprint import pprint
from Form_dir.main_form import Main_Form
from randomDraw2 import randomDraw2
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
        # self.form_window.window_refresh.connect(self.refresh_received)
        self.canvas_window = randomDraw2()
        self.form_window.show()
        # self.canvas_window.show()

    def refresh_received(self):
        pprint(vars(self.form_window))
        self.canvas_window = randomDraw2(
            cwidth=self.form_window.canvas_width,
            cheight=self.form_window.canvas_height,
            design=self.form_window.design_dropdown_value,
            color_choice=self.form_window.color_choice_index,
            color_count=self.form_window.color_count_index
            # img_count=self.form_window.shape_count
        )
        self.refresh_canvas_window()

        print('refreshed')

    def refresh_canvas_window(self):
        print('inside refresh canvas')
        squares_painting = self.canvas_window.mosaic_painting.squares_painting.squares_board
        squares_painting.setWindowTitle("randomDraw2 Canvas")
        squares_painting.showMaximized()
        squares_painting.show()


run_app = QApplication(sys.argv)

start_window = app()

sys.exit(run_app.exec())

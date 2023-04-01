import sys
from main_utility_functions import utility

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
    QWidget,
)

# DEFAULT VARIABLE VALUES
DEFAULT_SHAPE_COUNT = 100

# Subclass QMainWindow to customize your application's main window
class Squares_Form(QMainWindow):
    def __init__(self, cwidth):
        super().__init__()
        self.shape_count = DEFAULT_SHAPE_COUNT
        self.canvas_width = cwidth

        self.setWindowTitle("Squares Controls")
        layout = QVBoxLayout()

        shape_count_box = QLineEdit()
        # shape_count_box.setMaxLength(6)
        shape_count_box.setPlaceholderText(str(self.shape_count))
        shape_count_box.textChanged.connect(self.shape_count_text_changed)

        layout.addWidget(shape_count_box)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def shape_count_text_changed(self, s):
        int_count = int(s)
        suggested_count = utility.get_closest_box_count(self.canvas_width, int_count)
        self.canvas_width = suggested_count
        print(self.canvas_width)


# app = QApplication(sys.argv)
# mosaic_control_window = Squares_Form()
# mosaic_control_window.show()

# app.exec()

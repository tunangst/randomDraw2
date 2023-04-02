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
    QHBoxLayout,
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
        additional_container_layout = QVBoxLayout()
        shape_count_layout = QHBoxLayout()

        additional_container_header = QLabel("Additional Squares Config")
        additional_container_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        shape_count_label = QLabel("Aprox. Shape Count")

        self.shape_count_box = QLineEdit()
        # shape_count_box.setMaxLength(6)
        self.shape_count_box.setPlaceholderText(str(self.shape_count))
        self.shape_count_box.textChanged.connect(self.shape_count_text_changed)

        additional_container_layout.addWidget(additional_container_header)
        additional_container_layout.addLayout(shape_count_layout)

        shape_count_layout.addWidget(shape_count_label)
        shape_count_layout.addWidget(self.shape_count_box)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        widget = QWidget()
        widget.setLayout(additional_container_layout)
        self.setCentralWidget(widget)

    def shape_count_text_changed(self, s):
        if s != "":
            int_count = int(s)
            suggested_count = utility.get_closest_box_count(
                self.canvas_width, int_count
            )
            self.shape_count = suggested_count
            self.shape_count_box.setText(str(suggested_count))
        print(self.shape_count)


# app = QApplication(sys.argv)
# mosaic_control_window = Squares_Form()
# mosaic_control_window.show()

# app.exec()

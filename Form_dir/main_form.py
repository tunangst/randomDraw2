import sys
from Form_dir.squares_form import Squares_Form
from randomDraw2 import randomDraw2
from PyQt6 import QtCore
from PyQt6.QtCore import Qt, pyqtSignal
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
DEFAULT_DESIGN_DROPDOWN_VALUE = 1
DEFAULT_CANVAS_WIDTH = 2560
DEFAULT_CANVAS_HEIGHT = 1440
DEFAULT_COLOR_CHOICE_INDEX = 1
DEFAULT_COLOR_COUNT_INDEX = 1

# Subclass QMainWindow to customize your application's main window


class Main_Form(QMainWindow):
    # window_refresh = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.main_window = QVBoxLayout()
        self.image_instance = QVBoxLayout()
        # self.setCentralWidget(self.main_window)

        self.design_dropdown_value = DEFAULT_DESIGN_DROPDOWN_VALUE
        self.canvas_width = DEFAULT_CANVAS_WIDTH
        self.canvas_height = DEFAULT_CANVAS_HEIGHT
        # random_color_count (1=random, 2=dual, 3=tri, 4=quad, 5=penta)
        self.color_choice_index = DEFAULT_COLOR_CHOICE_INDEX
        self.color_count_index = DEFAULT_COLOR_COUNT_INDEX

        self.setWindowTitle("randomDraw2 Controls")
        self.move(0, 0)

        self.main_container_layout = QVBoxLayout()

        draw_button = QPushButton("DRAW")
        draw_button.clicked.connect(self.draw_btn_clicked)

        core_container_layout = QVBoxLayout()
        design_layout = QHBoxLayout()
        width_layout = QHBoxLayout()
        height_layout = QHBoxLayout()
        color_choice_layout = QHBoxLayout()
        color_count_layout = QHBoxLayout()

        design_label = QLabel("Select Design")
        design_dropdown = QComboBox()
        # DESIGN (1=random, 2=square, 3=rectangle, 4=scales, 5=mandala)
        design_dropdown.addItems(
            [
                "Random",
                "Squares",
                "Bricks",
                "Scales",
                "Mandala",
                "Flower Drop",
                "Spirograph",
            ]
        )
        # Sends the current index (position) of the selected item.
        design_dropdown.currentIndexChanged.connect(self.design_index_changed)
        # There is an alternate signal to send the text.
        design_dropdown.currentTextChanged.connect(self.design_text_changed)

        width_label = QLabel("Select Width")
        width_box = QLineEdit()
        width_box.setMaxLength(6)
        width_box.setPlaceholderText(str(self.canvas_width))
        width_box.textChanged.connect(self.width_text_changed)

        height_label = QLabel("Select Height")
        height_box = QLineEdit()
        height_box.setMaxLength(6)
        height_box.setPlaceholderText(str(self.canvas_height))
        height_box.textChanged.connect(self.height_text_changed)

        color_choice_label = QLabel("Color Selection")
        color_choice_dropdown = QComboBox()
        # COLOR_CHOICE (1=random, 2=theme)
        color_choice_dropdown.addItems(["Random", "Theme"])
        color_choice_dropdown.currentIndexChanged.connect(
            self.color_choice_index_changed)
        color_choice_dropdown.currentTextChanged.connect(
            self.color_choice_text_changed)

        # WILL NEED TO BE DISABLED IF THEME IS CHOSEN
        color_count_label = QLabel("How many colors?")
        color_count_dropdown = QComboBox()
        # random_color_count (2=dual, 3=tri, 4=quad, 5=penta)
        color_count_dropdown.addItems(
            ["Random", "Dual", "Tri", "Quad", "Penta"])
        color_count_dropdown.currentIndexChanged.connect(
            self.color_count_index_changed)
        color_count_dropdown.currentTextChanged.connect(
            self.color_count_text_changed)

        self.main_container_layout.addWidget(draw_button)

        self.main_container_layout.addLayout(core_container_layout)
        core_container_layout.addLayout(design_layout)
        design_layout.addWidget(design_label)
        design_layout.addWidget(design_dropdown)
        core_container_layout.addLayout(width_layout)
        width_layout.addWidget(width_label)
        width_layout.addWidget(width_box)
        core_container_layout.addLayout(height_layout)
        height_layout.addWidget(height_label)
        height_layout.addWidget(height_box)
        core_container_layout.addLayout(color_choice_layout)
        color_choice_layout.addWidget(color_choice_label)
        color_choice_layout.addWidget(color_choice_dropdown)
        core_container_layout.addLayout(color_count_layout)
        color_count_layout.addWidget(color_count_label)
        color_count_layout.addWidget(color_count_dropdown)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        # app = QApplication(sys.argv)
        self.controls_widget = QWidget()
        self.controls_widget.setLayout(self.main_container_layout)
        self.setCentralWidget(self.controls_widget)
        # Keep this controls window on top
        self.setWindowFlags(self.windowFlags() ^
                            Qt.WindowType.WindowStaysOnTopHint)

        # app.exec()

    # def refresh(self, event):
    #     self.window_refresh.emit()
        # print(event)
        # event.accept()
        # pass
        # self.window_closed.emit()
        # event.accept()
        # event.ignore() # if you want the window to never be closed

    # def event(self, e):
    #     print(e)

    def design_index_changed(self, i):  # i is an int
        print(i + 1)
        self.design_dropdown_value = i + 1
        match self.design_dropdown_value:
            case 2:
                print("open squares module")
                squares_section = Squares_Form(self.canvas_width)
                self.main_container_layout.addWidget(squares_section)

            case _:
                print("out of scope")

    def design_text_changed(self, s):  # s is a str
        print(s)

    def width_text_changed(self, s):
        if s != "":
            self.canvas_width = int(s)
            print(self.canvas_width)

    def height_text_changed(self, s):
        if s != "":
            self.canvas_height = int(s)
            print(self.canvas_height)

    def color_choice_index_changed(self, i):  # i is an int
        self.color_choice_index = i + 1
        print(i + 1)

    def color_choice_text_changed(self, s):  # s is a str
        print(s)

    def color_count_index_changed(self, i):  # i is an int
        self.color_count_index = i + 1
        print(i + 1)

    def color_count_text_changed(self, s):  # s is a str
        print(s)

    def draw_btn_clicked(self, e):
        self.parent.refresh_received()
        # print(e)

        # self.image_instance = None
        # self.image_instance = randomDraw2(self.canvas_width, self.canvas_height,
        #                                   self.design_dropdown_value, self.color_choice_index, self.color_count_index)
        # self.image_instance.show()


# # squares_window = Squares_Form(control_window.canvas_width)
# # squares_window.show()
# app = QApplication(sys.argv)
# control_window = Main_Form()
# control_window.show()
# sys.exit(app.exec())

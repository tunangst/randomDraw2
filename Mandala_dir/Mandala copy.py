import random
from main_utility_functions.utility import get_random

# self.loop_shape_pattern_type = self.get_loop_shape_pattern_type(design_loop_shape_pattern_type, loop_count)


class Mandala:
    def __init__(self):
        self.canvas_width = 5321
        self.canvas_height = 1440
        self.canvas_center_point = (self.canvas_width / 2, self.canvas_height / 2)
        self.focus_radius = (
            self.canvas_center_point[0]
            if self.canvas_width > self.canvas_height
            else self.canvas_center_point[0]
        )

        self.max_loop_count = int(self.focus_radius / 250)
        self.min_loop_count = 1
        self.max_shape_count = self.focus_radius / 2
        self.min_shape_count = 4

        self.build_design()

    def build_design(self):

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # (random, same, incremental)
        loops_design = "random"
        # (random, same, incremental)
        shapes_design = "random"
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        design_loop_array = []
        loop_count = get_loop_count(self.max_loop_count, self.min_loop_count)

        print("loop count", loop_count)

        self.design_full_random_colors = True

        match loops_design:
            case "random":
                self.design_loop_array = self.build_loop(
                    loop_count, loops_design, shapes_design
                )
                pass
            case "same":
                # find alternate (all same, random loop, incremental)
                # (All Random, Random Random, Every Other Random, All Same, Incremental)
                pass
            case "incremental":
                pass
            case _:
                print("out of scope in get_chose_shape in Mandala copy")

        # else:
        #     self.design_loop_array = self.build_loop(self.loop_count, self.design_loop_shape_pattern_type)

    def build_loop(self, starting_loop_count, loops_design, shapes_design):
        self.loop_shape_array = []
        # (random, same, incremental)

        #   same loop, random shape
        #       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape
        #   same loop, same shape
        #       random shape is chosen on the main loop and loop pushes it to forced shape on shape
        #   same loop, incremental shape
        #       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
        #   incremental loop, random shape
        #
        #   incremental loop, same shape
        #       loop starts at first shape and forces it to shape, each consecutive loop will need to grab the next shape in line
        #   incremental loop, incremental shape
        #       loop starts at first shape and forces it to shape, build shape will start with that shape then increment the remaining loop its'self
        #       next loops start with the next shape in line and do the same to build shape.
        # loops_design = None
        # (random, same, incremental)
        # shapes_design = None
        forced_shape = None

        # self.loop_shape_pattern_type = self.get_loop_shape_pattern_type(design_loop_shape_pattern_type, loop_count)
        loop_count = starting_loop_count
        while loop_count > 0:
            loop_object = {}
            loop_count_tuple = (starting_loop_count, loop_count)

            chosen_shape_count = get_shape_count(
                self.max_shape_count, self.min_shape_count
            )
            if loops_design == "same":
                forced_shape = get_shape_type("random")
            match loops_design:
                case "random":
                    #   random loop, random shape
                    #       loop does not store a design
                    #       shape chooses a new shape each time
                    #   random loop, same shape
                    #       loop does not store a design
                    #       shape stores a random constant shape
                    #   random loop, incremental shape
                    #       loop does not store a design
                    #       shape starts a random shape at the start and chooses the next in line every shape
                    loop_object["shape_array"] = self.build_shape(
                        loops_design, chosen_shape_count, shapes_design, loop_count_tuple, None
                    )
                    pass
                case "same":
                    forced_shape = get_shape_type("random")
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        forced_shape,
                    )
                    #   same loop, random shape
                    #       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape.
                    #       shape is used for entire loop
                    #   same loop, same shape
                    #       random shape is chosen on the main loop and loop pushes it to forced shape on shape, shape uses the same for each shape
                    #       shape is same shape for everything
                    #   same loop, incremental shape
                    #       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
                    #       shape starts at same shape and iterates
                    pass
                case "incremental":
                    pass
                case _:
                    print("out of scope in build loop in Mandala")

            self.loop_shape_array.append(loop_object)
            loop_count -= 1

        return self.loop_shape_array

    def build_shape(
        self, loop_design, shape_count, shape_design, loop_count_tuple, force_shape=None
    ):
        force_shape = None
        chosen_shape_type = None
        #   random loop, random shape
        #       loop does not store a design
        #       shape chooses a new shape each time
        #   random loop, same shape
        #       loop does not store a design
        #       shape stores a random constant shape
        #   random loop, incremental shape
        #       loop does not store a design
        #       shape starts a random shape at the start and chooses the next in line every shape
        if force_shape == None and shape_design == 'same':
            chosen_shape_type = get_shape_type(shape_design)
        if loop_design == 'same':
            chosen_shape_type = force_shape
            
        shape_array = []

        while shape_count > 0:
            #
            if force_shape == None and shape_design == "random":
                chosen_shape_type = get_shape_type(shape_design, loop_count_tuple, None)
            if loop_design == 'same' and shape_design == 'incremental':
                if loop_count_tuple[0] == loop_count_tuple[1]:
                    pass
                else:
                    chosen_shape_type get_next_shape(force_shape)
            #

            shape_object = {}
            shape_object["chosen_shape"] = chosen_shape_type
            print(chosen_shape_type)

            # define types of color and blending etc
            shape_array.append(shape_object)
            shape_count -= 1
            # print(shape_object)

        return shape_array


# loop functions
def get_loop_count(max, min):
    # self.max_loop_count = int(self.focus_radius/250)
    # self.min_loop_count = 1
    return get_random(max, min)


# shape functions


def get_shape_count(max_shape_count, min_shape_count):
    # self.max_shape_count = self.focus_radius/2
    # self.min_shape_count = 4
    return get_random(max_shape_count, min_shape_count)


def get_shape_type(
    shape_design, loop_count_tuple=None, previous_chosen_shape_type=None
):
    shape_tuple = ("line", "ellipse", "circle", "rectangle", "square")
    chosen_shape = None
    if loop_count_tuple:
        max_loop_count = loop_count_tuple[0]
        cur_loop_count = loop_count_tuple[1]

    # (line, ellipse, circle, rectangle, square)
    # shape design (random, same, incremental)
    match shape_design:
        case "random":
            chosen_shape = random.choice(shape_tuple)
            pass
        case "same":
            chosen_shape = ""
            pass
        case "incremental":
            prev_shape_index = shape_tuple.index(previous_chosen_shape_type)
            new_shape_index = prev_shape_index + 1
            if new_shape_index > len(shape_tuple) -1:
                new_shape_index = 0
            chosen_shape = shape_tuple[new_shape_index]
        case _:
            print("out of scope in get_chose_shape in Mandala")
    return chosen_shape

def get_next_shape(prev_shape):
    

test = Mandala()

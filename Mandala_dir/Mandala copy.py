import random
from main_utility_functions.utility import get_random
from pprint import pprint

# (random, same, incremental)

#   same loop, random shape
#       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape
#   same loop, same shape
#       random shape is chosen on the main loop and loop pushes it to forced shape on shape
#   same loop, incremental shape
#       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
#   incremental loop, random shape
#       will end up all random
#   incremental loop, same shape
#       loop starts at first shape and forces it to shape, each consecutive loop will need to grab the next shape in line
#   incremental loop, incremental shape
#       loop starts at first shape and forces it to shape, build shape will start with that shape then increment the remaining loop its'self
#       next loops start with the next shape in line and do the same to build shape.


class Mandala:
    def __init__(self):
        self.canvas_width = 5321
        self.canvas_height = 1440
        self.canvas_center_point = (
            self.canvas_width / 2, self.canvas_height / 2)
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
        loops_design = "incremental"
        # (random, same, incremental)
        shapes_design = "incremental"
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        design_loop_array = []
        loop_count = get_loop_count(self.max_loop_count, self.min_loop_count)

        self.design_full_random_colors = True

        design_loop_array = self.build_loop(
            loop_count, loops_design, shapes_design
        )
        pprint(design_loop_array)

    def build_loop(self, starting_loop_count, loops_design, shapes_design):
        self.loop_shape_array = []

        forced_shape = None
        if loops_design == "same" or loops_design == 'incremental':
            forced_shape = get_shape_type("random")
        # self.loop_shape_pattern_type = self.get_loop_shape_pattern_type(design_loop_shape_pattern_type, loop_count)
        loop_count = starting_loop_count
        while loop_count > 0:
            loop_object = {}
            loop_count_tuple = (starting_loop_count, loop_count)

            chosen_shape_count = get_shape_count(
                self.max_shape_count, self.min_shape_count
            )
            chosen_shape_count = 10
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
                    if loops_design == "same" and shapes_design == 'random':
                        forced_shape = get_shape_type("random")
                    #   same loop, random shape
                    #       random shape is chosen on the loop on each loop and loop pushes it to forced shape on shape.
                    #       shape is used for entire loop
                    #   same loop, same shape
                    #       random shape is chosen on the main loop and loop pushes it to forced shape on shape, shape uses the same for each shape
                    #       shape is same shape for everything
                    #   same loop, incremental shape
                    #       random shape is chosen on the main loop, each loop will need to send incrementing value and each loop will push it to forced shape on shape
                    #       shape starts at same shape and iterates
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        forced_shape
                    )
                case "incremental":
                    forced_shape = get_shape_type(
                        'incremental', loop_count_tuple, forced_shape)
                    loop_object["shape_array"] = self.build_shape(
                        loops_design,
                        chosen_shape_count,
                        shapes_design,
                        loop_count_tuple,
                        forced_shape
                    )
                    pass
                case _:
                    print("out of scope in build loop in Mandala")

            self.loop_shape_array.append(loop_object)
            loop_count -= 1

        return self.loop_shape_array

    def build_shape(
        self, loop_design, shape_count, shape_design, loop_count_tuple, force_shape=None
    ):
        starting_shape_count = shape_count
        chosen_shape_type = None

        if loop_design == 'random' and shape_design == 'same':
            chosen_shape_type = get_shape_type('random')
        elif loop_design == 'random' and shape_design == 'incremental':
            chosen_shape_type = get_shape_type('random')
        elif loop_design == 'same':
            chosen_shape_type = force_shape
        elif loop_design == 'incremental' and (shape_design == 'same' or shape_design == 'incremental'):
            chosen_shape_type = get_shape_type(
                shape_design, None, None, force_shape)

        shape_array = []

        while shape_count > 0:
            shape_count_tuple = (starting_shape_count, shape_count)

            if loop_design == 'random' and shape_design == 'random':
                chosen_shape_type = get_shape_type(
                    shape_design)
            elif loop_design == 'random' and shape_design == 'incremental':
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type)
            elif loop_design == 'same' and shape_design == 'incremental':
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type)
            elif loop_design == 'incremental' and shape_design == 'random':
                chosen_shape_type = get_shape_type(
                    shape_design)
            elif loop_design == 'incremental' and shape_design == 'incremental':
                chosen_shape_type = get_shape_type(
                    shape_design, shape_count_tuple, chosen_shape_type)

            shape_object = {}
            shape_object["chosen_shape"] = chosen_shape_type

            # define types of color and blending etc
            shape_array.append(shape_object)
            shape_count -= 1

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
    shape_design, shape_count_tuple=None, previous_chosen_shape_type=None, forced_shape=None
):
    shape_tuple = ("line", "ellipse", "circle", "rectangle", "square")
    chosen_shape = None
    if shape_count_tuple:
        max_shape_count = shape_count_tuple[0]
        cur_shape_count = shape_count_tuple[1]
        if max_shape_count == cur_shape_count:
            return previous_chosen_shape_type

    # shape design (random, same, incremental)
    match shape_design:
        case "random":
            chosen_shape = random.choice(shape_tuple)
            pass
        case "same":
            chosen_shape = forced_shape
            pass
        case "incremental":
            # edge case for same loop
            if forced_shape:
                chosen_shape = forced_shape
            else:
                prev_shape_index = shape_tuple.index(
                    previous_chosen_shape_type)
                new_shape_index = prev_shape_index + 1
                if new_shape_index > len(shape_tuple) - 1:
                    new_shape_index = 0
                chosen_shape = shape_tuple[new_shape_index]
        case _:
            print("out of scope in get_chose_shape in Mandala")
    return chosen_shape


test = Mandala()

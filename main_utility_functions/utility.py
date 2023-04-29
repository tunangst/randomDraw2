import random
from contextlib import redirect_stdout


def get_random_theme_color(color_array):
    random_index = get_random(len(color_array) - 1, 0)
    # print('in get_random_theme_color', random_index, ' index in ', color_array, ' choice is ', color_array[random_index])
    return color_array[random_index]


def get_chosen_theme_color(color_array, color_index):
    chosen_color = color_array[color_index]
    return chosen_color


def get_random_rgb_color(bg=False):
    # bg is true, labeled as background choice black or white
    color_dictionary = {}
    if bg:
        b_or_w = get_random(2)
        if b_or_w == 1:
            return {"r": 0, "g": 0, "b": 0}
        else:
            return {"r": 255, "g": 255, "b": 255}
    else:
        r = get_random(255)
        g = get_random(255)
        b = get_random(255)
        color_dictionary["r"] = r
        color_dictionary["g"] = g
        color_dictionary["b"] = b
        # print('COLOR DICTIONARY ', color_dictionary)
    return color_dictionary


def get_random_color_theme(color_choice, color_count):
    # color_choice (1=random, 2=theme)
    match (color_choice):
        case 1:
            # print('in get_random_color_theme choice =2')
            chosen_theme = []
            while_index = 0
            while while_index < color_count:
                if while_index == 0:
                    chosen_color = get_random_rgb_color(True)
                else:
                    chosen_color = get_random_rgb_color()
                chosen_theme.append(chosen_color)
                # print(chosen_color, while_index, 'chosen color appended to array', chosen_theme)
                while_index += 1
            return chosen_theme
        case 2:
            # import themes array
            from .Themes.themes import themes_array
            print('in get_random_color_theme, theme choice case 2')
            # print('in get_random_color_theme choice =1')
            # choose array from master
            print('in utility get_random_color_theme, forcing color theme: remove later')
            chosen_theme = themes_array[0]
            # chosen_theme = themes_array[get_random(len(themes_array))]
            return chosen_theme
        case _:
            print("Out of scope")


def get_random(ceil, floor=1):
    # color_choice (1=random, 2=theme)
    # random_color_count (1=dual, 2=tri, 3=quad, 4=cint)
    return random.randint(floor, ceil)


def get_design_type():
    choice = random.randint(1, 2)
    match (choice):
        case 1:
            return "Mandala"
        case 2:
            return "Box"
        case _:
            return "Out of scope"


def get_sub_design_type():
    choice = random.randint(1, 3)
    # force 1 for working session
    choice = 1
    match (choice):
        case 1:
            return "Square"
        case 2:
            return "Rectangle"
        case 3:
            return "Scales"
        case _:
            return "Out of scope"


def get_closest_box_count(width, count):
    increment = 0
    while increment < count / 2:
        if width % (count + increment) == 0:
            return count + increment
        if width % (count - increment) == 0:
            return count - increment
        increment += 1


def get_shape_center_point(shape_width, shape_height):
    center_of_shape = (shape_width/2, shape_height/2)
    return center_of_shape


def get_shape_center_rotation_point(shape_depth, canvas_center_point):
    # will be centered on x-axis
    canvas_center_width = 0
    canvas_center_height = canvas_center_point[1]
    center_of_canvas_height_relative_to_shape_center = canvas_center_height - \
        shape_depth
    center_point = (canvas_center_width,
                    center_of_canvas_height_relative_to_shape_center)
    # print(center_point)
    return center_point


def get_shape_rotation_angle(shape_quantity):
    angle = 360/shape_quantity
    return angle


def test():
    from .Themes.themes3 import themes_array

    full_list = []
    for theme in themes_array:
        new_color_theme_array_of_objects = []
        for color in theme:

            # print(color)
            color_string_split = color.split(", ")
            # print(color_string_split)
            r = int(color_string_split[0][4:])
            g = int(color_string_split[1])
            b = int(color_string_split[2][0: len(color_string_split[2]) - 1])
            # print('r g b ', r, ' ', g, ' ', b)
            new_color_theme_array_of_objects.append({"r": r, "g": g, "b": b})
            # print(new_color_theme_array_of_objects)

        full_list.append(new_color_theme_array_of_objects)
    print(len(full_list), len(themes_array))
    with open("themes2.py", mode="wt") as f:
        with redirect_stdout(f):
            print(full_list)

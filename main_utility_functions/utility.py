import random


def get_random_color_theme():
    # import themes array
    from .Themes.themes import themes_array
    print(len(themes_array))
    # choose array from master
    chosen_theme = themes_array[get_random(len(themes_array))]
    print(chosen_theme)
    return chosen_theme


def get_random(ceil):
    # color_choice (1=random, 2=theme)
    # random_color_count (1=dual, 2=tri, 3=quad, 4=cint)
    return random.randint(1, ceil)


def get_design_type():
    choice = random.randint(1, 2)
    match(choice):
        case 1:
            return 'Mandala'
        case 2:
            return 'Box'
        case _:
            return 'Out of scope'


def get_sub_design_type():
    choice = random.randint(1, 3)
    # force 1 for working session
    choice = 1
    match(choice):
        case 1:
            return 'Square'
        case 2:
            return 'Rectangle'
        case 3:
            return 'Scales'
        case _:
            return 'Out of scope'


def get_closest_box_count(width, count):
    increment = 0
    while (increment < count/2):
        if (width % (count+increment) == 0):
            return (count+increment)
        if (width % (count-increment) == 0):
            return (count-increment)
        increment += 1

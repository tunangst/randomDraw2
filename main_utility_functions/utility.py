import random


def get_design_type():
    choice = random.randint(1, 2)

    match(choice):
        case 1:
            return 'Mandala'
        case 2:
            return 'Box'
        case _:
            return 'Out of scope'


def find_closest_box_count(width, count):
    increment = 0
    while (increment < count/2):
        if (width % (count+increment) == 0):
            return (count+increment)
        if (width % (count-increment) == 0):
            return (count-increment)
        increment += 1

import random

def get_random_theme_color(color_array):
    random_index = get_random(len(color_array)-1)
    print('in get_random_theme_color', random_index, ' index in ', color_array)
    return color_array[random_index]

def get_random_rgb_color(bg = False):
    #bg is true, labeled as background choice black or white
    if bg:
        b_or_w = get_random(2)
        if b_or_w == 1:
            return '0,0,0'
        else:
            return '255,255,255'
    r = get_random(255)
    g = get_random(255)
    b = get_random(255)
    return f'{r},{g},{b}'

def get_random_color_theme(color_choice, color_count):
    # color_choice (1=random, 2=theme)
    match(color_choice):
        case 1:
            # import themes array
            from .Themes.themes import themes_array
            print('in get_random_color_theme choice =1')
            # choose array from master
            chosen_theme = themes_array[get_random(len(themes_array))]
            return chosen_theme
        case 2:
            print('in get_random_color_theme choice =2')
            chosen_theme = []
            while_index = 0
            while while_index < color_count:
                if while_index == 0:
                    chosen_color = get_random_rgb_color(True)
                else:
                    chosen_color = get_random_rgb_color()
                chosen_theme.append(chosen_color)
                print(chosen_color, while_index, 'chosen color appended to array', chosen_theme)
                while_index += 1
            return chosen_theme   
        case _:
            print('Out of scope')

    


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

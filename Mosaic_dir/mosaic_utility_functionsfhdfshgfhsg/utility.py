def find_closest_box_count(width, count):
    increment = 0
    while (increment < count/2):
        print(width, count, increment)
        if (width % (count+increment) == 0):
            return (count+increment)
        if (width % (count-increment) == 0):
            return (count-increment)
        increment += 1

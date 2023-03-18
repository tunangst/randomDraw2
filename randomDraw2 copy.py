class randomDraw2():
    def __init__(self, img_count = 1, width = 2560, height = 1440 , location = '~/Pictures/randomDraw2'):
        self.image_count = img_count
        self.width = width
        self.height = height
        self.image_file_directory = location


    def set_image_count(self,count):
        self.image_count = count
    def set_image_size(self,width, height):
        self.width = width
        self.height = height
    def set_image_destination(self,location):
        self.image_file_directory = location
    def start():
        print('Starting to draw')

test = randomDraw2()
print(test.image_count)
test.set_image_count(5)
print(test.image_count)
print(test.width)
print(test.height)
test.set_image_size(1920,1080)
print(test.width)
print(test.height)
print(test.image_file_directory)
    
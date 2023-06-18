from PIL import Image
from itertools import chain
import math


def change_whole_rose_color(img, width, height):
    new_img1 = img.copy()
    for i in range (0, width):
        for j in range (0, height):
            data = new_img1.getpixel( (i,j) )
            if (data != (255,255,255)):
                new_img1.putpixel ( (i,j), (0, 0, 0) )

    new_img1.save("images/1_black_rose.jpg", "JPEG")
    new_img1.show()

def change_petals_color(img, width, height):
    new_img2 = img.copy()
    for i in range (0, width):
        for j in range (0, height):
            r,g,b = new_img2.getpixel( (i,j) )
            if (r > g and r > b):
                new_img2.putpixel ( (i,j), (0,92,252) )

    new_img2.save("images/1_blue_rose.jpg", "JPEG")
    new_img2.show()

def remove_leaves(img, width, height):
    new_img3 = img.copy()
    x_center = math.floor(width/2)
    custom_range = chain(range(x_center - 30), range(x_center + 30, width))
    for i in custom_range:
        for j in range (0, height):
            r,g,b = new_img3.getpixel( (i,j) )
            if (g > r and g > b):
                new_img3.putpixel ( (i,j), (255,255,255) )

    new_img3.save("images/1_rose_no_leaves.jpg", "JPEG")
    new_img3.show()


def main():
    img = Image.open("images/rose2.jpg")
    width, height = img.size

    change_whole_rose_color(img=img, width=width, height=height)
    change_petals_color(img=img, width=width, height=height)
    remove_leaves(img=img, width=width, height=height)


main()

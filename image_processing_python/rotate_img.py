from PIL import Image
import math

img = Image.open("images/clover.jpg")

angle = int(input("Enter the angle by which to rotate the image: "))
rad = math.radians(angle)
cos = math.cos(rad)
sin = math.sin(rad)

width, height = img.size
new_width = round(abs(width*cos) + abs(height*sin))
new_height = round(abs(height*cos) + abs(width*sin))
rotated_img = Image.new(mode=img.mode, size=(new_width, new_height))

x_center = math.floor(width/2)
y_center = math.floor(height/2)
new_x_center = math.floor(new_width/2)
new_y_center = math.floor(new_height/2)

for i in range(height):
    for j in range(width):
        x =  j - x_center
        y = y_center - i

        new_x = round(x*cos + -y*sin)
        new_y = round(x*sin + y*cos)

        col = new_x_center - new_x
        row = new_y_center - new_y

        if (0 <= col < new_width and 0 <= row < new_height):
            rotated_img.putpixel((col, row), img.getpixel((j, i)))

rotated_img.save(f"images/rotated_{angle}_deg.jpg", "JPEG")
rotated_img.show()

from PIL import Image

img = Image.open("images/luffy.jpg")
mult = 3
width = img.size[0] * mult
height = img.size[1] * mult
enlarged_img = Image.new(mode=img.mode, size=(width, height))

for i in range (width):
    for j in range (height):
        data = img.getpixel( (i/mult,j/mult) ) 
        enlarged_img.putpixel ( (i,j), data )
        
enlarged_img.save("images/enlarged.jpg", "JPEG")
enlarged_img.show()


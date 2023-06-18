from PIL import Image

def shrink_get_one_pixel(width, height, n, img):
    shrinked_img1 = Image.new(mode=img.mode, size=(width, height))
    for i in range (width):
        for j in range (height):
            data = img.getpixel( (i * n, j * n) ) 
            shrinked_img1.putpixel ( (i,j), data )
            
    shrinked_img1.save("images/shrinked1.jpg", "JPEG")
    shrinked_img1.show()

def shrink_get_average(width, height, n, img):
    shrinked_img2 = Image.new(mode=img.mode, size=(width, height))

    for i in range (width):
        for j in range (height):
            x = i * n
            y = j * n
            tl = img.getpixel( (x, y) )
            tr = img.getpixel( (x + 1, y) )
            bl = img.getpixel( (x, y + 1) )
            br = img.getpixel( (x+1, y+1) )
            data = (int((tl[0] + tr[0] + bl[0] + br [0]) / 4), int((tl[1] + tr[1] + bl[1] + br [1]) / 4), int((tl[2] + tr[2] + bl[2] + br [2]) / 4))
            shrinked_img2.putpixel ( (i,j), data )     
            
    shrinked_img2.save("images/shrinked2.jpg", "JPEG")
    shrinked_img2.show()



def shrink_remove_odd_col(width, height, n, img):
    shrinked_img3 = Image.new(mode=img.mode, size=(width, height))
    for i in range (width):
        for j in range (height):
            data = img.getpixel( (i * n, j) ) 
            shrinked_img3.putpixel ( (i,j), data )

    shrinked_img3.save("images/shrinked3.jpg", "JPEG")
    shrinked_img3.show()

def shrink_remove_odd_row(width, height, n, img):
    shrinked_img4 = Image.new(mode=img.mode, size=(width, height))
    for i in range (width):
        for j in range (height):
            data = img.getpixel( (i, j*n) ) 
            shrinked_img4.putpixel ( (i,j), data )

    shrinked_img4.save("images/shrinked4.jpg", "JPEG")
    shrinked_img4.show()

def main():
    img = Image.open("images/luffy.jpg")
    n = 2
    width = int(img.size[0] / n)
    height = int(img.size[1] / n)
   

    shrink_get_one_pixel(width, height, n, img)
    shrink_get_average(width, height, n, img)
    shrink_remove_odd_col(width, img.size[1], n, img)
    shrink_remove_odd_row(img.size[0], height, n, img)

main()


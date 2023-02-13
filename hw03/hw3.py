# Name: Kai Francis
# Assignment: Homework 3
# Date: 9/28/21

# Leave this import here
import media


# Write your functions here
width = 700
height = 450
newpic = media.makeEmptyPicture(width, height)

#PART ONE
def upper_colors(x1, x2, pic, color):
    #setting a for in statement to target the range of x for the colors to be applied to the canvas for the longer blocks
    for x in range (x1, x2, 1):
        for y in range(0, 400, 1):
            pixel = media.getPixel(newpic, x, y)
            media.setColor(pixel, color)
        
    return newpic


def lower_colors(x1, x2, pic, color):
    #setting a for in statement to target the range of x for the colors to be applied to the canvas for the shorter blocks
    for x in range (x1, x2, 1):
        for y in range(400, 450, 1):
            pixel = media.getPixel(newpic, x, y)
            media.setColor(pixel, color)
        
    return newpic


#PART TWO
def mirror_half(picture):
    new_pix = media.duplicatePicture(picture)
    pixels = media.getPixels(new_pix) 
    
    # We will use this variable to keep track of where
    #   we want to copy our pixel data in the list.
    # We start by targeting the first pixel in the list 
    target = 0
    
    # We will make a range from 0 (the index of the first
    #   pixel in the list) up to the middle pixel index. 
    for index in range(len(pixels) - 1, len(pixels)//2, -1):
        source_pixel = pixels[index]
        source_color = media.getColor(source_pixel)
        target_pixel = pixels[target]
        media.setColor(target_pixel,source_color) 
        
        # We reduce our target index by one to move
        #   forward in the list. 
        target = target + 1 
        
    return new_pix


# Call your functions here
picture = upper_colors(0, 100, newpic, media.white)
picture = upper_colors(100, 200, newpic, media.yellow)
picture = upper_colors(200, 300, newpic, media.cyan)
picture = upper_colors(300, 400, newpic, media.green)
picture = upper_colors(400, 500, newpic, media.magenta)
picture = upper_colors(500, 600, newpic, media.red)
picture = upper_colors(600, 700, newpic, media.blue)

#calling the function for the lower colors
picture = lower_colors(0, 100, newpic, media.blue)
picture = lower_colors(100, 200, newpic, media.black)
picture = lower_colors(200, 300, newpic, media.magenta)
picture = lower_colors(300, 400, newpic, media.black)
picture = lower_colors(400, 500, newpic, media.cyan)
picture = lower_colors(500, 600, newpic, media.black)
picture = lower_colors(600, 700, newpic, media.gray)

media.show (picture)

media.writePictureTo(picture,'color_test.jpg')

#calling the modified picture to show with the mirrored effect
modified_picture = mirror_half(picture)
media.show(modified_picture)
media.writePictureTo(picture,'color_test_mirror.jpg')
# DO NOT REMOVE media.quit()
#   DO NOT WRITE CODE AFTER media.quit()
media.quit()
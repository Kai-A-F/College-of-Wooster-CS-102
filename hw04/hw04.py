import media

filename = 'astronaut.jpg'
picture = media.makePicture(filename)

#### Create your super neato functions here! ####
def switch_colors(picture):
    picture = media.makePicture(filename)
    new_pic = media.duplicatePicture(picture)
    
    for pixel in media.getPixels(new_pic):
        Red = media.getRed(pixel)
        Green = media.getGreen(pixel)
        Blue = media.getBlue(pixel)
        
        # Change the red channel value
        media.setRed(pixel,Green)
        media.setBlue(pixel,Red)
        media.setGreen(pixel,Blue)
        
    # Return my edited picture    
    return new_pic

def weighted_gray_scale(picture):
    new_pics = media.duplicatePicture(picture)
    
    for pixel in media.getPixels(new_pics): 
        # We reduce each channel by a weighted value
        #    the total of all weights is 1
        #    models the way the human eye perceives
        #    brightness. 
        new_red = media.getRed(pixel) * 0.229
        new_green = media.getGreen(pixel) * 0.587
        new_blue = media.getBlue(pixel) * 0.114
        intensity = new_red + new_green + new_blue
        media.setColor(pixel, media.makeColor(intensity, intensity, intensity))
        
    return new_pics

def quarters(picture):
    pix = media.duplicatePicture(picture)
    
    width = media.getWidth(pix)
    height = media.getHeight(pix)
    
    for px in media.getPixels(pix):
        x = media.getX(px)
        y = media.getY(px)
        
        # Top left quadrant
        if 0 <= x <= width//2 and 0 <= y <= height//2:
            media.setRed(px, media.getRed(px) * .5)
        # Top right quadrant
        elif width//2 <= x <= width - 1 and 0 <= y <= height//2:
            media.setGreen(px, media.getGreen(px) * .5)
        # Bottom left quadrant
        elif 0 <= x <= width//2 and height//2 <= y <= height - 1:
            media.setBlue(px, media.getBlue(px) * .5)
        # Bottom right (the rest) quadrant
        else:
            lum = media.getRed(px) + media.getGreen(px) + media.getBlue(px)
            lum = lum // 3
            media.setColor(px, media.makeColor(lum, lum, lum))

    return pix

def mirror_half(picture):
    new_pix = media.duplicatePicture(picture)
    pixels = media.getPixels(new_pix) 
    
    # We will use this variable to keep track of where
    #   we want to copy our pixel data in the list.
    # We start by targeting the last pixel in the list 
    target = len(pixels) - 1 
    
    # We will make a range from 0 (the index of the first
    #   pixel in the list) up to the middle pixel index. 
    for index in range(len(pixels)//2):
        source_pixel = pixels[index]
        source_color = media.getColor(source_pixel)
        target_pixel = pixels[target]
        media.setColor(target_pixel,source_color) 
        
        # We reduce our target index by one to move
        #   backward in the list (towards the 0 index). 
        target = target - 1 
        
    return new_pix
# # # #
def collage(picture):
    src = media.makePicture('astronaut.jpg')
    canvas = media.makeEmptyPicture(1000,1000)
    targetX = 0
    for sourceX in range(0, media.getWidth(src)):
        targetY = 0
        for sourceY in range(0, media.getHeight(src)):
            color = media.getColor(media.getPixel(src,sourceX,sourceY))
            media.setColor(media.getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    media.show(canvas)
    src = media.makePicture('quart_astro.jpg')
    targetX = 100
    for sourceX in range(0, media.getWidth(src)):
        targetY = 100
        for sourceY in range(0, media.getHeight(src)):
            color = media.getColor(media.getPixel(src,sourceX,sourceY))
            media.setColor(media.getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    media.show(canvas)
    src = media.makePicture('green_astro.jpg')
    targetX = 200
    for sourceX in range(0, media.getWidth(src)):
        targetY = 200
        for sourceY in range(0, media.getHeight(src)):
            color = media.getColor(media.getPixel(src,sourceX,sourceY))
            media.setColor(media.getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    media.show(canvas)
    src = media.makePicture('grayastro.jpg')
    targetX = 150
    for sourceX in range(0, media.getWidth(src)):
        targetY = 300
        for sourceY in range(0, media.getHeight(src)):
            color = media.getColor(media.getPixel(src,sourceX,sourceY))
            media.setColor(media.getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    media.show(canvas)
    src = media.makePicture('mirrored_astro.jpg')
    targetX = 0
    for sourceX in range(0, media.getWidth(src)):
        targetY = 400
        for sourceY in range(0, media.getHeight(src)):
            color = media.getColor(media.getPixel(src,sourceX,sourceY))
            media.setColor(media.getPixel(canvas,targetX,targetY),color)
            targetY = targetY + 1
        targetX = targetX + 1
    media.show(canvas)
    return canvas
    
    
# Open your image(s)

edit = (switch_colors(filename))
media.writePictureTo(edit, 'green_astro.jpg')
# # # #
edit = (weighted_gray_scale(picture))
media.writePictureTo(edit, 'grayastro.jpg')
# # # # 
edit = (quarters(picture))
media.writePictureTo(edit, 'quart_astro.jpg')
# # # #
edit = mirror_half(picture)
media.writePictureTo(edit, 'mirrored_astro.jpg')
# # # #
collage = collage(edit)
# # Output the canvas to an image file with media.writePictureTo()
final = media.writePictureTo(edit,"collage.jpg")
# Clean up media content
media.quit()
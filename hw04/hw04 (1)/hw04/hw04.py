import media

#### Create your super neato functions here! ####
def quarters(pix):
    pix = media.duplicatePicture(filename)
    
    width = media.getWidth(filename)
    height = media.getHeight(filename)
    
    for px in media.getPixels(pix):
        x = media.getX(px)
        y = media.getY(px)
        
        
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

# Open your image(s)
filename = media.makePicture('red-lips.jpg')

# Create a canvas
# edit1 = quarters(filename)
media.show(quarters(filename))

# Run your functions and place the resulting image on your canvas

# Output the canvas to an image file with media.writePictureTo()

# Clean up media content
media.quit()
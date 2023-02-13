import media

width = 700
height = 450
newpic = media.makenewpicPicture(width, height)

def green_screen(newpic):
    px= media.getPixels(newpic)
    for px in media.getPixels(newpic):
        media.getGreen
    return newpic

media.show(green_screen(newpic))

media.quit()
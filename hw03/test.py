import media

filename ='color_test.jpg'
picture = media.makePicture(filename)



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


#filename ='media_fine.png'
#picture = media.makePicture(filename)


modified = mirror_half(picture)
media.show(modified)


media.quit()
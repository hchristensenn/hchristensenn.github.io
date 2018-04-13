import os.path
import numpy as np
import PIL
import PIL.ImageEnhance

def resize(original_image, directory=None):
    img = original_image.resize((original_image.width // 5, original_image.height // 5))
    return img
    
def enhance(original_image, directory=None):
    enhancer = PIL.ImageEnhance.Color(original_image)
    img=enhancer.enhance(2)
    return img

def brightness(original_image, directory=None):
    enhancer = PIL.ImageEnhance.Brightness(original_image)
    img=enhancer.enhance(1.1)
    return img

def make_gray(original_image, directory=None): 
    img2 = np.array(original_image) 
    width, height = original_image.size 
    for row in range(height):
        for column in range(width):
            pxl=sum(img2[row][column])/3
            img2[row][column] = [pxl, pxl, pxl]
    return img2

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = []
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
def filter_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are resized, color enhanced, and brightened.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        new_image = resize(image_list[n])
        new_image = enhance(new_image)
        new_image = brightness(new_image)
        new_image = make_gray(new_image)
        new_image_filename = os.path.join(new_directory, filename)
        print new_image_filename
        img3 = PIL.Image.fromarray(new_image)
        img3.save(new_image_filename)
        

filter_all_images(directory = "C:\\Users\\hssteam\\Desktop\\hanna\\final_project_images")
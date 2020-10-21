# cropper.py

from PIL import Image
from pathlib import Path

def cropconv(img_path, pixel_values:tuple=None, percent_reduction:int=0):
    '''
    Helps in type cropping of images to a smaller size

    
    Args:
    img_path - List of paths
    pixel_values - String j2p or p2j

    Returns:
    mod_image - ndarray
    '''
    for path in img_path:

        img = Image.open(path)
        x, y = Image.open(path).size

        if percent_reduction > 0:
            
            x, y = x*(percent_reduction/100), y*(percent_reduction/100)
            pixel_values = (x-x/2, y-y/2, x+x/2, y+y/2)

        else:
            if pixel_values[0] > x or pixel_values[2] > x:
                print(f'Wrong values for x, image_size should be in range {x,y}')

            elif pixel_values[1] > y or pixel_values[3] > y:
                print(f'Wrong values for y, image_size should be in range {x,y}')

        new_img = img.crop(box=pixel_values)
        return new_img

if __name__ == '__main__':
    print('running this command typeconv line code')

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('image_list',
                        type=list,
                        help='List of Path of images that needs to be processed')
    

    parser.add_argument('operation',
                        type=str,
                        help='Type of operation that is performed')
    
    args = parser.parse_args()

    if args.code = 

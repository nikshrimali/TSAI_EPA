# cropper.py

from PIL import Image
from pathlib import Path
import argparse

def cropconv(img_path:list, pixel_values:tuple=None, percent_reduction:int=0)-> list:
    '''
    Helps in type cropping of images to a smaller size

    
    Args:
    img_path - List of paths
    pixel_values - String j2p or p2j

    Returns:
    mod_image - ndarray
    '''
    converted = []
    not_converted = []

    for path in img_path:
        try:
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
            new_img.save(path)
            converted.append(path)
        
        except Exception as e:
            print(e)
            not_converted.append(path)

    return converted, not_converted


if __name__ == '__main__':
    print('running this command typeconv line code')

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-f',
                        type=str,
                        help='List of Path of images that needs to be processed')
    

    parser.add_argument('-r',
                        type=str,
                        help='Type of operation that is performed')

    parser.add_argument('-v',
                        type=str,
                        help='Number by which the images are to be reduced')
    
    args = parser.parse_args()
    print(args)

    file_list = args.f.split(',')

    if args.r == 'crp_px':
        pixel_values = tuple([int(i) for i in args.v.split(',')])
        converted, not_converted = cropconv(img_path=file_list, pixel_values=pixel_values)

    elif args.r == 'crp_p':
        converted, not_converted = cropconv(img_path=file_list, percent_reduction=int(args.v))

    else:
        print('Only res_p or res_w arguments are supported')
    
    print(f'Images Converted {converted}')
    print(f'Images not converted {not_converted}')

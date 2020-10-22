# resize.py

from PIL import Image
from pathlib import Path
import time, os
import argparse

def reshaper(img_path:list, percent_reduction:int=0, height:int=0, width:int=0):
    '''
    Helps in type reshaping of images to a smaller size

    Args:
    img_path - List of paths
    pixel_values - String j2p or p2j

    Returns:
    mod_image - images
    '''
    converted = []
    not_converted = []

    for path in img_path:
        try:
            img = Image.open(path)
            x, y = Image.open(path).size

            if percent_reduction in range(1,101):
                reduction = percent_reduction

            elif width in range(1,x+1):
                print('w', x)
                reduction = width/x*100

            elif height in range(1,y+1):

                reduction = height/y*100

            else:
                raise ValueError('Wrong Values provided for reshaping Select integer values for height or width or percent value for percent_reduction')

            x, y = int(x*(reduction/100)), int(y*(reduction/100))
            print(f'reduced by {reduction} - New x {x} y {y}')
            new_img = img.resize(size=(x,y))
            new_img.save(path)
            converted.append(path)
            
        except Exception as e:
            print('Exception encountered', e)
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
                        type=int,
                        help='Number by which the images are to be reduced')
    
    
    
    args = parser.parse_args()
    print(args)

    file_list = args.f.split(',')

    if args.r == 'res_p':
        converted, not_converted = reshaper(img_path=file_list, percent_reduction= args.v)

    elif args.r == 'res_w':
        converted, not_converted = reshaper(img_path=file_list, width= args.v)
    
    elif args.r == 'res_h':
        converted, not_converted = reshaper(img_path=file_list, height= args.v)

    else:
        print('Only res_p or res_w arguments are supported')
    
    print(f'Images Converted {converted}')
    print(f'Images not converted {not_converted}')
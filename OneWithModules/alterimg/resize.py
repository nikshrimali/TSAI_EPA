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
                # print('Height smaller than 800 y is ==', y)
                img.save(os.path.join(r'D:\Python Projects\abc', (str(round(time.time()*1000)) +'.jpg')))
                raise ValueError('Wrong Values provided for reshaping Select integer values for height or width or percent value for percent_reduction')

            x, y = int(x*(reduction/100)), int(y*(reduction/100))
            print(f'reduced by {reduction} - New x {x} y {y}')
            new_img = img.resize(size=(x,y))
            # print('ni',new_img)
            new_img.save(os.path.join(r'D:\Python Projects\abc', (str(round(time.time()*1000)) +'.jpg')))
            # return new_img
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print('running this command typeconv line code')

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('image_list',
                        type=list,
                        help='List of Path of images that needs to be processed')
    

    parser.add_argument('operation',
                        type=str,
                        help='Type of operation that is performed')
    
    parser.add_argument('value',
                        type=int,
                        help='Number by which the images are to be reduced')
    
    args = parser.parse_args()

    if args.code == 'res_p':
        reshaper(img_path=args.image_list, percent_reduction= args.value)
    
    elif args.code == 'res_w':
        reshaper(img_path=args.image_list, width= args.value)
    
    elif args.code == 'res_h':
        reshaper(img_path=args.image_list, height= args.value)




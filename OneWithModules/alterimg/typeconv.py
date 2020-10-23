# typeconv.py

from PIL import Image
from pathlib import Path
import argparse
import os
def typeconv(img_path:list, type:str='j2p')-> list:
    '''
    Helps in type conversion of images from jpeg to png or png to jpeg
    
    Args:
    img_path - List of paths
    type - String j2p or p2j

    Returns:
    mod_image - ndarray
    '''
    #Images path

    converted = []
    not_converted = []
    try:
        for path in img_path:
            print('path ',path)
            if type == 'j2p':
                new_path = changeextn(path, '.png')
                save_new_img(path, new_path)
                
            elif type == 'p2j':
                new_path = changeextn(path, '.jpg')
                save_new_img(path, new_path)
                
            else:
                raise ValueError('Type can be only j2p or p2j')

            converted.append(path)

    except Exception as e:
        print(e)
        not_converted.append(path)

    return converted, not_converted

    
def save_new_img(oldpath, newpath):
    '''Takes the image at old path and replace it with
     image with new extension
     
     Args:
     oldpath - str
     newpath - str
     '''
    img = Image.open(oldpath)
    img.save(newpath)


def changeextn(imgpath, new_ext):
    '''Changes the extension of the image to the new path
    Args:
    imgpath: String
    new_ext - String
    '''
    filename = Path(imgpath)
    return filename.with_suffix(new_ext)


if __name__ == '__main__':
    print('running this command typeconv line code')

    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-f',
                        type=str,
                        help='List of Path of images that needs to be processed')
    

    parser.add_argument('-r',
                        type=str,
                        help='Type of operation that is performed')
    
    
    args = parser.parse_args()

    file_list = args.f.split(',')
    print(file_list)

    if args.r == 'j2p':
        converted, not_converted = typeconv(img_path=file_list, type= args.r)

    
    elif args.r == 'p2j':
        converted, not_converted = typeconv(img_path=file_list, type= args.r)

    else:
        print('Only res_p or res_w arguments are supported')
    
    print(f'Images Converted {converted}')
    print(f'Images not converted {not_converted}')

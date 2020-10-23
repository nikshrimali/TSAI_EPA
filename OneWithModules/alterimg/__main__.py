# a main module that exposes all these features (using argparse)
# finally create an zipped app, that exposes all of these features
# each module must be independently available and tested (write test to check whether you can call them from command line)
# each feature must be available via argument selection
# images must not be required to be in the same folder where your code is
import argparse
from typeconv import *
from resize import *
from cropper import *



if __name__ == '__main__':
    print('running this command Image Alterimg line code')

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f',
                        type=str,
                        help='List of Path of images that needs to be processed')
    

    parser.add_argument('-r',
                        type=str,
                        help='Type of operation that is performed')

    parser.add_argument('-v',
                        type=str,
                        help='Magnitude/Value of the operation performed on the images')
    
    args = parser.parse_args()
    print(args)
    file_list = args.f.split(',')

    if args.r == 'crp_px':
        pixel_values = tuple([int(i) for i in args.v.split(',')])
        converted, not_converted = cropconv(img_path=file_list, pixel_values=pixel_values)

    elif args.r == 'crp_p':
        converted, not_converted = cropconv(img_path=file_list, percent_reduction=int(args.v))

    elif args.r == 'res_p':
        converted, not_converted = reshaper(img_path=file_list, percent_reduction=int(args.v))

    elif args.r == 'res_w':
        converted, not_converted = reshaper(img_path=file_list, width=int(args.v))
    
    elif args.r == 'res_h':
        converted, not_converted = reshaper(img_path=file_list, height=int(args.v))
    
    elif args.r == 'j2p':
        converted, not_converted = typeconv(img_path=file_list, type=args.r)

    elif args.r == 'p2j':
        converted, not_converted = typeconv(img_path=file_list, type=args.r)

    else:
        print('Only res_p or res_w arguments are supported')
    
    print(f'Images Converted {converted}')
    print(f'Images not converted {not_converted}')

    

    
    

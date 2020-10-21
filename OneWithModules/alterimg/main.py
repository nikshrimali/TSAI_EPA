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

    
    

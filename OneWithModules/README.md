# Create these modules:
- jpg/jpeg to png conversion (use PIL library) j2p
- png to jpg conversion (use PIL library) p2j
- image resizer that can resize bulk images with these features:
- resize by user determined percentage (say 50% for height and width) (proportional) res_p
- resize by user determined width (proportional) res_w
- resize by user determined height (proportional) res_h
- image cropper that can crop bulk images with these features:
- center square/rectangle crop by user-determined pixels crp_px
- centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
- it let's user know which all images were not cropped due to size mismatches
- a __main__ module that exposes all these features (using argparse)
- finally create an zipped app, that exposes all of these features

## How to test your code:
- each module must be independently available and tested (write test to check whether you can call them from command line) 
- each feature must be available via argument selection
- images must not be required to be in the same folder where your code is

## final test:
- download 20 jpeg images of size more than 1000x1000
- convert to png
- convert to jpg
- resize to 80%
- resize to 500 width
- resize to 500 height
- all this using your zipped app
- center crop to 224x224
- You must have at least 20+ test. (github actions)
- Each test is worth 50 points (no additional points for more tests). So total 1000 pts.
Failing test, reduces mark.
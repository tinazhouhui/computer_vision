from sys import argv

# list of all the possible transformations
from image_processing.convo import create_transformed_outputs
from router import router

actions = {'blend': 'blending two images together (using addWeighted)',
           'bitwise-operations': 'creates a logo that is inserted to a picture',
           'convolution': 'will run all available convolutions',
           'gamma-correction': 'gamma adjustment via linear stretching',
           'coin-detection': 'compares outputs of manual and Hough detection of circles (coins)',
           'edge-detection': 'traces the edges of the image'
           }

if len(argv) > 1: #checks for argument inputed in console
    if argv[1] not in actions:
        print('Argument does not exist, please choose an existing argument from the list below:\n')
        for action, description in actions.items():
            print("\u2022\033[1m " + action + '\033[0m - ' + description)

    router(argv[1])()

else:
    print('\nPlease add an argument behind "start.py" from the list below:\n')
    for action, description in actions.items():
        print("\u2022\033[1m " + action + '\033[0m - ' + description)


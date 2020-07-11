from sys import argv

# list of all the possible transformations
actions = {'draw': 'basic manipulation with images',
           'blend': 'blending two images together (addWeighted)',
           'bitwise-operations': 'bitwise operations',
           'convolution': 'convolution and kernel',
           'gamma-correction': 'gamma adjustment via linear stretching',
           'coin-recognition': 'identify coins',
           }

if len(argv) > 1: #checks for argument inputed in console
    if argv[1] not in actions:
        print('Argument does not exist, please choose an existing argument from the list below:\n')
        for action, description in actions.items():
            print("\u2022\033[1m " + action + '\033[0m - ' + description)
else:
    print('\nPlease add an argument behind "start.py" from the list below:\n')
    for action, description in actions.items():
        print("\u2022\033[1m " + action + '\033[0m - ' + description)
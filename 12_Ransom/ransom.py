#!/usr/bin/env python3
"""Ransom note"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')#The text argument is a positional string value

    parser.add_argument('-s', #The --seed option is an integer that defaults to None.
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args() #Process the command-line arguments into the args variable.

    if os.path.isfile(args.text):#If the args.text is a file, use the contents of that as the new Return the arguments args.text value.
        args.text = open(args.text).read().rstrip()

    return args #Return the arguments args.text value. to the caller.


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed) #Set the random.seed() to the given args.seed value. The default is None, which is the same as not setting it. That means the program will appear random when no seed is given but will be testable when we do provide a seed value.

    # Method 7: map
    print(''.join(map(choose, args.text)))


# --------------------------------------------------
def choose(char): #Define a function to randomly return the upper- or lowercase version of a given character.
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if random.choice([0, 1]) else char.lower() #Use random.choice() to select either 0 or 1, which, in the Boolean context of the if expression, evaluates to False or True, respectively.


# --------------------------------------------------
def test_choose(): #Define a test_choose() function that will be run by Pytest. The function takes no arguments
    """Test choose"""

    state = random.getstate() #Save the current state of the random module.
    random.seed(1) #Set the random.seed() to a known value for the purposes of the test.
    assert choose('a') == 'a' #Use the assert statement to verify that we get the expected result from the choose() for a known argument
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state) #Reset the random module’s state so that our changes won’t affect any other part of the program


# --------------------------------------------------
if __name__ == '__main__':
    main()

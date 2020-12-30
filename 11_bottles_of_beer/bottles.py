#!/usr/bin/env python3
"""Bottles of beer song"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', #Define the --num argument as an int with a default value of 10.
                        '--num',
                        metavar='number',
                        type=int,
                        default=10,
                        help='How many bottles')

    args = parser.parse_args() #Parse the commandline argument into the variable args

    if args.num < 1: #If args.num is less than 1, use parser.error() to display an error message and exit the program with an error value.
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1)))) #The map() function expects a function as the first argument and some iterable as the second argument. Here I feed the descending numbers from the range() function to my verse() function. The result from map() is a new list of verses that can be joined on two newlines.


# --------------------------------------------------
def verse(bottle):#Define a function that can create a single verse().
    """Sing a verse"""

    next_bottle = bottle - 1 #Define a next_bottle that is one less than the current bottle.
    s1 = '' if bottle == 1 else 's' #Define an s1 (the first “s”) that is either the character 's' or the empty string, depending on the value of current bottle.
    s2 = '' if next_bottle == 1 else 's'#Do the same for s2 (the second “s”), depending on the value of next_bottle.
    num_next = 'No more' if next_bottle == 0 else next_bottle #Define a value for next_num depending on whether the next value is 0 or not.
    return '\n'.join([ #Create a return string by joining the four lines of text on the newline. Substitute in the variables to create the correct verse.
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{num_next} bottle{s2} of beer on the wall!',
    ])


# --------------------------------------------------
def test_verse():#Define a unit test called test_verse() for the verse() function. The test_ prefix means that the pytest module will find this function and execute it.
    """Test verse"""

    last_verse = verse(1) #Test the last verse() with the value 1.
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2) #Test a verse() with the value 2.
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()

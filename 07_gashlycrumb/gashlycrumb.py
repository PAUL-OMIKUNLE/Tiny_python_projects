#!/usr/bin/env python3
"""Interactive Gashlycrumb"""

import argparse


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    

    parser = argparse.ArgumentParser(
        description='Interactive Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter) #thiswould help us figure out all hearguments

    parser.add_argument('-f',         #telling the parser to expect use a file arguments to be used 
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'), #file type type argument to be used ithe main
                        default='gashlycrumb.txt') #making use of the text file

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args() #et the file arguments above
    lookup = {line[0]: line.rstrip() for line in args.file} #a key value to look up the first letter in each line and the 'strip it to each sentence' in the file argument

    while True:
        letter = input('Please provide a letter [! to quit]: ') #input a letter

        if letter == '!': #input ! to leave
            print('Bye')
            break

        print(lookup.get(letter.upper(), f'I do not know "{letter}".')) #to get number in upper case if not program returns i do not know the number


# --------------------------------------------------
if __name__ == '__main__': #to identify  the module, so it can be applied to the main, 
    main()

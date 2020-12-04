#!/usr/bin/env python3 
"""Apples and Bananas"""

import argparse
import os
import re


# --------------------------------------------------
def get_args(): #defining our arguments (get_args)
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)#defining our parser so we can state arguments to be used

    parser.add_argument('text', metavar='text', help='Input text or file') #argument for text usage

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou')) #argument for vowel usage

    args = parser.parse_args()

    if os.path.isfile(args.text):  #check if the text argument is a file argument 
        args.text = open(args.text).read().rstrip() #if it is, read the file using thr rsrtip() to remove trailing whitespace

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    text = re.sub('[aeiou]', vowel, text) #substitute any of the lowercase vowels (lowercase because of the restrictions in get_args())
    text = re.sub('[AEIOU]', vowel.upper(), text)#substituteany of the uppercase with uppecase vowel
    print(text)  


# --------------------------------------------------
if __name__ == '__main__': #to identify  the module, so it can be applied to the main, 
    main() 

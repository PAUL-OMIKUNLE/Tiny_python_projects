#!/usr/bin/env python3
"""Telephone"""

import argparse
import os
import random
import string #Import the string module we’ll need to select a random character.


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file') #Define a positional argument for the text. This could be either a string of text or a file that needs to be read.

    parser.add_argument('-s',   #The --seed parameter is an integer value with a default of None.
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m', #The --mutations parameter is a floating-point value with a default of 0.1.
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args() #Process the arguments from the command line. If argparse detects problems, such as non-numeric values for the seed or mutations, the program dies here and the user sees an error message. If this call succeeds, argparse has validated the arguments and converted the values

    if not 0 <= args.mutations <= 1: #If args.mutations is not in the acceptable range of 0–1, use parser.error() to halt the program and print the given message. Note the use of feedback to echo the bad args.mutation value to the user.
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):#If args.text names an existing file, read that file for the contents and overwrite the Return the processed original value of args.text.
        args.text = open(args.text).read().rstrip()

    return args #Return the processed original value of args.text. 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed) #Set the random.seed() to the value provided by the user. Remember that the default value for args.seed is None, which is the same as not setting the seed.
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation)) #Set alpha to be the characters we’ll use for replacements. The sorted() function will return a new list of the characters in the right order, and then we can use the str.join() function to turn that back into a str value.
    len_text = len(text) #Since we use len(text) more than once, we put it into a variable.
    num_mutations = round(args.mutations * len_text) #Figure the num_mutations by multiplying the mutation rate by the length of the text.
    new_text = list(text) #Make a copy of text.

    for i in random.sample(range(len_text), num_mutations): #Use random.sample () to get num_mutations indexes to change. This function returns a list that we can iterate using the for loop.
        new_text[i] = random.choicse(alpha.replace(new_text[i], ''))#Now we can directly modify a value in new_text.

    print('You said: "{}"\nI heard : "{}"'.format(text, ''.join(new_text))) #Join new_list on the empty string to make a new str.


# --------------------------------------------------
if __name__ == '__main__':
    main()

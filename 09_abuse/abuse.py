#!/usr/bin/env python3
"""Heap abuse"""

import argparse 
import random #Bring in the random module so we can call functions.


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2) #Define the parameter for the number of adjectives, setting type=int and the default value.

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3) #Similarly define the parameter for the number of insults as an integer with a default.

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None) #The random seed default should be None.
    args = parser.parse_args() #Get the result of parsing the command-line arguments. The argparse module will handle errors such as non-integer values.

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0') #Check that args.adjectives is greater than 0. 
                                                                      #If there is a problem, call parser.error() with the error message.
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0') #Similarly check args.number

    return args #At this point, all the user’s arguments have been validated, so return the arguments to the caller.


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args() #This is where the program actually begins as it is the first action inside main(). getting the arguments.
    random.seed(args.seed) #Set random.seed() using whatever value was passed by the user.

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split() #Create a list of adjectives by splitting the very long string contained in the triple quotes.

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()  #Create a list of nouns by splitting the very long string contained in the triple quotes.

    for _ in range(args.number):
        #Use the random.sample() function to select the correct number of adjectives and join them on the comma-space string.
        adjs = ', '.join(random.sample(adjectives, k=args.adjectives)) 
        print(f'You {adjs} {random.choice(nouns)}!') #Use an f-string to format the output to print().


# --------------------------------------------------
if __name__ == '__main__':
    main()

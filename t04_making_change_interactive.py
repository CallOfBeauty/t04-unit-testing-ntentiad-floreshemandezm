######################################################################
# Author: Jan Pearce and Patrick Shepherd   TODO: Change this to your names
# Username: pearcej & shepherdp             TODO: Change this to your usernames
#
# Assignment: T04: Unit Testing
#
# Purpose: This file runs the interactive mode of the making change code.
######################################################################
# Acknowledgements:
#
# Original code by: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import t04_making_change         # Notice I'm importing my own code!
                                 # If you see a syntax error here, right click your project folder,
                                 # and select "Mark Directory As..." and select "Sources Root"


def main():
    """
    Runs the interactive mode of the t5_making_change file

    :return: None
    """

    t04_making_change.user_input_of_coins()
    # Notice that the test suite does NOT run here!


main()

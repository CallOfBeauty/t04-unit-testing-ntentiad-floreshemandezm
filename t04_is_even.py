######################################################################
# Author: Jan Pearce and Patrick Shepherd   TODO: Change this to your names
# Username: pearcej & shepherdp             TODO: Change this to your usernames
#
# Assignment: T04: Unit Testing
#
# Purpose: This program is designed to demonstrate testing of the of Boolean functions
# and the modulus (%) operator which gives the remainder following a division
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys

TESTNUM = 1

def mytest(did_pass):
    """
    Print the result of a unit test.

    This function works correctly--it is verbatim from the textbook, Chapter 6.

    You should reuse this function anytime you are creating a custom test suite

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    global TESTNUM

    if did_pass:
        msg = 'Test %d Passed' % TESTNUM
    else:
        msg = 'Test %d Failed' % TESTNUM
    print(msg)

    TESTNUM += 1


def is_even_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the is_even() function (below), returning True
    only when the input is even.

    :return: None
    """
    print("\nRunning is_even_testsuite().")

    # Testing of positive integers
    mytest(is_even(1) == False)
    mytest(is_even(2) == True)
    mytest(is_even(10) == True)
    mytest(is_even(99999) == False)

    # Testing of 0 and negative integers
    mytest(is_even(0) == True)
    mytest(is_even(-1) == False)
    mytest(is_even(-2) == True)
    mytest(is_even(-11111) == False)

    # What should the is_even function do to handle this case?
    mytest(is_even(1.1) == False)

    # And these cases? (Uncomment them to see what happens)
    # testit(is_even("hi") == False)
    # testit(is_even(True) == True)

    print("Run of is_even_testsuite() complete.")


def is_even(num):
    """
    Function intended to take an integer as input. Returns True if even and False if odd

    :param num: the integer to be tested
    :return: Boolean value representing if the number is even or not
    """
    if int(num) % 2 == 0:
        return True
    else:
        return False


def main():
    """
    This main function is intended to test the correctness of the is_even function
    :return: None
    """
    is_even_testsuite()


if __name__ == "__main__":
    main()

"""

This class symbolizes an eight-sided die.
The initializer sets the sides to 8 to represent it.
The class uses its superclass' getters and setters.

The implementation of roll checks the positivity of the die
and then delegates a result.
The result depends on the generated random.randint number (from one to eight).

Negative and Positive dice have different symbol distribution probabilities,
their different match cases represent it.

Based off of possible rolls the class implements str to print results legibly.
"""

import Die
import random
from datetime import datetime

# Seed set to change with time to ensure random result generation
random.seed(datetime.now().timestamp())


class EightDieClass(Die.DieClass):
    def __init__(self, postype=False):

        # Call superclass to initialize
        # Default is Negative die
        super().__init__(postype)

        # set sides
        self.sides = 8

    def roll(self):
        """
        This function generates a random number
        and uses it to initiate the dice face symbols
        :return: int randomly generated from 1 to 8

        """
        # Generate number
        result = random.randint(1, 8)
        # DEBUG LINE print(result)
        if self.get_positive():
            # If the die is positive the distribution is:
            match result:
                case 1:
                    self.set_symbol3("Advantage")
                case 2:
                    self.set_symbol1("Success")
                case 3:
                    self.set_symbol3("Advantage")
                    self.set_isdouble(True)
                case 4:
                    self.set_symbol1("Success")
                    self.set_symbol3("Advantage")
                case 5:
                    self.set_symbol3("Advantage")
                case 6:
                    self.set_symbol3("Advantage")
                case 7:
                    self.set_symbol1("Success")
                    self.set_isdouble(True)
                case 8:
                    # Blank face
                    ...
        else:
            # If the die is negative
            match result:
                case 1:
                    self.set_symbol3("Threat")
                case 2:
                    self.set_symbol1("Failure")
                case 3:
                    self.set_symbol3("Threat")
                case 4:
                    self.set_symbol3("Threat")
                case 5:
                    self.set_symbol1("Failure")
                    self.set_isdouble(True)
                case 6:
                    self.set_symbol3("Threat")
                    self.set_isdouble(True)
                case 7:
                    self.set_symbol1("Failure")
                    self.set_symbol3("Threat")
                case 8:
                    # Blank face
                    ...

        # Return the result for testing purposes
        return result

    def __str__(self):
        """
        :return: str Human readable result of a die roll
        """
        # Printing results functionality
        result = ""
        # empty strings are False
        if bool(self.get_symbol1()) & bool(not self.get_symbol3())\
                & self.get_isdouble():
            # If the die is double 1
            result = "Double " + self.get_symbol1()
        elif bool(self.get_symbol1()) & bool(not self.get_symbol3()):
            # If the die is 1
            result = self.get_symbol1()
        elif bool(self.get_symbol1()) & bool(self.get_symbol3()):
            # If the die is 1 and 3
            result = self.get_symbol1() + " and " + self.get_symbol3()
        elif bool(self.get_symbol3()) & bool(not self.get_symbol1())\
                & self.get_isdouble():
            # If the die is double 3
            result = "Double " + self.get_symbol3()
        elif bool(self.get_symbol3()) & bool(not self.get_symbol1()):
            # If the die is 3
            result = self.get_symbol3()
        elif self.is_blank():
            # If the die rolled Blank
            result = "Blank"
        else:
            print("Printing Error")
        return result

    def cancel(self, die: Die):
        """
        Compare two opposing EightDieClass objects and print the result
        :param die: EightDieClass die to compare with
        :return: Prints result of comparison
        """

        # Try block commented out for unit testing the error
        # try:
        if die.get_sides() != 8:
            # If the dice are not of the same denomination raise error
            raise ArithmeticError

        if self.get_positive() ^ die.get_positive():
            # XOR condition, proceed only if the dice are opposite

            print("The pair is {0} vs {1} the result is: ".
                  format(self, str(die)))

            # Determine opposition results
            if bool(self.get_symbol1()) & bool(self.get_symbol3())\
                    & bool(die.get_symbol1()) & bool(die.get_symbol3()):
                print("Blank")

            # Threat and Failure vs Success and Advantage cancel to Blank
            elif die.is_blank():
                print(self)

            # Second Die is blank
            elif self.is_blank():
                print(str(die))

            # First Die is blank
            elif self.get_isdouble() & bool(self.get_symbol3())\
                    & bool(die.get_symbol1()) & bool(die.get_symbol3()):

                print("{0} and {1}".format(self.get_symbol3(),
                                           die.get_symbol1()))
            # Double Advantage vs Threat and Failure to Advantage and Failure
            elif self.get_isdouble() & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(die.get_symbol3()):

                print("{0} and {1}".format(self.get_symbol1(),
                                           die.get_symbol3()))
            # Double Success vs Threat and Failure to single Success and Threat
            elif self.get_isdouble() & bool(self.get_symbol3())\
                    & bool(die.get_symbol3()) & bool(not die.get_isdouble()):

                print(self.get_symbol3())
            # Double Advantage vs Threat to single Advantage
            elif die.get_isdouble() & bool(die.get_symbol3())\
                    & bool(self.get_symbol3()) & bool(not self.get_isdouble()):

                print(str(die.get_symbol3()))
            # Double Threat vs Advantage to single Threat
            elif die.get_isdouble() & bool(die.get_symbol3())\
                    & bool(self.get_symbol3()) & bool(self.get_symbol1()):

                print("{0} and {1}".format(self.get_symbol1(),
                                           str(die.get_symbol3())))
            # Double Threat vs Advantage and Success to Threat and Success
            elif die.get_isdouble() & bool(die.get_symbol1())\
                    & bool(self.get_symbol3()) & bool(self.get_symbol1()):

                print("{0} and {1}".format(self.get_symbol3(),
                                           str(die.get_symbol1())))
            # Double Failure vs Advantage and Success to Failure and Advantage
            elif self.get_isdouble() & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(not die.get_isdouble()):

                print(self.get_symbol1())
            # Double Success vs Failure to single Success
            elif bool(not self.get_isdouble()) & bool(self.get_symbol3())\
                    & bool(die.get_symbol3()) & die.get_isdouble():

                print(str(die.get_symbol3()))
            # Double Failure vs Success to single Failure
            elif bool(self.get_symbol3()) & bool(not self.get_symbol1())\
                    & bool(die.get_symbol3()) & bool(not die.get_symbol1()):

                print("Blank")
            # Cancels Success and Failure
            elif bool(not self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(not die.get_symbol3()) & bool(die.get_symbol1()):

                print("Blank")
            # Cancels Advantage and Threat
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol3()) & bool(die.get_symbol1()):

                print("Blank")
            # Cancels Threat and Failure with Advantage and Success
            elif self.get_isdouble() & die.get_isdouble():

                print("Blank")
            # Cancels two doubled symbols
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol3()) & bool(not die.get_symbol1()):

                print(self.get_symbol1())
            # Success and Advantage vs Failure to Advantage
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(not die.get_symbol3()) & bool(die.get_symbol1()):

                print(self.get_symbol3())
            # Success and Advantage vs Threat to Success
            elif bool(die.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(not self.get_symbol1()) & bool(
                    self.get_symbol3()):

                print(die.get_symbol1())
            # Threat and Failure vs Advantage to Failure
            elif bool(die.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(self.get_symbol1()) & bool(not self.get_symbol3()):

                print(die.get_symbol3())
            # Threat and Failure vs Success to Threat
            else:
                # If the symbols rolled do not oppose
                print("{0} and {1}, they don't match.".format(str(self),
                                                              str(die)))
        else:
            # If both dice are of the same type, warn
            print("The dice don't match, be sure they are opposing!")

        # Error handling
        # except ArithmeticError:
        # print("The dice have different number of faces!")

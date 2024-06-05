"""

This class symbolizes a six-sided die.
The initializer sets the sides to 6 to represent it.
The class uses its superclass' getters and setters.

The implementation of roll checks the positivity of the die
and then delegates a result.
The result depends on the generated random.randint number (from one to six).

Negative and Positive dice have different symbol distribution probabilities,
their different match cases represent it.

Based off of possible rolls the class implements str to print results legibly.
"""

import Die
import random
from datetime import datetime

# Seed set to change with time to ensure random result generation
random.seed(datetime.now().timestamp())


class SixDieClass(Die.DieClass):

    def __init__(self, postype=False):
        # Call superclass to initialize
        # Default is Negative die
        super().__init__(postype)

        # set sides
        self.sides = 6

    def roll(self):
        """
        This function generates a random number
        and uses it to initiate the dice face symbols
        :return: int randomly generated from 1 to 6
        """
        # Generate number
        result = random.randint(1, 6)
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
                case _:
                    # Cases 5 and 6 are Blank faces (Default values)
                    ...
        else:
            # If the die is negative
            match result:
                case 1:
                    self.set_symbol3("Threat")
                case 2:
                    self.set_symbol1("Failure")
                case _:
                    # All other cases are Blank (Default values)
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
        if bool(self.get_symbol1()) & bool(not self.get_symbol3()):
            # If the symbol rolled is 1
            result = self.get_symbol1()
        elif bool(self.get_symbol1()) & bool(self.get_symbol3()):
            # If the symbol rolled is both 1 and 3
            result = self.get_symbol1() + " and " + self.get_symbol3()
        elif bool(self.get_symbol3()) & bool(self.get_isdouble()):
            # If the symbol rolled is double 3 (there is no double 1 in SixDie)
            result = result + "Double " + self.get_symbol3()
        elif bool(self.get_symbol3()):
            # If the symbol rolled is 3
            result = self.get_symbol3()
        elif self.is_blank():
            # If the die rolled Blank
            result = "Blank"
        else:
            print("Printing Error")
        return result

    def cancel(self, die: Die.DieClass):
        """
        Compare two opposing SixDieClass objects and print the result
        :param die: SixDieClass die to compare with
        :return: Prints result of comparison
        """
        # Try block commented out for unit testing the error
        # try:
        if die.get_sides() != 6:
            # If the dice are not of the same denomination raise error
            raise ArithmeticError

        if self.get_positive() ^ die.get_positive():
            # XOR condition, proceed only if the dice are opposite

            print("The pair is {0} vs {1} the result is: ".
                  format(self, str(die)))

            # Determine opposition results
            if self.get_isdouble() & bool(die.get_symbol3()):
                print(self.get_symbol3())
            # Double Advantage vs Threat to single Advantage
            elif die.get_isdouble() & bool(self.get_symbol3()):
                print(die.get_symbol3())
            # Threat vs Double Advantage to single Advantage
            elif self.is_blank():
                print(die)
            # If blank print other
            elif die.is_blank():
                print(self)
            # If blank print other
            elif bool(not self.get_isdouble()) & bool(self.get_symbol3())\
                    & bool(not self.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(not die.get_symbol1()):
                print("Blank")
            # Fully opposing dice
            elif bool(not self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(not die.get_symbol3()):
                print("Blank")
            # Fully opposing dice
            elif bool(not self.get_isdouble()) & bool(self.get_symbol3())\
                    & bool(not self.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(die.get_symbol1()):
                print(die.get_symbol1())
            # Threat vs Success and Advantage to Success
            elif bool(not self.get_isdouble()) & bool(not self.get_symbol3())\
                    & bool(self.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(die.get_symbol1()):
                print(die.get_symbol3())
            # Failure vs Success and Advantage to Advantage
            elif bool(not self.get_isdouble()) & bool(self.get_symbol3())\
                    & bool(self.get_symbol1()) & bool(die.get_symbol3())\
                    & bool(not die.get_symbol1()):
                print(self.get_symbol1())
            # Success and Advantage vs Threat to Success
            elif bool(not self.get_isdouble()) & bool(self.get_symbol3())\
                    & bool(self.get_symbol1()) & bool(die.get_symbol1())\
                    & bool(not die.get_symbol3()):
                print(self.get_symbol3())
            # Success and Advantage vs Failure to Advantage
            else:
                # If the symbols rolled do not oppose
                print("{0} and {1}, they don't match.".
                      format(str(self), str(die)))
        else:
            # If both dice are of the same type, warn
            print("The dice don't match, be sure they are opposing!")

            # Error handling
            # except ArithmeticError:
            # print("The dice have different number of faces!")

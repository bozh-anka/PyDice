"""

This class symbolizes an eight-sided die.
The initializer sets the sides to 12 to represent it.
The class uses its superclass' getters and setters.

The implementation of roll checks the positivity of the die
and then delegates a result.
The result depends on the generated random.randint number (from one to twelve).

Negative and Positive dice have different symbol distribution probabilities,
their different match cases represent it.

Based off of possible rolls the class implements str to print results legibly.

"""

import Die
import random
from datetime import datetime

# Seed set to change with time to ensure random result generation
random.seed(datetime.now().timestamp())


class TwelveDieClass(Die.DieClass):
    def __init__(self, postype=False):

        # Call superclass to initialize
        # Default is Negative die
        super().__init__(postype)

        # set sides
        self.sides = 12

    def roll(self):
        """
        This function generates a random number and uses
        it to initiate the dice face symbols
        :return: int randomly generated from 1 to 12

        """
        # Generate number
        result = random.randint(1, 12)
        # DEBUG LINE print(result)
        if self.get_positive():
            # If the die is positive the distribution is:
            match result:
                case 1:
                    self.set_symbol3("Advantage")
                    self.set_isdouble(True)
                case 2:
                    self.set_symbol3("Advantage")
                    self.set_isdouble(True)
                case 3:
                    self.set_symbol3("Advantage")
                    self.set_isdouble(True)
                case 4:
                    self.set_symbol2("Triumph")
                case 5:
                    self.set_symbol1("Success")
                case 6:
                    self.set_symbol1("Success")
                    self.set_symbol3("Advantage")
                case 7:
                    self.set_symbol1("Success")
                case 8:
                    self.set_symbol1("Success")
                    self.set_symbol3("Advantage")
                case 9:
                    self.set_symbol1("Success")
                    self.set_isdouble(True)
                case 10:
                    self.set_symbol1("Success")
                    self.set_symbol3("Advantage")
                case 11:
                    self.set_symbol1("Success")
                    self.set_isdouble(True)
                case _:
                    # Blank face
                    ...
        else:
            # If the die is negative
            match result:
                case 1:
                    self.set_symbol3("Threat")
                    self.set_isdouble(True)
                case 2:
                    self.set_symbol3("Threat")
                case 3:
                    self.set_symbol3("Threat")
                    self.set_isdouble(True)
                case 4:
                    self.set_symbol3("Threat")
                case 5:
                    self.set_symbol1("Failure")
                    self.set_symbol3("Threat")
                case 6:
                    self.set_symbol1("Failure")
                case 7:
                    self.set_symbol1("Failure")
                    self.set_symbol3("Threat")
                case 8:
                    self.set_symbol1("Failure")
                case 9:
                    self.set_symbol1("Failure")
                    self.set_isdouble(True)
                case 10:
                    self.set_symbol2("Despair")
                case 11:
                    self.set_symbol1("Failure")
                    self.set_isdouble(True)
                case _:
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
                & bool(not self.get_symbol2()) & self.get_isdouble():
            # If the die is double 1
            result = "Double " + self.get_symbol1()
        elif bool(self.get_symbol1()) & bool(not self.get_symbol3()):
            # If the die is 1
            result = self.get_symbol1()
        elif bool(self.get_symbol1()) & bool(self.get_symbol3()):
            # If the die is 1 and 3
            result = self.get_symbol1() + " and " + self.get_symbol3()
        elif bool(self.get_symbol3()) & bool(not self.get_symbol1())\
                & bool(not self.get_symbol2()) & self.get_isdouble():
            # If the die is double 3
            result = "Double " + self.get_symbol3()
        elif bool(self.get_symbol3()):
            # If the die is 3
            result = self.get_symbol3()
        elif bool(self.get_symbol2()):
            # If the die is 2
            result = self.get_symbol2()
        elif self.is_blank():
            # If the die rolled Blank
            result = "Blank"
        else:
            print("Printing Error")
        return result

    def cancel(self, die: Die):
        """
        Compare two opposing SixDieClass objects and print the result
        :param die: TwelveDieClass die to compare with
        :return: Prints result of comparison
        """
        # Try block commented out for unit testing the error
        # try:
        if die.get_sides() != 12:
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
            # Opposing symbols
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

            # cancels double advantage to single advantage and failure
            elif self.get_isdouble() & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(die.get_symbol3()):
                print("{0} and {1}".format(self.get_symbol1(),
                                           die.get_symbol3()))

            # cancels double success to single success and threat
            elif self.get_isdouble() & bool(self.get_symbol3())\
                    & bool(not die.get_isdouble()) & bool(die.get_symbol3()):
                print(self.get_symbol3())

            # cancels double advantage
            elif die.get_isdouble() & bool(die.get_symbol3())\
                    & bool(self.get_symbol3()) & bool(
                    not self.get_isdouble()):
                print(str(die.get_symbol3()))

            # cancels double threat
            elif die.get_isdouble() & bool(die.get_symbol3())\
                    & bool(self.get_symbol1()) & bool(self.get_symbol3()):
                print("{0} and {1}".format(self.get_symbol1(),
                                           str(die.get_symbol3())))

            # cancels double failure to one failure and advantage
            elif die.get_isdouble() & bool(die.get_symbol1())\
                    & bool(self.get_symbol1()) & bool(self.get_symbol3()):
                print("{0} and {1}".format(self.get_symbol3(),
                                           str(die.get_symbol1())))

            # cancels double threat to one threat and success
            elif self.get_isdouble() & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(not die.get_isdouble()):
                print(self.get_symbol1())

            # cancels double success to single success
            elif die.get_isdouble() & bool(die.get_symbol1())\
                    & bool(self.get_symbol1()) & bool(not self.get_isdouble()):
                print(str(die.get_symbol1()))

            # cancels double failure to single failure
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(die.get_symbol3()):
                print("Blank")

            # Complete opposites
            elif bool(not self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(not die.get_symbol3()):
                print("Blank")

            # Complete opposites
            elif bool(self.get_symbol3()) & bool(not self.get_symbol1())\
                    & bool(not die.get_symbol1()) & bool(
                    die.get_symbol3()):
                print("Blank")

            # Complete opposites
            elif self.get_isdouble() & bool(self.get_symbol3())\
                    & die.get_isdouble() & bool(die.get_symbol3()):
                print("Blank")

            # Complete opposites
            elif self.get_isdouble() & bool(self.get_symbol1())\
                    & die.get_isdouble() & bool(die.get_symbol1()):
                print("Blank")

            # Complete opposites
            elif bool(self.get_symbol2()) & bool(die.get_symbol2()):
                print("Blank")

            # Complete opposites
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(die.get_symbol1()) & bool(not die.get_symbol3()):
                print(self.get_symbol3())

            # cancelling out one success leaving one advantage
            elif bool(self.get_symbol3()) & bool(self.get_symbol1())\
                    & bool(not die.get_symbol1()) & bool(die.get_symbol3()):
                print(self.get_symbol1())

            # cancelling out one advantage leaving one success
            elif bool(die.get_symbol3()) & bool(die.get_symbol1())\
                    & bool(not self.get_symbol1()) & bool(self.get_symbol3()):
                print(die.get_symbol1())

            # cancelling out one threat leaving one failure
            elif bool(die.get_symbol3()) & bool(die.get_symbol1())\
                    & bool(self.get_symbol1()) & bool(not self.get_symbol3()):
                print(die.get_symbol3())

            # cancelling out one failure leaving one threat
            else:
                # If the symbols rolled do not oppose
                print("{0} and {1}, they don't match.".format(str(self),
                                                              str(die)))
        else:
            # If the symbols rolled do not oppose
            print("The dice don't match, be sure they are opposing!")

        # Error handling
        # except ArithmeticError:
        # print("The dice have different number of faces!")

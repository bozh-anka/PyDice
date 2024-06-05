"""
This is a class that abstracts the functions of a symbol-ed dice.
There are two types of die for each denomination (d6,d8,d12).

The type is denoted as positive(True) and negative(False)
Each die can have a combination of 3 symbol classes that are as follows:

Positive    Negative  Name
Success and Failure  symbol1
Triumph and Despair  symbol2
Advantage and Threat symbol3

Some symbols can appear twice on the same face od the die,
that is denoted by isdouble(True)

The side number is set to zero,
each subclass changes it to their respective side denomination.
There are getters and setters for all attributes besides sides,
which only has a getter.

There are two abstract methods in the class roll() and cancel()
The first when implemented assigns the symbols to each die,
which are by default null.
Cancel accepts a second die and compares their symbols,
printing the result of the comparison.

There is one concrete method which checks if all symbols are null,
this is to check for a blank face.
Dice can roll a blank, this is intended functionality.

"""


from abc import ABC, abstractmethod


class DieClass(ABC):

    def __init__(self, positive):
        self.positive = positive

        # positive or negative die
        self.isDouble = False
        # double or single symbol
        self.sides = 0  # number of sides on the die
        self.symbol1 = ""
        self.symbol2 = ""
        self.symbol3 = ""

    def get_positive(self):
        """
        :return: bool positivity of the die
        """
        return self.positive

    def set_positive(self, positive):
        """
        Set positivity
        :param positive: bool
        """
        # ensure is bool
        if isinstance(positive, bool):
            self.positive = positive
        else:
            self.positive = False

    def get_isdouble(self):
        """
        :return: bool is the symbol doubled
        """
        return self.isDouble

    def set_isdouble(self, double):
        """
        Set doubled attribute
        :param double: bool
        """
        # ensure is bool
        if isinstance(double, bool):
            self.isDouble = double
        else:
            self.isDouble = False

    def get_sides(self):
        """
        Return number of sides
        :return: int
        """
        return self.sides

    def get_symbol1(self):
        """
        Returns symbol1 value
        :return: str Success or Failure
        """
        return self.symbol1

    def get_symbol2(self):
        """
        Return symbol2 value
        :return: str Triumph or Despair
        """
        return self.symbol2

    def get_symbol3(self):
        """
        Return symbol3 value
        :return: str Advantage or Threat
        """
        return self.symbol3

    def set_symbol1(self, sym):
        """
        Set dice face to symbol1
        :param sym: str set symbol1
        """
        self.symbol1 = sym

    def set_symbol2(self, sym):
        """
        Set dice face to symbol2
        :param sym: str set symbol2
        """
        self.symbol2 = sym

    def set_symbol3(self, sym):
        """
        Set dice face to symbol3
        :param sym: str set symbol3
        """
        self.symbol3 = sym

    def is_blank(self):
        """
        Checks if all symbol attributes are blank
        :return: bool True if all blank False otherwise
        """
        # Check if all symbols are ""/null
        if bool(not self.get_symbol1()) & bool(not self.get_symbol2())\
                & bool(not self.get_symbol3()):
            return True
        else:
            return False

    @abstractmethod
    def roll(self):
        pass

    @abstractmethod
    def cancel(self, die: ABC):
        pass

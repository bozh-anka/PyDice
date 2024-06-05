"""

This file contains all the functions necessary for processing
a csv file of the format:

         sides;Positivity
    Example: 6;Positive
             8;Negative

Into dedicated by type and positivity pairs that
then get compared and cancelled accordingly.
The results are printed in the console.
"""


from SixDie import SixDieClass
from EightDie import EightDieClass
from TwelveDie import TwelveDieClass
import csv
import argparse


def check_type(row: list):
    """
    A function for determining die type based off of csv file rows

    :param row: List strings denoting die sides and type
    :return: String shorthand for die sides and type

    """
    if bool(int(row[0]) == 6) & bool(row[1] == "Positive"):
        # If the die is six sided and positive
        return "psix"
    elif bool(int(row[0]) == 6) & bool(row[1] == "Negative"):
        # If the die is six sided and negative
        return "nsix"
    elif bool(int(row[0]) == 8) & bool(row[1] == "Positive"):
        # If the die is eight sided and positive
        return "peight"
    elif bool(int(row[0]) == 8) & bool(row[1] == "Negative"):
        # If the die is eight sided and negative
        return "neight"
    elif bool(int(row[0]) == 12) & bool(row[1] == "Positive"):
        # If the die is twelve sided and positive
        return "ptwelve"
    elif bool(int(row[0]) == 12) & bool(row[1] == "Negative"):
        # If the die is twelve sided and negative
        return "ntwelve"
    else:
        return "Wrong input"


def roll_dice(die_list):
    """Calls the roll function for every die in die_list"""
    for i in range(len(die_list)):
        die_list[i].roll()


def cancel_all(plist, nlist):
    """

    Function to pair dice from each list against each other and cancel
    Prints cancellation results and unpaired remainder

    :param plist: Positive list of dice
    :param nlist: Negative list of dice


    """
    if len(plist) == len(nlist):
        # If positive list and negative list are the same
        for i in range(len(plist)):
            # Call cancel for each pair
            plist[i].cancel(nlist[i])
    else:
        print("Uneven match up.")
        if bool(not plist):
            # If the positive list is empty
            print("No opposites the remainder is: ")
            for i in range(len(nlist)):
                # Print negative list
                print(nlist[i])
        elif bool(not nlist):
            # If the negative list is empty
            print("No opposites the remainder is: ")
            for i in range(len(plist)):
                # Print positive list
                print(plist[i])
        elif len(plist) > len(nlist):
            # If the positive list is longer
            for i in range(len(nlist)):
                # Cancel pairs
                plist[i].cancel(nlist[i])
            print("\nThe left over is: ")
            for i in range(len(nlist), len(plist)):
                # Print left over positive
                print(plist[i])
        else:
            # If the negative list is longer
            for i in range(len(plist)):
                # Cancel pairs
                plist[i].cancel(nlist[i])
            print("The left over is:")
            for i in range(len(plist), len(nlist)):
                # Print left over negative
                print(nlist[i])


def file_processing():
    """
    Function for reading dice quantities from a csv file and processing them
    """
    # Accept file name as command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    arg = parser.parse_args()

    # File handling
    try:
        # Open file fed through command line
        dice = open(arg.f, mode='r')

        # Initialize dice lists
        psix_list = []  # Six sided Positive
        nsix_list = []  # Six sided Negative
        peight_list = []  # Eight sided Positive
        neight_list = []  # Eight sided Negative
        ptwelve_list = []  # Twelve sided Positive
        ntwelve_list = []  # Twelve sided Negative

        # Create reader for file processing
        csv_reader = csv.reader(dice, delimiter=';')

        # First line is the header
        linenum = 0

        # Reading row by row
        for row in csv_reader:

            # Read header
            if linenum == 0:
                print("File processing started, dice are being paired up")

                # Move on from header
                linenum += 1
            else:
                # Distribute data into matching list
                match check_type(row):
                    case "psix":
                        # If positive six die
                        psix_list.append(SixDieClass(True))
                    case "nsix":
                        # If negative six die
                        nsix_list.append(SixDieClass(False))
                    case "peight":
                        # If positive eight die
                        peight_list.append(EightDieClass(True))
                    case "neight":
                        # If negative eight die
                        neight_list.append(EightDieClass(False))
                    case "ptwelve":
                        # If positive eight die
                        ptwelve_list.append(TwelveDieClass(True))
                    case "ntwelve":
                        # If negative eight die
                        ntwelve_list.append(TwelveDieClass(False))

        print("Dice are paired, rolling and cancelling.")
        print("Six sided die results are: ")

        # Roll the dice in six die lists
        roll_dice(psix_list)
        roll_dice(nsix_list)

        # Compare and Cancel
        cancel_all(psix_list, nsix_list)

        print("\nEight sided die results are: ")

        # Roll the dice in eight die lists
        roll_dice(peight_list)
        roll_dice(neight_list)

        # Compare and Cancel
        cancel_all(peight_list, neight_list)

        print("\nTwelve sided die results are: ")

        # Roll the dice in twelve die lists
        roll_dice(ptwelve_list)
        roll_dice(ntwelve_list)

        # Compare and Cancel
        cancel_all(ptwelve_list, ntwelve_list)

        print("\n\nAll dice pairs processed!")

        # Close file
        dice.close()
    except FileNotFoundError:
        # Handle file not found
        print("File not found")

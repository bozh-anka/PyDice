from DiceFunctions import file_processing

if __name__ == '__main__':
    """
    csv file of the format 
    sides;Positivity
    Example: 6;Positive
             8;Negative

    Each entry is a new die into the pile.
    Dice get paired against their opposite and their rolls cancelled

    """
    file_processing()

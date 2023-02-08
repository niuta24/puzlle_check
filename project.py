""" Implements the first rule of the game
"""
def first_rule(board:list)->bool:
    """ Checking if there is no repeating of numbers in the line
    Args:
        board (list): field woth strings
    >>> first_rule(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **","  8  2***", "  2  ****"])
    True
    >>> first_rule(["**** ****", "***1 **1*", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **","  8  2***", "  2  ****"])
    False
    """
    for i in board:
        for k in range(9):
            if i.count(str(k))>1:
                return False
    return True

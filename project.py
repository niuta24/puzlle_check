""" Implements the first rule of the game
"""


def validate_board(board: list) -> bool:
    """ Checking if the field is okay with all 3 rules
    Args:
        board (list): field with strings
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"]
    False
    >>> validate_board(["**** ****", "***1 **1*", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   *  **", "  8  2***", "  2  ****"]
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   *  **", "  8  2***", "  2  ****"]
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   4  **", "  8  2***", "  2  ****"]
    False
    """
    if not first_rule(board):
        return False
    if not second_rule(board):
        return False
    if not third_rule(board):
        return False
    return True


def first_rule(board: list) -> bool:
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
        for k in range(1, 10):
            if i.count(str(k)) > 1:
                return False
    return True

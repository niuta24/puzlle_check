"""
Checks board
"""
def validate_board(board: list) -> bool:
    """ Checking if the field is okay with all 3 rules
    Args:
        board (list): field with strings
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 **1*", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   *  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   *  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   4  **", "  8  2***", "  2  ****"])
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
    """
    Checking if there is no repeating of numbers in the line
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

def second_rule(board):
    """
    >>> second_rule(["*1**4***5", "**3***27*", "4***2**6*", \
"*76**91**","**83**5**", "*4**8**3*", "***7*1**8",\
"2**5***4*", "*6***2**9"])
    True
    >>> second_rule(["*1**4***5","**3***27*","4***2**6*","*76**91**",\
"**83**5**","*4**8**3*","***7*1**8",\
"2**5***4*","*6**2***9"])
    False
    >>> second_rule(["**** ****", "***1 ****", "  3****",\
"* 4 1****", "     9 5 ", " 6  89  *", "3   1  ","  8  2***", "  2  ****"])
    False
    >>> second_rule(["**** ****",\
                    "***1 ****",\
                    "  3****",\
                    "* 4 1****",\
                    "     9 5 ",\
                    " 6  89  *",\
                    "3   1  ",\
                    "  8  2***",\
                    "  2  ****"])
    False
    """
    res = [[] for x in range(1,10)]
    for line in board:
        for num, element in enumerate(line):
            res[num].append(element)
    for boardy in res:
        for k in range(1,10):
            if boardy.count(str(k))>1:
                return False
    return True

def third_rule(board:list) -> bool:
    """
    Checking if there is no repeating of numbers in the colours of the field
    Args:
        board (list): field of the game
    Returns:
        bool: True if there is no repeating of numbers in the colours
    >>> third_rule(["**** ****", "***1 ****", "** 13****", "* 4  ****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> third_rule(["**** ****", "***1 ****", "**  3****", "* 4  ****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    row = 0
    col = 4
    check_lst = []
    for _ in range(5):
        for jnd in range(5):
            if board[row + jnd][col] != " " and board[row + jnd][col] != "*":
                check_lst.append(int(board[row + jnd][col]))
        for jnd in range(4):
            if board[row + 4][col + jnd + 1] != " " and board[row + 4][col + jnd + 1] != "*":
                check_lst.append(int(board[row + 4][col + jnd + 1]))
        row += 1
        col -= 1
        for elm in check_lst:
            if int(elm) > 9 or int(elm) < 1:
                return False
        if len(check_lst) != len(set(check_lst)):
            return False
        check_lst = []
    return True

if __name__=="__main__":
    validate_board(["**** ****", "***1 ****", "**  3****",\
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])

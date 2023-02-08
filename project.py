def third_rule(board):
    """Checking if there is no repeating of numbers in the colours of the field 

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
    for ind in range(5):
        for jnd in range(5):
            if board[row + jnd][col] != " " and board[row + jnd][col] != "*":
                check_lst.append(int(board[row + jnd][col]))
        for jnd in range(5):
            if board[row + 4][col + jnd] != " " and board[row + 4][col + jnd] != "*":
                check_lst.append(int(board[row + 4][col + jnd]))
        row += 1
        col -= 1
        for elm in check_lst:
            if int(elm) > 9 or int(elm) < 1:
                return False
        if len(check_lst) != len(set(check_lst)):
            return False
        check_lst = []
    return True

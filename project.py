"""subtask 2"""
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

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=True))

def spiralOrder(matrix):
    r = len(matrix)  # 3
    c = len(matrix[0])  # 4

    res = []

    for turn in range(min(c, r) // 2):  # of rounds
        # only one round of turn

        # r = 0,1,2,3
        for j in range(turn, c - turn):
            res.append(matrix[turn][j])
        # c = 1, 2
        for i in range(turn + 1, r - turn):
            res.append(matrix[i][c - turn - 1])
        # r = 0, 1, 2 | c = 2
        for j in range(c - turn - 2, turn - 1, -1):
            res.append(matrix[r - turn - 1][j])
        # c = 1 | r = 0
        for i in range(r - turn - 2, turn, -1):
            res.append(matrix[i][turn])

    # check whether it's odd or even
    # if it's odd, then add either the last row or the last column
    if min(c, r) % 2 == 1:
        turn = min(c, r) // 2  # take the floor

        if r <= c: # add a column
            for j in range(turn, c - turn):
                res.append(matrix[turn][j])
        else: # add a row
            for i in range(turn, r - turn):
                res.append(matrix[i][c - turn - 1])
    # if it's even, finish turns
    return res


input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output = spiralOrder(input)
print(output)

# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]

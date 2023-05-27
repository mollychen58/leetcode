def spiralOrder(matrix):
    l = 0
    r = len(matrix[0]) - 1
    t = 0
    b = len(matrix) - 1
    res = []

    while True:
        # left to right
        for i in range(l, r + 1):
            res.append(matrix[t][i])
        t += 1
        if t > b: break

        # top to down
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        r -= 1
        if l > r: break

        # right to left
        for i in range(r, l - 1, -1):
            res.append(matrix[b][i])
        b -= 1
        if t > b: break

        # bottom to top
        for i in range(b, t - 1, -1):
            res.append(matrix[i][l])
        l += 1
        if l > r: break

    return res


input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output = spiralOrder(input)
print(output)

# r 0  1  2  3          c
# [1, 2, 3, 4]         0
# [5, 6, 7, 8]         1
# [9, 10, 11, 12]      2

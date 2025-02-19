# exploration_strategies.py
def zigzag_iterator(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                yield (i, j)
        else:
            for j in range(cols - 1, -1, -1):
                yield (i, j)

"""
(C) Copyright 2024 Muhammad Faran Aiki
On analysis of Linear Algebra
for Lights out
made by Faran Aiki out of curiosity
"""

""""""
def sort_matrix(mtr : list, val : list) -> list[list]:
    max_l = min(len(mtr), len(mtr[0]))
    row_s = len(mtr)
    loop = 1
    while loop < max_l:
        for row in range(loop, row_s):
            if mtr[row][loop] == 1:
                temp = val[row]
                val[row] = val[loop]; val[loop] = temp
                temp = mtr[row]
                mtr[row] = mtr[loop]; mtr[loop] = temp
                break
        loop += 1
    return [val, mtr]

# binary 2
def calculate_rref(matrix : list) -> list:
    already_pivot : set = set()
    col : int = 0
    row_s, col_s = len(matrix), len(matrix[0])
    val : list[set] = [set([i + 1]) for i in range(row_s)]
    for col in range(col_s):
        pivot = -1
        y = 0
        while y < row_s:
            if y == pivot:
                pass
            elif pivot == -1 and matrix[y][col] == 1 and not y in already_pivot:
                pivot = y
                already_pivot |= set([pivot])
                y = -1
            elif pivot != -1 and matrix[y][col] == 1:
                #print(y, col)
                #print(matrix[pivot], "%d and" %pivot, matrix[y])
                n_matr = [matrix[pivot][t] ^ matrix[y][t] for t in range(len(matrix[y]))]
                matrix[y] = n_matr
                val[y] ^= val[pivot]
            y += 1

    return sort_matrix(matrix, val)

def ask_input() -> list:
    matrix = []    

    print("Matrix ( ... | . ):")
    last : str = ""
    while True:
        s_matr : str = input("")
        if s_matr.strip() == "":
            break
        matrix.append([int(i) for i in s_matr.strip().split(' ')])

    return matrix

def main() -> int:
    matrix : list = ask_input()
    print("Result")
    v = calculate_rref(matrix)
    for i in v[0]:
        print(i)
    print("Whole matrix")
    for matr in range(len(v[1])):
        print(' '.join([str(s) for s in v[1][matr]]), v[0][matr])
    return 0

if __name__ == '__main__':
    exit(main())


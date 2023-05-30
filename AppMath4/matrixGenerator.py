from scipy.sparse import dok_matrix
from random import randint, random


def random_matrix_generator(x, y):
    r = 0
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            if i == j:
                array[i].append(3 * x * random() + 3 * x)
            else:
                array[i].append(random() * 3)
            r += 1
    return array

def ak_matrix_generator(k, n):
    A = dok_matrix((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                A[i, j] = randint(0, 4) - 4

    for i in range(n):
        for j in range(n):
            if i != j:
                A[i, i] += A[i, j]
        A[i, i] += pow(10, -k)

    return A


def gilbert_matrix_generator(n):
    M = dok_matrix((n, n))

    for i in range(n):
        for j in range(n):
            M[i, j] = 1 / (i + j + 1)
    return M
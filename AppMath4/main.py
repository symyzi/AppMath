import time
from scipy.sparse import csr_matrix
from matrixGenerator import ak_matrix_generator, random_matrix_generator, gilbert_matrix_generator
from methods import *


# Matrix -> csr & LU-decomposition & Inverse Matrix finding method through LU-decomposition


def task1():
    print("------- Task 1 - CSR matrix ops. -------")

    A = [[10, -7, 0], [-3, 6, 2], [5, -1, 5]]
    A = csr_matrix(A)

    print("Matrix A:\n", A, "\n")

    array = lu_sparse(A)
    L = array[0]

    print("LU Decomposition:")
    print("L:\n", L, '\n')

    U = array[1]

    print("U:\n", U, "\n")

    b = inverse_sparse(A)

    print("Inverse of matrix A (via LU decomp.):")
    print(b, "\n")

# Implementation of Seidel Method


def task2():
    print("------- Task 2 - Seidel Method -------")

    A = ak_matrix_generator(2, 4)
    B = csr_matrix(random_matrix_generator(4, 1))
    EPS = 1e-5

    print('Matrix: \n', A, '\n')
    print('Vector B: \n', B, '\n')

    C, iterations = seidel(A, B, EPS)
    print('Result:\n', C, '\n')
    print('Iterations:', iterations, '\n')

# Ak Matrix Testing
def task3():
    print("------- Task 3 - Compare speed for AK matrices -------")


    for k in range(1, 5):
        print('K value:', k)

        A = ak_matrix_generator(k, 20)
        B = ak_matrix_generator(k, 20)
        start_time = time.time()
        C = system_solution(A, B)

        print('\tLU: ')
        print("\tTime: %s seconds" % (time.time() - start_time), '\n')

        print('\tSeidel: ')
        EPS = 1e-5
        start_time1 = time.time()
        S, count = seidel(A, B, EPS)

        C = C.todense()
        S = S.todense()

        print("\tTime: %s seconds" % (time.time() - start_time1), '\n')


# Hilbert Matrix Testing
def task4():
    print("------- Task 4 - Compare speed for Hilbert matrices -------")
    for n in range(1, 10):
        print('Size:', n)

        print('LU: ')
        A = gilbert_matrix_generator(n)
        B = gilbert_matrix_generator(n)
        start_time = time.time()
        C = (system_solution(A, B))
        print("%s seconds" % (time.time() - start_time))

        print('Seidel:')
        EPS = 1e-5
        A = gilbert_matrix_generator(n)
        B = gilbert_matrix_generator(n)

        start_time = time.time()
        C, count = seidel(A, B, EPS)

        print("Time: %s seconds" % (time.time() - start_time))
        print('Iterations: ', count, '\n')

# Overall methods comparison
def task5():
    print("------- Task 5 - Compare speed for bigger matrices -------")

    sizes = [10, 50, 10 ** 2, 10 ** 3]

    for i in sizes:
        print("Matrix size:", i)

        A = csr_matrix(random_matrix_generator(i, i))
        B = csr_matrix(random_matrix_generator(i, 1))
        start_time = time.time()
        C, count = (system_sparse_solution_count(A, B))

        print('\tLU:')
        print("\tTime: %s seconds" % (time.time() - start_time))
        print('\tIterations:', count, '\n')


        EPS = 1e-5
        A = csr_matrix(random_matrix_generator(i, i))
        B = csr_matrix(random_matrix_generator(i, i))

        start_time = time.time()
        C, count = seidel(A, B, EPS)
        print('\tSeidel:')
        print("\tTime: %s seconds" % (time.time() - start_time))
        print('\tIterations:', count, '\n')

def main():
    task1()

if __name__ == '__main__':
    main()

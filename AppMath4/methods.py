import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import dok_matrix


# Sparse matrix inversion
def inverse_sparse(a):
    n = a.shape[0]

    L, U = lu_sparse(a)

    Y = []

    for i in range(n):
        y = triangular_system_solution(
            L, np.eye(100, 1, k=-i), lower=True)
        Y.append(y)

    Ai = lil_matrix(a.shape)
    for i in range(n):
        Ai[:, i] = triangular_system_solution(
            U, Y[i], lower=False)

    return Ai


# LU matrix decomposition
def lu_sparse(a):
    EPS = 1e-5

    L = dok_matrix(a.shape)
    U = dok_matrix(a.shape)

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if i <= j:
                t = a[i, j] - (L[i, :i] @ U[:i, j]).sum()

                if abs(t) > EPS:
                    U[i, j] = t

                if i == j:
                    L[i, i] = 1.0

            else:
                if U[j, j] == 0.0:
                    raise ValueError('LU decomposition does not exist!')

                t = (a[i, j] - (L[i, :j] @ U[:j, j]).sum()) / U[j, j]
                if abs(t) > EPS:
                    L[i, j] = t

    return L.tocsr(), U.tocsr()


# System Ax=B solving via LU decomposition
def system_solution(a, b):
    n = a.shape[0]

    L, U = lu_sparse(a)

    y = triangular_system_solution(L, b, lower=True)
    x = triangular_system_solution(U, y, lower=False)

    return x


# Triangular system solving
def triangular_system_solution(a, b, lower):
    n = a.shape[0]

    x = dok_matrix((n, 1))

    if lower:
        for i in range(n):
            x[i] = (b[i].sum() - (a[i, :i] @ x[:i]).sum()) / a[i, i]
    else:
        for i in range(n - 1, -1, -1):
            x[i] = (b[i].sum() - (a[i, i + 1:] @ x[i + 1:]).sum()) / a[i, i]
    return x


# lu_sparse with iteration counter
def lu_sparse_count(a, count):
    EPS = 1e-100

    L = dok_matrix(a.shape)
    U = dok_matrix(a.shape)

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if i <= j:
                t = a[i, j] - (L[i, :i] @ U[:i, j]).sum()
                count = count + 1

                if abs(t) > EPS:
                    U[i, j] = t

                if i == j:
                    L[i, i] = 1.0

            else:
                if U[j, j] == 0.0:
                    raise ValueError('LU decomposition does not exist!')

                t = (a[i, j] - (L[i, :j] @ U[:j, j]).sum()) / U[j, j]
                count = count + 1
                if abs(t) > EPS:
                    L[i, j] = t

    return L.tocsr(), U.tocsr(), count


# triangular_system_solution with iteration counter
def triangular_system_solution_count(a, b, count, lower):
    n = a.shape[0]

    x = dok_matrix((n, 1))

    if lower:
        for i in range(n):
            x[i] = (b[i].sum() - (a[i, :i] @ x[:i]).sum()) / a[i, i]
            count = count + 1
    else:
        for i in range(n - 1, -1, -1):
            x[i] = (b[i].sum() - (a[i, i + 1:] @ x[i + 1:]).sum()) / a[i, i]
            count = count + 1
    return x, count


def system_sparse_solution_count(a, b):
    n = a.shape[0]
    count = 0
    L, U, count = lu_sparse_count(a, count)

    y, count = triangular_system_solution_count(L, b, count, lower=True)
    x, count = triangular_system_solution_count(U, y, count, lower=False)

    return x, count


# System solving via Seidel method
def seidel(a, b, eps):
    U = dok_matrix(a.shape)
    L = dok_matrix(a.shape)

    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            if i < j:
                U[i, j] = a[i, j]
            else:
                L[i, j] = a[i, j]

    L_inv = inverse_sparse(L)
    T = -L_inv @ U
    C = L_inv @ b
    x = dok_matrix(b.shape)
    prev = dok_matrix(b.shape)

    for i in range(b.shape[0]):
        x[i, 0] = 1
    count = 0

    while is_not_equal(x, prev, eps):
        prev = x
        x = T @ x + C
        count += 1

    return x, count

# Matrix equality comparer
def is_not_equal(a, b, eps):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if abs(a[i, j] - b[i, j]) > eps:
                return True
    return False

from Matrix import Matrix
from math import sqrt
from Givence import Givence_rotation
import copy

EPS = 1e-15

def Hessenberg(input_matrix):
    M = input_matrix.rows
    N = input_matrix.cols
    if M == 0 or N == 0:
        raise ValueError('Матрица пуста')

    # Создаем копию данных, чтобы не испортить исходную
    A = copy.deepcopy(input_matrix.data)

    p = [0.0] * M

    Q_data = [[0.0] * M for _ in range(M)] #задаём как единичную
    for k in range(M):
        Q_data[k][k] = 1.0

    for i in range(N - 2):
        #Вычисляем норму подстолбца
        s = 0.0
        for r in range(i + 2, M):
            s += A[i][r] ** 2

        s += A[i][i + 1] ** 2

        if sqrt(s) > EPS:
            beta = sqrt(s)
            if A[i][i + 1] > 0:
                beta = -beta

            mu = 1.0 / (beta * (beta - A[i][i + 1]))

            #Вектор p
            for r in range(M):
                p[r] = 0.0
            for r in range(i + 2, M):
                p[r] = A[i][r]
            p[i + 1] = A[i][i + 1] - beta

            # Левое умножение: A <- H * A
            for c in range(i, N):  # для каждого столбца
                dot = 0.0
                for r in range(i + 1, M):
                    dot += A[c][r] * p[r]
                dot *= mu
                for r in range(i + 1, M):
                    A[c][r] -= dot * p[r]

            # Правое умножение: A <- A * H
            for r in range(M):  # для каждой строки
                dot = 0.0
                for c in range(i + 1, N):
                    dot += A[c][r] * p[c]
                dot *= mu
                for c in range(i + 1, N):
                    A[c][r] -= dot * p[c]

            # Накопление Q <- Q * H
            for r in range(M):
                dot = 0.0
                for c in range(i + 1, M):
                    dot += Q_data[c][r] * p[c]
                dot *= mu
                for c in range(i + 1, M):
                    Q_data[c][r] -= dot * p[c]

    H = Matrix(data=A)
    Q = Matrix(data=Q_data)
    return H, Q


def Eigenvalues_QR_Iterations(input_matrix, eps=1e-5):
    M = input_matrix.rows
    N = input_matrix.cols
    if M == 0:
        raise ValueError('Матрица пуста')
    if M != N:
        raise ValueError('Матрица неквадратная')

    #Матрицы QR-разложения
    Q = Matrix(data=[[0.0] * M for _ in range(M)])
    R = Matrix(data=[[0.0] * M for _ in range(M)])
    RQ = Matrix(data=[[0.0] * M for _ in range(M)])
    Eigenvectors = Matrix(data=[[0.0] * M for _ in range(M)]) #собственные векторы
    Eigenvalues = [] #собственные значения

    for i in range(M):
        Eigenvectors.data[i][i] = 1.0
        for j in range(M):
            RQ.data[i][j] = input_matrix.data[i][j]

    while True:
        num = 0
        for i in range(M-1):
            if abs(RQ.data[i][i+1]) < eps:
                num += 1

        if num == M - 1:
            break

        Q.clear()
        R.clear()
        Q, R = Givence_rotation(RQ)

        RQ = R.multiply_matrix(Q)
        Eigenvectors = Eigenvectors.multiply_matrix(Q)

    for i in range(M):
        Eigenvalues.append(RQ.data[i][i])

    return Eigenvectors, Eigenvalues



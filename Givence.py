from Matrix import Matrix
from math import sqrt

EPS = 1e-15 #машинный ноль


def Givence_rotation(A):
    #Вращение Гивенса исправленное
    Q = Matrix(data=[[0]*A.rows for _ in range(A.cols)]) #результат разложения
    for i in range(A.cols):
        Q.data[i][i] = 1.0
    R = Matrix(data=A.data)

    M = A.rows
    N = A.cols

    help1, help2, c, s  = 0, 0, 0, 0
    global EPS

    for j in range(N-1):
        for i in range(j+1, M):
            if abs(R.data[j][i]) > EPS:
                help1 = sqrt(R.data[j][i]**2 + R.data[j][j]**2)
                c = R.data[j][j]/help1
                s = R.data[j][i]/help1

                for k in range(j, N):
                    help1 = c*R.data[k][j] + s*R.data[k][i]
                    help2 = c*R.data[k][i] - s*R.data[k][j]
                    R.data[k][j] = help1
                    R.data[k][i] = help2

                for k in range(M):
                    help1 = c*Q.data[j][k] + s*Q.data[i][k]
                    help2 = c*Q.data[i][k] - s*Q.data[j][k]
                    Q.data[j][k] = help1
                    Q.data[i][k] = help2

    return Q, R
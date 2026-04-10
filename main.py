from Givence import Givence_rotation
from Matrix import Matrix
from Eigenvalues import Hessenberg, Eigenvalues_QR_Iterations

print('Практическое задание №3. Проблема собственных значений')
print()

print('Ковариционная матрица данных: ')
C = Matrix(data = [[0.66666666, 0.33333333], [0.3333333, 0.33333333]])
C.print_matrix()

#Находим собственные значения и собственные вектора
C = Hessenberg(C)[0]
Eigvectors, Eigenvalues = Eigenvalues_QR_Iterations(C)
print('Cобственные векторы:')
Eigvectors.print_matrix()
print('Собственные значения', Eigenvalues)

#Рассчитываем общую дисперсию и долю каждого признака
summ_eig = sum(Eigenvalues)
print('Общая дисперсия: ', summ_eig)
doli = []
for i in range(len(Eigenvalues)):
    x = Eigenvalues[i]/summ_eig*100
    print('Доля признака номер', i+1, ':', x)
    doli.append(x)

print()
print('Матрица центрирования данных: ')
B = Matrix(data=[[0.0, 0.0, -1.0, 1.0], [0.5, -0.5, -0.5, 0.5]])
B.print_matrix()

#Проекция центрированнных данных на главные компоненты
print('Проекция центрированнных данных на главные компоненты:')
B2 = B.multiply_matrix(Eigvectors)
B2.print_matrix()




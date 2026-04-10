class Matrix():
    # класс матриц
    def __init__(self, data=[]):
        self.data = data
        self.rows = len(data[0])  # количество строк
        self.cols = len(data) if data else 0  # количество столбцов

    def transpose(self):  # транспонирование
        if self.rows == 0 or not self.data:
            return self

        # Создаем транспонированную матрицу
        transposed = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                new_row.append(self.data[j][i])
            transposed.append(new_row)

        # Обновляем данные и размеры
        self.data = transposed
        self.rows, self.cols = self.cols, self.rows  # меняем местами
        return self

    def print_matrix(self):  # вывод матрицы на экран
        if self.cols == 0 or not self.data:
            print('Матрица пуста')
            return

        for i in range(self.rows):
            for j in range(self.cols):
                x = str(self.data[j][i])
                n = 20 - len(x)
                print(x+n*' ', end=' ')
            print()
        print()

    def matrix_add(self, other):
        """Сложение матриц (оператор +)"""
        # Проверка размерностей
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Нельзя сложить матрицы {self.rows}x{self.cols} и {other.rows}x{other.cols}")

        # Создание новой матрицы для результата
        result_data = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.data[i][j] + other.data[i][j])
            result_data.append(row)

        return Matrix(result_data)

    def multiply_matrix(self, B):
        """Умножение данной матрицы на B"""
        # Проверка возможности умножения
        if self.cols != B.rows:
            raise ValueError("Количество столбцов A должно равняться количеству строк B")

        # Размеры результирующей матрицы
        rows_A = self.rows  # количество строк в A
        cols_B = B.cols  # количество столбцов в B

        result_data = [[0 for _ in range(rows_A)] for _ in range(cols_B)]

        for j in range(cols_B):
            for i in range(rows_A):
                total = 0
                for k in range(self.cols):
                    total += self.data[k][i] * B.data[j][k]
                result_data[j][i] = total

        return Matrix(data=result_data)

    def scalar_multiply(self, scalar):
        for i in range(self.cols):
            for j in range(self.rows):
                self.data[i][j] *= scalar

        return self

    def determinant(self):
        """Определитель матрицы второго порядка"""
        return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

    def clear(self): #очистка
        self.data = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
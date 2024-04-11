import time


def open_file(filename):
    # Открываем файл для чтения
    with open(filename, 'r') as file:
        matrix = []
        # Читаем каждую строку в файле
        for line in file:
            # Разделяем строку на элементы и преобразуем их в целые числа
            row = list(map(int, line.split()))
            # Добавляем строку в матрицу
            matrix.append(row)
    return matrix

def save_to_file(data, filename):
   with open(filename, "w") as file:
       file.write("\n".join(map(str, data)) + "\n")


def transponir(matrix):
   # Создаем пустую матрицу для хранения результата транспонирования
   transponirResult = [
       [0]*len(matrix)
       for i in range(len(matrix[0]))
   ]
   # Проходим по каждой строке исходной матрицы
   for row in range(len(matrix)):
       # Проходим по каждому столбцу исходной матрицы
       for colon in range(len(matrix[0])):
           # Значение в ячейке исходной матрицы становится значением в соответствующем столбце результирующей матрицы
           transponirResult[colon][row] = matrix[row][colon]

   # Возвращаем транспонированную матрицу
   return transponirResult


def Jordana_Gaussa_inverse(matrix):
    # Создаем расширенную матрицу, добавляя к каждой строке матрицы единицы в конце
    extended_matrix = [
        [
            matrix[row][colon] if colon < len(matrix) else int(row == colon - len(matrix))
            for colon in range(2 * len(matrix))
        ]
        for row in range(len(matrix))
    ]
    # Проходим по каждой строке матрицы
    for row in range(len(matrix)):
        # Выбираем элемент диагонали текущей строки
        diagonal_elem = extended_matrix[row][row]
        for colon in range(2 * len(matrix)):
            # Делим все элементы в строке на элемент диагонали
            extended_matrix[row][colon] /= diagonal_elem
        # Обнуляем все элементы под строкой элемента диагонали
        for colon in range(len(matrix)):
            if row != colon:
                scalar = extended_matrix[colon][row]
                for k in range(2 * len(matrix)):
                    extended_matrix[colon][k] -= scalar * extended_matrix[row][k]

    # Извлекаем обратную матрицу из расширенной матрицы
    inverse = [
        [
            extended_matrix[row][colon]
            for colon in range(len(matrix), 2 * len(matrix))
        ]
        for row in range(len(matrix))
    ]

    return inverse

def minor(matrix, i, j):
   # Создаем новую матрицу, удаляя строку i и столбец j
   new_matrix = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
   return new_matrix

def determinant(matrix):
    det = 0
    razmernost = len(matrix)
    if razmernost == 1:
        return matrix[0][0]
    elif razmernost == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for k in range(razmernost):
           det += (-1) ** k * matrix[0][k] * determinant(minor(matrix, 0, k))
    return det


# Функция для вычисления обратной матрицы
def Algebrdopoln_Determinant_inverse(matrix):
    # Создание матрицы для хранения элементов обратной матрицы
    complete_matrix = [
        [0]*len(matrix)
        for _ in range(len(matrix[0]))
    ]
    # Вычисление определителя исходной матрицы
    det_A = determinant(matrix)

    # Вычисление элементов обратной матрицы
    for row in range(len(matrix)):
        for colon in range(len(matrix[0])):
            # Создание подматрицы без строки и столбца, где находится текущий элемент
            sub_matrix = matrix[:row] + matrix[row + 1:]
            # Вычисление минора и определителя минора, умножение на (-1) в степени суммы индексов строки и столбца
            complete_matrix[row][colon] = (-1) ** (row+colon) * determinant(minor(matrix, row, colon))

    # Транспонирование матрицы
    complete_matrix = transponir(complete_matrix)
    # Нормализация матрицы путем деления каждого ее элемента на определитель исходной матрицы
    complete_matrix = [[k/det_A for k in elem] for elem in complete_matrix]
    return complete_matrix


try:
    matrix = open_file("input.txt")
    results = []
    start_time = time.perf_counter()
    algebrdop_determin_matrix = Algebrdopoln_Determinant_inverse(matrix)  # Обратная матрица по алгоритму вычисления определителя и алгебраического дополнения
    sec_time = time.perf_counter()
    jordana_gauss_matrix = Jordana_Gaussa_inverse(matrix)  # Обратная матрица по алгоритму Жордана-Гаусса
    end_time = time.perf_counter()

    algebrdon_determin_time = sec_time - start_time
    jordana_gauss_time = end_time - sec_time

    results.append(algebrdop_determin_matrix)
    results.append(algebrdon_determin_time)
    results.append(jordana_gauss_matrix)
    results.append(jordana_gauss_time)
    save_to_file(results, "output.txt")
except ZeroDivisionError:
    print("Определитель нулевой и обратная матрица не может быть вычислена!")
    with open("output.txt", "w") as file:
       file.write("Determinant = 0")
except IndexError:
    print("Матрица не квадратная")
    with open("output.txt", "w") as file:
       file.write("matrix is not quadratic")


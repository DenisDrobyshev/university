import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx

import sys

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# ------------------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# ------------------------------------------------------------------------------------
def in_deep_matrix(p, y, x):
    # Возвращает новую матрицу меньшего размера, за вычитом строки и столбца
    return p.drop([y], axis=0).drop([x], axis=1)


# ------------------------------------------------------------------------------------
def reduction_matrix(p):
    # Производим редуцирование матрицы, возвращаем нижнюю границу
    bottom_line = 0

    # Находим минимум по каждой строке и вычитаем его
    for index, row in p.iterrows():
        min = row.min()
        if np.isinf(min):
            return np.inf
        bottom_line += min
        for key, value in row.items():
            p[key][index] -= min

    # Находим минимум по каждому столбцу и вычитаем его
    for key, value in p.items():
        min = value.min()
        if np.isinf(min):
            return np.inf
        bottom_line += min
        for index, row in value.items():
            p[key][index] -= min

    return bottom_line


# ------------------------------------------------------------------------------------
def partition_matrix(p):
    # Ищем элемент для разбиения матрицы на m1 и m2
    # Для этого производим оценку нулевых элементов матрицы
    max_sum = 0
    index_i = None
    index_j = None
    for index, row in p.iterrows():
        for key, value in p.items():
            if p[key][index] == 0:
                min_i = np.inf
                min_j = np.inf

                for k, v in p[key].items():  # по столбецу
                    if k != index and v < min_i:
                        min_i = v

                for k, v in p.loc[index].items():
                    if k != key and v < min_j:
                        min_j = v

                l = min_i + min_j
                if l > max_sum:
                    max_sum = l
                    index_i = index
                    index_j = key

    return [index_i, index_j, max_sum]


# ------------------------------------------------------------------------------------
def reverse_index(l, i, j):
    # Находим обрытный индекс для матрицы
    def in_dict(d, v):
        while v in d:
            v = d[v]
        return v

    ln = len(l)
    d1 = {l[k][0]: l[k][1] for k in range(0, ln, 1)}
    d2 = {l[k][1]: l[k][0] for k in range(0, ln, 1)}
    return [in_dict(d1, i), in_dict(d2, j)]


# ------------------------------------------------------------------------------------
def evaluation_matrix(p, res, bottom_line):
    # Оценка матрицы, поиск решения
    if len(p) == 1:
        res['steps'] += 1
        bottom_line += p.iat[0, 0]

        # Если текущее решение лучше, запоминаем его
        if bottom_line < res['global_min']:
            res['global_min'] = bottom_line
            res['local_result'].append([p.index[0], p.columns[0]])
            res['best_result'] = res['local_result'].copy()
            print('Решение лучше:', bottom_line, res['best_result'], 'шаг: ', res['steps'])
        return

    # Производим редуцирование матрицы, возвращаем минимальную нижнюю границу
    bottom_line += reduction_matrix(p)
    if np.isinf(bottom_line):
        return

    max_sum = 0
    while True:
        res['steps'] += 1
        # Находим элемент для разбиения на подмножества m1 и m2
        i, j, max_sum = partition_matrix(p)
        # Больше нет элементов для разбиения
        if i is None:
            return

        v_len = len(res['local_result'])
        # Рассматриваем m1 (соглашаемся на разбиение по элементу)
        if bottom_line < res['global_min']:
            res['local_result'].append([i, j])
            p1 = in_deep_matrix(p, i, j)
            # Вычёркиваем обратный элемент только для матрицы большей чем 2х2, чтоб не получить inf
            if len(p1) > 2:
                i_reverse, j_reverse = reverse_index(res['local_result'], i, j)
                p1[j_reverse][i_reverse] = np.inf
            evaluation_matrix(p1, res, bottom_line)

        # Рассматриваем m2
        if res['global_min'] < bottom_line + max_sum:
            return
        p[j][i] = np.inf  # Исключаем не выбранный элемент
        res['local_result'] = res['local_result'][:v_len]  # Обрезаем список пути


# ------------------------------------------------------------------------------------
def return_res(res):
    l = res['best_result']
    if l:
        d = {l[k][0]: l[k][1] for k in range(len(l))}
        li = []
        a = l[0][0]
        for v in range(len(l)):
            li.append(a)
            a = d[a]
        return li
    else:
        return []


# ------------------------------------------------------------------------------------
# random.seed(1)
n = 13

v1 = []
points = {}
for i in range(n):
    points[i] = (random.randint(1, 1000), random.randint(1, 1000))

input_matrix = []
for i, vi in points.items():
    m1 = []
    for j, vj in points.items():
        if i == j:
            m1.append(np.inf)
        else:
            m1.append(int(distance(vi[0], vi[1], vj[0], vj[1])))
            v1.append([i, j, int(distance(vi[0], vi[1], vj[0], vj[1]))])
    input_matrix.append(m1.copy())

plt.figure(figsize=(6, 6))
graph = nx.Graph()
graph.add_nodes_from(points)

# Добавляем дуги в граф
for i in v1:
    graph.add_edge(i[0], i[1], weight=i[2])

f1 = pd.DataFrame(input_matrix)

print(f1)
# Инициализация массива решений
res = {'global_min': np.inf, 'best_result': [], 'local_result': [], 'steps': 0}
# Запуск нахождения решения
evaluation_matrix(f1, res, 0)

print('Результат:', res['global_min'], return_res(res), 'всего шагов:', res['steps'])

# Рисуем всё древо
nx.draw(graph, points, width=1, edge_color="#C0C0C0")
# Рисуем оптимальный путь
nx.draw_networkx(graph, points, with_labels=True, edgelist=res['best_result'], arrows=True, edge_color="blue", width=5)

plt.gcf().suptitle('Your Graph')
plt.show()

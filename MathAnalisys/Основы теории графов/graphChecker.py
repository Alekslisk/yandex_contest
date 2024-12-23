import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = int(input())

matrix = []
for i in range(n):
    row = list(map(lambda x: int(x), input().split()))
    matrix.append(row)

matrix = np.array(matrix)

graph = nx.from_numpy_array(matrix)

plt.figure(figsize=(12, 4))
nx.draw(graph, with_labels=True)
plt.title('Из матрицы смежности')
plt.show()
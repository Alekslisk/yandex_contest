import sys
import heapq

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(lambda x: int(x), input().split()))
        matrix.append(row)
    return matrix


def calculate_distance(graph, start, end):

    distance = {node: float('inf') for node in range(len(graph))}
    distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distance[current_node]:
            continue
        
        for neighbor in range(len(graph)):
            weight = graph[current_node][neighbor]
            if weight != 0:  
                new_distance = current_distance + weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    if distance[end] == float('inf'): return -1
    return distance[end] 





def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n = int(input())

    graph = create_matrix(n)
    a, b = map(lambda x: int(x), input().split())
    print(calculate_distance(graph, a, b))



if __name__ == '__main__':
    main()
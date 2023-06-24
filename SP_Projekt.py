import time
import random
import sys
import heapq

def generate_matrix(size, allownegative):
    matrix = [[0] * size for _ in range(size)]
    num_elements = size * size
    num_inf_elements = int(num_elements * 0.4)

    for i in range(size):
        neg_count = 0
        for j in range(size):
            if i != j:
                if allow_negative and neg_count < 1:
                    num_values = random.randint(-1, 20)
                    if num_values < 0:
                        neg_count += 1
                else:
                    num_values = random.randint(1, 20)

                matrix[i][j] = num_values

    inf_indices = random.sample(range(round(num_elements/2)), num_inf_elements)

    for i in range(size):
        for j in range(size):
                if i != j:
                    ind = i * size/2 + j
                    if ind in inf_indices:
                        matrix[i][j] = float('inf')

    return matrix

# Przykładowe użycie
size = int(input("Size of matrix: "))
allow_negative = input("Negative values (T/F): ")

if allow_negative.upper() == 'T':
    allow_negative = True
else:
    allow_negative = False



import heapq

def dijkstra(matrix, start):
    size = len(matrix)
    distances = [float('inf')] * size
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(size):
            weight = matrix[current_vertex][neighbor]
            if weight < 0:  
                print("Negative weight detected. The graph contains negative weights.")
                return True
                

            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def bellman_ford(matrix, start):
    size = len(matrix)
    distances = [float('inf')] * size
    distances[start] = 0

    for _ in range(size - 1):
        any_updates = False  
        for i in range(size):
            for j in range(size):
                if matrix[i][j] != float('inf'):
                    if distances[j] > distances[i] + matrix[i][j]:
                        distances[j] = distances[i] + matrix[i][j]
                        any_updates = True  
        if not any_updates:
            break  

    for i in range(size):
        for j in range(size):
            if matrix[i][j] != float('inf'):
                if distances[j] > distances[i] + matrix[i][j]:
                    print("Negative cycle detected. The graph contains a negative cycle.")
                    return True

    return distances


def floyd_warshall(matrix):
    size = len(matrix)
    distances = matrix

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    for i in range(size):
        if distances[i][i] < 0:
            print("Negative cycle detected. The graph contains a negative cycle.")
            return True

    return distances

# Przykładowe użycie
matrix = generate_matrix(size, allow_negative)
print("Wygenerowana macierz:")
for row in matrix:
    print(row)
start_vertex = 0
count = 0
for row in matrix:
        for num in row:
            if num < 0:
                count += 1
print(count)

# menu glowne --------------------------------------------
print("1. Dijkstra's algorithm")
print("2. Bellmana-Forda-Moora algorithm")
print("3. Floyd-Warshall algorithm ")

while True:
    wybor = input('Select type of algorithm [1-3]: ')
    wybor = int(wybor)
    if wybor == 1:
        start_time = time.time()
        distances = dijkstra(matrix, start_vertex)
        end_time = time.time()
        if distances != True:
            print(f"Shortest distances from vertex {start_vertex}:")
            for i, distance in enumerate(distances):
                print(f"To vertex {i}: {distance}")
            print(f"Czas trwania algorytmu: {end_time - start_time}")

    if wybor == 2:
        start_time = time.time()
        distances = bellman_ford(matrix, start_vertex)
        end_time = time.time()
        if distances != True:
            print(f"Shortest distances from vertex {start_vertex}:")
            for i, distance in enumerate(distances):
                print(f"To vertex {i}: {distance}")
            print(f"Czas trwania algorytmu: {end_time - start_time}")

    if wybor == 3:
        start_time = time.time()
        shortest_paths = floyd_warshall(matrix)
        end_time = time.time()
        if shortest_paths != True:
            print(f"Neighbour Matrix: \n {shortest_paths} \n")
            print(f"Czas trwania algorytmu: {end_time - start_time}")
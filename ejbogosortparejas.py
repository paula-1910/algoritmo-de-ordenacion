import random
import timeit
import heapq

def bogo_sort(arr):
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def heap_sort(arr):
        heapq.heapify(arr) # Convierte la lista en un heap
        return [heapq.heappop(arr) for _ in range(len(arr))]

# Conjuntos de datos
data_random = [random.randint(1, 100) for _ in range(8)]
data_sorted = list(range(1, 9))
data_reversed = list(range(8, 0, -1))

data_large_random = [random.randint(1, 1000) for _ in range(1000)]
data_large_sorted = list(range(1, 1001))
data_large_reversed = list(range(1000, 0, -1))

# Pruebas y medición de tiempo
print("Bogo Sort:")
for dataset, name in zip([data_random, data_sorted, data_reversed], ["Aleatoria", "Ordenada", "Invertida"]):
    print(f"Lista {name}: {dataset}")
    print("Ordenada:", timeit.timeit(lambda: bogo_sort(dataset[:]), number=1), "segundos")

print("\nHeap Sort:")
for dataset, name in zip([data_random, data_sorted, data_reversed], ["Aleatoria", "Ordenada", "Invertida"]):
    print(f"Lista {name}: {dataset[:10]}")
    print("Ordenada en:", timeit.timeit(lambda: heap_sort(dataset[:]), number=1), "segundos")
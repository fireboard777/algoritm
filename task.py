def heapify(arr, n, i):
    largest = i      # Инициализируем наибольший элемент как корень
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Если левый дочерний элемент больше корня
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    # Если правый дочерний элемент больше корня
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Если наибольший элемент не является корнем
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # Меняем местами
        heapify(arr, n, largest)   # Применяем heapify для поддерева

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap (пирамиды)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Меняем местами
        heapify(arr, i, 0)

# Пример использования:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:", arr)

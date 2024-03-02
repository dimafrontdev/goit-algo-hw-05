def binary_search_with_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            upper_bound = mid
            return (iterations, upper_bound)

    if low < len(arr):
        upper_bound = low

    return (iterations, upper_bound)


# Приклад використання
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
x = 2.4
result = binary_search_with_upper_bound(arr, x)
print(f"Кількість ітерацій: {result[0]}, Індекс верхньої межі: {result[1]}")

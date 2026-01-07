# Time complexity: O(n^2)

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[smallest] > arr[j]: smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr
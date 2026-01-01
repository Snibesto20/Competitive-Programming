# Algorithm efficiency: O(n)

def linearSearch(target, arr):
    for i in range(len(arr)):
        if arr[i] == target: return i

    return -1
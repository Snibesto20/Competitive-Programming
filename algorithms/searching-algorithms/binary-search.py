# Algorithm efficiency: O(log n)
# Works on sorted arrays only so linear search can sometimes be a better choice!

target = int(input())
arr = list(map(int, input().split()))

def binarySearch(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        
        if arr[middle] > target: end = middle - 1
        elif arr[middle] < target: start = middle + 1
        else: return middle

    return -1

print(binarySearch(target, arr))
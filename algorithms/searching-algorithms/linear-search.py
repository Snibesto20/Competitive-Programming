# Algorithm efficiency: O(n)

target = int(input())
arr = list(map(int, input().split()))

def linearSearch(target, arr):
    for i in range(len(arr)):
        if arr[i] == target: return i

    return -1

print(linearSearch(target, arr))
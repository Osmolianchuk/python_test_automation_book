# TASK 1
def bubbleSortAscending(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def bubbleSortDescending(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
def bubbleSortStop(arr):
    for i in range(len(arr)):
        stop = False;
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                Stop = True;
        if Stop = False:
          break;
# TASK 2
cache = {}
def square(n):
    if n in cache:
        return cache[n]
    result = n * n
    cache[n] = result
    return result
# TASK 3



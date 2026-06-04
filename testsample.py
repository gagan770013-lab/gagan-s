def linear_search(list, n, key):
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1

list = [9, 12, 15, 37, 28, 30]
n = len(string)
key = 9

result = linear_search(list, n, key)
if (result == -1):
    print("Element not found")
else
    print("Element found at the position", result + 1)

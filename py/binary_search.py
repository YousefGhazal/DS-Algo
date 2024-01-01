def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        # print(arr[mid])
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

# if result != -1:
#     print("element is present at index", result)
# else:
#     print("element is not present in array")
# a = "abcd"
# def string_to_binary(a):
#     return ' '.join(format(ord(c), '08b') for c in a)


words = ["abcd", "dbca", "dddd"]
for i in range(len(words)):
    res = sum(ord(char) for char in words[i])
    print(res)

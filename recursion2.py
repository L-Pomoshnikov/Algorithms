def factorial(x):
    if x == 1:
        res = 1
    else:
        res = x * factorial(x-1)
    return res

# x = int(input())
# print(factorial(x))

def sum(arr):
    if len(arr) == 1:
        res = arr[0]
    else:
        res = arr[0] + sum(arr[1:len(arr)])
    return res

# a = [4,5,8,10,1]
# print(sum(a))
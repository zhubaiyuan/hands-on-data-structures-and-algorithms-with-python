def iterTest(low, high):
    while low <= high:
        print(low)
        low += 1


print("print values using iteration")
iterTest(2, 10)


def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest(low + 1, high)


print("print values using recursion")
recurTest(2, 10)

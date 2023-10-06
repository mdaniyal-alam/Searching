array = ["a", "b", "e", "i", "p", "s", "z"]


def bisearch(array):
    size = len(array)
    ub = size - 1
    lb = 0

    value = input("Enter the value you want to search: ")

    while lb <= ub:
        mid = (lb + ub) // 2
        if array[mid] == value:
           print("The value was found at location", mid)
           break
        elif array[mid] > value:
           ub = mid - 1
        else:
           lb = mid + 1


bisearch(array)

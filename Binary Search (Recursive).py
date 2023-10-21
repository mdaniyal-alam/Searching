
def bisearch(ub, lb, array, value):
    mid = (lb + ub) // 2

    if array[mid] == value:
        print("The value was found on location ", mid)
    elif array[mid] > value:
        return bisearch(mid - 1, lb, array, value)
    else:
        return bisearch(ub, mid + 1, array, value)


array = ['a', 'b', 'h', 'j', 'p', 'y']
val = input("Enter the value to search: ")
ub = len(array) - 1
lb = 0

bisearch(ub, lb, array, val)


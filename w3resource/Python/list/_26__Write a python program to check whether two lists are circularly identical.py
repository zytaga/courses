# 26. Write a python program to check whether two lists are circularly identical.

def fun(item1, item2):
    if len(item1) != len(item2):
        return False

    # find the smallest number of list1
    smallest = min(item1)
    # set both lists to the smallest number and start looping and comparing
    list1 = []
    list2 = []

    beforeSmallest = []
    smallestFound = False
    for x in item1:
        if smallestFound == True:
            list1.append(x)
        if smallestFound == False:
            beforeSmallest.append(x)
            if x == smallest:
                smallestFound = True

    list1 = list1 + beforeSmallest

    beforeSmallest = []
    smallestFound = False
    for x in item2:
        if smallestFound == True:
            list2.append(x)
        if smallestFound == False:
            beforeSmallest.append(x)
            if x == smallest:
                smallestFound = True

    list2 = list2 + beforeSmallest

    for x in range(0, len(list1) - 1):
        if list1[x] != list2[x]:
            return False
    return True


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 0, 4, 1], [3, 0, 4, 1, 2]) == False
    assert fun([1, 2, 3, 0, 4], [3, 0, 4, 1, 2]) == True
    assert fun([10, 10, 0, 0, 10], [10, 10, 10, 0, 0]) == True
    assert fun([10, 10, 10, 0, 0], [1, 10, 10, 0, 0]) == False

    print('Testing completed!')
def binary_search(list, searchItem):
    lowIndex = 0
    highIndex = len(list) - 1

    while lowIndex <= highIndex:
        midIndex = (lowIndex + highIndex)
        guessItem = list[midIndex]

        if guessItem == searchItem:
            return midIndex

        if guessItem > searchItem:
            highIndex = midIndex - 1
        else:
            lowIndex = midIndex + 1
    return None


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        smallestElement = arr.pop(smallest)
        newArr.append(smallestElement)
    return newArr


def quicksort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        numberLessThanPivot = [i for i in arr[1:] if i <= pivot]
        numberGreaterThanPivot = [i for i in arr[1:] if i > pivot]

        return quicksort(numberLessThanPivot) + [pivot] + quicksort(numberGreaterThanPivot)

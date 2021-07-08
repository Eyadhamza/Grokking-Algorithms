def binary_search(list,searchItem):
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


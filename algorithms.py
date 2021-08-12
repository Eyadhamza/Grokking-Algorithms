from collections import deque


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
        numbersLessThanPivot = [i for i in arr[1:] if i <= pivot]
        numbersGreaterThanPivot = [i for i in arr[1:] if i > pivot]

        return quicksort(numbersLessThanPivot) + [pivot] + quicksort(numbersGreaterThanPivot)


def breadth_first_search(graph, name):
    search_queue = deque()

    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if personIsSeller(person):

                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def personIsSeller(person):
    return person[-1] == 'm'



def dijkstraGraph():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}
    infinity = float("inf")
    costs = {"a": 6, "b": 2, "fin": infinity}
    parents = {"a": "start", "b": "start", "fin": None}
    processed = []

    node = find_lowest_cost_node(costs,processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)
        return parents


def find_lowest_cost_node(costs,processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

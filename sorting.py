def partition(elements, low, high):
    pivot = elements[high]
    position = high


def swap(elements, left, right):
    temp = elements[left]
    elements[left] = elements[right]
    elements[right] = temp


def bubble_sort(elements):
    for index in range(1, len(elements)):
        for left in range(0, len(elements)-index):
            right = left + 1
            if elements[left] > elements[right]:
                swap(elements, left, right)


def insertion_sort(elements):
    # insert to a new list
    result = []

    for x in elements:
        if len(result) > 0:
            for pos in range(0, len(result)+1):
                if pos == len(result):
                    result.append(x)
                elif x < result[pos]:
                    result.insert(pos, x)
                    break
        else:
            result.append(x)

    return result


def testing():
    record1 = [86, 33, 92, 58, 9, 12, 445, 87]
    print insertion_sort(record1)

    bubble_sort(record1)
    print "Bubble Sort:" + str(record1) + "!"



testing()
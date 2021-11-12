
def bubble_sort(list):
    # we assume that with each new iteration the highest number will be in the end of the list
    # hence we can decrement total number of iterations by one
    for totalNumberOfIterations in range(len(list) - 1, 0, -1):
        for index in range(totalNumberOfIterations):
            # if the number at given index is higher than the number next to it we move it one index forward
            # hence that number can go thru all list until the end if it doesn't face any number higher that it is
            # or it will be left behind and we start compare next value
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp
    return list

list = [1, 2, 3, 4, 5, 7, 6]
print(bubble_sort(list))
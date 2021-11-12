def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        prev_index = i-1
        while temp < list[prev_index] and prev_index > -1:
            list[prev_index+1] = list[prev_index]
            list[prev_index] = temp
            prev_index -= 1
    return list

list = [2, 1, 3, 4, 6, 5]
print(insertion_sort(list))
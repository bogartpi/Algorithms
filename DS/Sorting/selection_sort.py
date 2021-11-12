def selection_sort(list):
    for index in range(len(list)-1):
        min_index = index
        for next_index in range(index+1, len(list)):
            if list[next_index] < list[min_index]:
                min_index = next_index
        if index != min_index:
            temp = list[index]
            list[index] = list[min_index]
            list[min_index] = temp
    return list

list = [4,1,3,6,5,7,2]
print(selection_sort(list))
        
# both lists should be sorted
def merge(list1, list2):
    i = 0
    j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i < len(list1):
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1 
    return combined

# 0(n log n) - time complexity 
def merge_sort(list):
    if len(list) == 1:
        return list
    mid = int(len(list)/2)
    left = list[:mid]
    right = list[mid:]
    return merge(merge_sort(left), merge_sort(right))
    
list = [5, 8, 1, 4, 7, 9, 6, 3, 2, 10]

print(merge_sort(list))
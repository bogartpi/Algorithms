list1 = [1,3,5]
list2 = [2,4,5]

# O(n) - find if there are common items in 2 lists

def item_in_common(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
    for j in list2:
        if j in dict:
            return True
    return False

print(item_in_common(list1, list2))
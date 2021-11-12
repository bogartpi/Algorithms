class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def print_table(self):
        for container in self.data_map:
            print(container)
    
    def hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.hash(key)
        container = self.data_map[index]
        if container:
            for i in range(len(container)):
                if container[i][0] == key:
                    return container[i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            container = self.data_map[i]
            if container:
                for j in range(len(container)):
                    keys.append(self.data_map[i][j][0])
        print(keys)



ht = HashTable()

ht.set_item('bolts', 1000)
ht.set_item('washers', 50)
ht.set_item('lumber', 70)

ht.print_table()

ht.keys()
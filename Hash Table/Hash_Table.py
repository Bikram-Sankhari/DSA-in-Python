class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []

        for item in self.data_map[index]:
            if item[0] == key:
                item[1] = value
                return

        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]

        return None

    def keys(self):
        all_keys = []
        for items in self.data_map:
            if items:
                for inner_item in items:
                    all_keys.append(inner_item[0])

        return all_keys


my_hash = HashTable()

my_hash.set_item('pen', 4)
my_hash.set_item('pencil', 5)

my_hash.set_item('pen', 8)
print(my_hash.keys())

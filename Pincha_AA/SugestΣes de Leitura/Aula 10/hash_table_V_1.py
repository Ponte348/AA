#
#   A "toy" hash table class
#
#   J. Madeira - November 2016
#
#   Adapted from:
#
#   Problem Solving with Algorithms and Data Structures using Python
#   Brad Miller and David Ranum
#   http://interactivepython.org/
#  


class HashTable:

    def __init__(self, size=17):

        self.size = size
        self.slots = [None] * self.size     # to store the keys
        self.data = [None] * self.size

    def __getitem__(self, key):

        return self.get(key)

    def __setitem__(self, key, data):

        self.put(key, data)

    def hash_function(self, key):

        return key % self.size

    def new_hash(self, old_hash):

        return (old_hash + 1) % self.size

    def put(self, key, data):

        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                # look for an empty slot

                next_slot = self.new_hash(hash_value)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.new_hash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):

        start_slot = self.hash_function(key)

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.new_hash(position)
                if position == start_slot:
                    stop = True
        return data


def main(args):

    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(H.slots)
    print(H.data)

    print(H[20])
    print(H[17])


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

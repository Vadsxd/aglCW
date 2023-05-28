class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hash_function(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = [key, data]
            self.resize()
        else:
            if self.slots[hashvalue][0] == key:
                self.slots[hashvalue][1] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot][0] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = [key, data]
                    self.resize()

                else:
                    self.slots[nextslot][1] = data

    @staticmethod
    def hash_function(key, size):
        if type(key) == str:
            str_hash = 0
            for i in range(len(key)):
                str_hash = (257 * str_hash + ord(key[i])) % 11
            return str_hash
        return key % size

    @staticmethod
    def rehash(oldhash, size):
        return (oldhash + 1) % size

    def find(self, key):
        startslot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position][0] == key:
                found = True
                data = self.slots[position][1]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def delete(self, key):
        hashvalue = self.hash_function(key, len(self.slots))
        self.slots[hashvalue] = None

    def resize(self):
        self.size += 1
        self.slots.append(None)

    def get_table(self):
        return self.slots

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, data):
        self.put(key, data)

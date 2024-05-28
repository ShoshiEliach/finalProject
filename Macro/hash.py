class HashTableOfLists:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if stored_key == key:
                    return value
        return None

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    self.table[index].remove(item)
                    return

#def main():
    #print("Hash calculation completed successfully.")
    #print("Result: 12345")

#if __name__ == "__main__":
    #main()

# # Create a hash table of lists with size 10
# hash_table = HashTableOfLists(10)
#
# # Insert values into the hash table
# hash_table.insert('apple', 5)
# hash_table.insert('banana', 10)
# hash_table.insert('cherry', 15)
# hash_table.insert('apple', 20)  # Adding another value for the key 'apple'
#
# # Search for values in the hash table
# print(hash_table.search('banana'))  # Output: 10
# print(hash_table.search('apple'))   # Output: [5, 20]
#
# # Delete a key-value pair from the hash table
# hash_table.delete('banana')
#
# # Search again after deletion
# print(hash_table.search('banana'))  # Output: None

from __future__ import annotations

from __future__ import annotations


class HashTable:
    """
    A HashTable implementation using separate chaining for collision resolution.

    The HashTable supports storing (key, value) pairs where the key can be either an integer or a string.
    The hash table resizes itself when the int of elements exceeds half of its capacity.
    """

    def __init__(self, capacity: int):
        """
        Initializes a hash table with a given initial capacity.

        Args:
            capacity (int): The initial capacity of the hash table, defining the int of buckets.

        Attributes:
            capacity (int): The int of buckets in the hash table.
            no_elems (int): The current int of elements in the hash table.
            list_of_lists (list of lists): A list where each index contains a list of key-value pairs.

        Example:
            >>> ht = HashTable(10)
            >>> print(ht.capacity)  # 10
            >>> print(ht.list_of_lists)  # [[], [], [], [], [], [], [], [], [], []]
        """
        self.capacity = capacity
        self.no_elems = 0
        self.list_of_lists = []
        for key in range(capacity):
            self.list_of_lists.append([])

    def hash_function(self, key: int | str) -> int:
        """
        Computes the hash value for the given key.

        If the key is an integer, it returns the modulo of the key by the table's capacity.
        If the key is a string, it computes the sum of the ASCII values of its characters
        and takes the modulo of that sum by the table's capacity.

        Args:
            key (int | str): The key to hash, which can be an integer or string.

        Returns:
            int: The computed hash value for the key.

        Example:
            >>> ht = HashTable(10)
            >>> ht.hash_function(15)  # 15 % 10 == 5
            5
            >>> ht.hash_function("key")  # sum(ord(c) for c in "key") % 10
            7
        """
        if isinstance(key, int):
            return key % self.capacity
        return sum([ord(car) for car in key]) % self.capacity

    def insert(self, key: int | str, value: int | str):
        """
        Inserts a (key, value) pair into the hash table.

        If the int of elements in the table exceeds half of its capacity, the table will be resized
        and all the elements will be rehashed into the new structure.

        Args:
            key (int | str): The key associated with the value, which can be an integer or string.
            value (int): The value to store in the hash table.

        Example:
            >>> ht = HashTable(10)
            >>> ht.insert(1, 100)
            >>> ht.insert("name", 200)
        """
        if self.no_elems > self.capacity // 2:
            self.resize_and_rehash()
        hash_value = self.hash_function(key)
        self.list_of_lists[hash_value].append((key, value))
        self.no_elems += 1

    def resize_and_rehash(self):
        """
        Resizes the hash table by doubling its capacity and rehashes all existing elements.

        This function is triggered automatically when the int of elements exceeds half the capacity.
        All elements from the original hash table are rehashed and inserted into a new list structure
        with the updated capacity.

        Example:
            >>> ht = HashTable(5)
            >>> ht.insert(1, 100)
            >>> ht.insert(2, 200)
            >>> ht.insert(3, 300)
            >>> ht.insert(4, 400)  # This should trigger resize
            >>> print(ht.capacity)  # 10
        """
        self.capacity *= 2
        new_list = [[] for _ in range(self.capacity)]

        # Rehash and redistribute elements into the new list
        for bucket in self.list_of_lists:
            for elem in bucket:
                hash_value = self.hash_function(elem[0])
                new_list[hash_value].append(elem)

        self.list_of_lists = new_list

    def delete(self, key: int | str):
        """
        Deletes the key-value pair associated with the given key from the hash table.

        If the key exists in the hash table, its corresponding pair is removed. If the key does
        not exist, the function does nothing.

        Args:
            key (int | str): The key to be deleted.

        Example:
            >>> ht = HashTable(10)
            >>> ht.insert(1, 100)
            >>> ht.delete(1)
            >>> print(ht.get(1))  # None
        """
        hash_value = self.hash_function(key)
        bucket = self.list_of_lists[hash_value]
        for i, elem in enumerate(bucket):
            if elem[0] == key:
                del bucket[i]
                self.no_elems -= 1
                return

    def get(self, key: int | str) -> int | None:
        """
        Retrieves the value associated with the given key in the hash table.

        If the key exists, it returns the corresponding value. If the key does not exist,
        it returns `None`.

        Args:
            key (int | str): The key whose value is to be retrieved.

        Returns:
            int | None: The value associated with the key, or None if the key is not found.

        Example:
            >>> ht = HashTable(10)
            >>> ht.insert(1, 100)
            >>> ht.get(1)  # 100
            >>> ht.get(2)  # None
        """
        hash_value = self.hash_function(key)
        for elem in self.list_of_lists[hash_value]:
            if elem[0] == key:
                return elem[1]
        return None

    def get_all_elements(self):
        """
        Retrieves all elements from the hash table.

        Returns:
            list: A list containing all elements from the hash table.

        Example:
            >>> ht = HashTable(10)
            >>> ht.insert(1, 100)
            >>> ht.insert("name", 200)
            >>> ht.get_all_elements()  # [(1, 100), ("name", 200)]
        """
        all_elements = []
        for bucket in self.list_of_lists:
            all_elements.extend(bucket)
        return all_elements


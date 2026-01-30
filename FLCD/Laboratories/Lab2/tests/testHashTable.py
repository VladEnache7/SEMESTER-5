import unittest

from Lab2.models.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_initialization(self):
        ht = HashTable(10)
        self.assertEqual(ht.capacity, 10)
        self.assertEqual(ht.no_elems, 0)
        self.assertEqual(len(ht.list_of_lists), 10)
        for lst in ht.list_of_lists:
            self.assertEqual(lst, [])

    def test_insert_and_get(self):
        ht = HashTable(10)
        ht.insert(1, 100)
        ht.insert("key", 200)
        ht.insert(15, 300)  # This should hash to the same index as 1 (15 % 10 == 1 % 10)

        self.assertEqual(ht.get(1), 100)
        self.assertEqual(ht.get("key"), 200)
        self.assertEqual(ht.get(15), 300)

    def test_resize_and_rehash(self):
        ht = HashTable(5)
        ht.insert(1, 100)
        ht.insert(2, 200)
        ht.insert(3, 300)
        ht.insert(4, 400)
        ht.insert(5, 500)  # Trigger resize and rehash

        self.assertEqual(ht.capacity, 10)  # The capacity should now be doubled
        self.assertEqual(ht.get(1), 100)
        self.assertEqual(ht.get(2), 200)
        self.assertEqual(ht.get(3), 300)
        self.assertEqual(ht.get(4), 400)
        self.assertEqual(ht.get(5), 500)

    def test_delete(self):
        ht = HashTable(10)
        ht.insert(1, 100)
        ht.insert("key", 200)
        ht.insert(15, 300)

        # Delete existing key
        ht.delete(1)
        self.assertIsNone(ht.get(1))  # Should return None since it's deleted

        # Delete non-existing key
        ht.delete("non_existing_key")
        self.assertIsNone(ht.get("non_existing_key"))  # Nothing to delete, should still be None

        # Ensure other keys are not affected
        self.assertEqual(ht.get("key"), 200)
        self.assertEqual(ht.get(15), 300)

    def test_insert_duplicate_key(self):
        ht = HashTable(10)
        ht.insert(1, 100)
        ht.insert(1, 200)  # Insert the same key with a different value

        # In this case, it should append both values, but the expected behavior for updating
        # is not defined in your class. You might need to handle duplicates in the insert method.
        self.assertEqual(ht.get(1), 100)  # The first inserted value is retrieved (not overridden)

    def test_hash_function(self):
        ht = HashTable(10)

        # Test hash function for integers
        self.assertEqual(ht.hash_function(1), 1 % 10)
        self.assertEqual(ht.hash_function(15), 15 % 10)

        # Test hash function for strings
        self.assertEqual(ht.hash_function("key"), sum([ord(c) for c in "key"]) % 10)
        self.assertEqual(ht.hash_function("another_key"), sum([ord(c) for c in "another_key"]) % 10)


if __name__ == '__main__':
    unittest.main()

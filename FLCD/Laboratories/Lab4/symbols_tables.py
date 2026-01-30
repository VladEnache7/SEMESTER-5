from Lab2.models.hash_table import HashTable


class SymbolTable:
    def __init__(self):
        self.hash_table = HashTable(10)

    def add(self, key, value):
        self.hash_table.insert(key, value)

    def get(self, key):
        return self.hash_table.get(key)

    def get_all(self):
        return self.hash_table.get_all_elements()


class SymbolTableConstants:
    def __init__(self):
        self.hash_table = HashTable(10)

    def add(self, key, value):
        self.hash_table.insert(key, value)

    def get(self, key):
        return self.hash_table.get(key)

    def get_all(self):
        return self.hash_table.get_all_elements()

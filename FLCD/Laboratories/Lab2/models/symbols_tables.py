from Lab2.models.hash_table import HashTable


class SymbolTableIdentifiers:
    def __init__(self):
        self.hash_table = HashTable(10)

    def add_identifier(self, key, value):
        self.hash_table.insert(key, value)

    def get_identifier_value(self, key):
        return self.hash_table.get(key)

    def get_all_identifiers(self):
        return self.hash_table.get_all_elements()


class SymbolTableConstants:
    def __init__(self):
        self.hash_table = HashTable(10)

    def add_constant(self, key, value):
        self.hash_table.insert(key, value)

    def get_constant(self, key):
        return self.hash_table.get(key)

    def get_all_constants(self):
        return self.hash_table.get_all_elements()

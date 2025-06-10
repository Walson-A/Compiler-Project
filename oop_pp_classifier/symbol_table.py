class SymbolTable:
    def __init__(self):
        self.symbols = []

    def add(self, token_type, value):
        self.symbols.append({'type': token_type, 'value': value})

    def get_symbols(self):
        return self.symbols

    def __str__(self):
        return '\n'.join(f"{sym['type']}: {sym['value']}" for sym in self.symbols)

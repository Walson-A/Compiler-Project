import re
from symbol_table import SymbolTable

class Scanner:
    token_specs = [
        ('CLASS', r'\bclass\b'),
        ('EXTENDS', r'\bextends\b'),
        ('PUBLIC', r'\bpublic\b'),
        ('PRIVATE', r'\bprivate\b'),
        ('THIS', r'\bthis\b'),
        ('NEW', r'\bnew\b'),
        ('DEF', r'\bdef\b'),
        ('FUNC', r'\bfunction\b'),
        ('IDENT', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SEMICOLON', r';'),
        ('SKIP', r'[ \t\n]+'),
        ('MISMATCH', r'.'),  # Error
    ]

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specs))

    def scan(self, code):
        tokens = []
        for match in self.regex.finditer(code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise ValueError(f"Illegal character: {value}")
            else:
                tokens.append((kind, value))
                self.symbol_table.add(kind, value)
        return tokens, self.symbol_table

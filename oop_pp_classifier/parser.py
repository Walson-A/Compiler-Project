class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.oop_found = False
        self.pp_found = False

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def match(self, expected_type):
        if self.current_token()[0] == expected_type:
            self.pos += 1
            return True
        else:
            raise SyntaxError(f"Expected {expected_type} but found {self.current_token()[0]}")

    def parse(self):
        while self.current_token()[0] != 'EOF':
            if self.current_token()[0] == 'CLASS':
                self.oop_found = True
                self.parse_class()
            elif self.current_token()[0] in ['DEF', 'FUNC']:
                self.pp_found = True
                self.parse_function()
            else:
                self.pos += 1

        if self.oop_found and self.pp_found:
            return 'Hybrid'
        elif self.oop_found:
            return 'Object-Oriented'
        elif self.pp_found:
            return 'Procedural'
        else:
            return 'Unknown'

    def parse_class(self):
        self.match('CLASS')
        self.match('IDENT')
        if self.current_token()[0] == 'EXTENDS':
            self.match('EXTENDS')
            self.match('IDENT')
        self.match('LBRACE')

        while self.current_token()[0] not in ['RBRACE', 'EOF']:
            self.pos += 1

        if self.current_token()[0] == 'RBRACE':
            self.match('RBRACE')
        else:
            raise SyntaxError("Missing closing brace '}' for class declaration.")

    def parse_function(self):
        self.match(self.current_token()[0])  # DEF or FUNC
        self.match('IDENT')
        self.match('LPAREN')

        while self.current_token()[0] not in ['RPAREN', 'EOF']:
            self.pos += 1

        if self.current_token()[0] == 'RPAREN':
            self.match('RPAREN')
        else:
            raise SyntaxError("Missing closing parenthesis ')' in function declaration.")

        self.match('LBRACE')

        while self.current_token()[0] not in ['RBRACE', 'EOF']:
            self.pos += 1

        if self.current_token()[0] == 'RBRACE':
            self.match('RBRACE')
        else:
            raise SyntaxError("Missing closing brace '}' in function body.")

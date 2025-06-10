from scanner import Scanner
from parser import Parser

def classify_code(filename):
    try:
        with open(filename, 'r') as f:
            code = f.read()

        scanner = Scanner()
        tokens, symbol_table = scanner.scan(code)

        parser = Parser(tokens)
        classification = parser.parse()

        print(f"\n--- File: {filename} ---")
        print("Classification:", classification)
        print("\nSymbol Table:")
        print(symbol_table)

    except Exception as e:
        print(f"Error while processing {filename}: {e}")

if __name__ == '__main__':
    files = ['test_cases/oop_sample.txt', 'test_cases/pp_sample.txt', 'test_cases/hybrid_sample.txt']
    for file in files:
        classify_code(file)

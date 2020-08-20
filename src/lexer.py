
class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []

        source_code = self.source_code.split()

        source_index = 0

        for i in source_code:
            print(i)
            source_index += 1

        return tokens

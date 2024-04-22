from typing import Final
from token import Token
KEYWORDS: Final = ('print', 'read', 'write', 'open', 'close', 'input')
LITERALS: Final = ('True', 'False', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
OPERATORS: Final = ('+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=', '+=', '-=', '*=', '/=', 'substring', 'search', 'replace')
DELIMITERS: Final = ('(', ')', '[', ']', '{', '}', ',', ';', ':', '.')
COMMENTS: Final = """#"""
STRING_TOKENS: Final = '''"'''


class Tokenizer:
    code: str = """"""

    def __init__(self, code: str) -> None:
        self.code = code

    def tokenization(self) -> list[Token]:
        tokens: list[Token] = []
        string_token_position: list[int, int] = [0, 0]
        for stroke in self.code.split('\u000A'):
            first: bool = False
            second: bool = False
            for element in stroke.split(' '):
                if len(element):
                    start_position: int = stroke.index(element[0])
                    end_position: int = stroke.index(element[-1])
                if COMMENTS in element:
                    comment_stroke: str = stroke[stroke.index(element):]
                    ind = comment_stroke.index(COMMENTS)
                    comment_stroke = comment_stroke.replace(comment_stroke[0:ind], """""")
                    tokens.append(Token('COMMENT', comment_stroke, (start_position + ind, len(stroke))))
                    break
                if STRING_TOKENS in element and not first:
                    string_token_position[0] = element.index(STRING_TOKENS) + stroke.index(element)
                    first = True
                elif STRING_TOKENS in element and not second:
                    string_token_position[1] = element.index(STRING_TOKENS) + stroke.index(element) + 1
                    second = True
                if element in KEYWORDS:
                    tokens.append(Token('KEYWORD', element, (start_position, end_position)))
                elif element.isnumeric():
                    tokens.append(Token('LITERAL', element, (start_position, end_position)))
                elif element in LITERALS:
                    tokens.append(Token('LITERAL', element, (start_position, end_position)))
                elif element in OPERATORS:
                    tokens.append(Token('OPERATOR', element, (start_position, end_position)))
                elif element in DELIMITERS:
                    tokens.append(Token('DELIMITER', element, (start_position, end_position)))
                else:
                    if '"' not in element:
                        tokens.append(Token('IDENTIFIER', element, (start_position, end_position)))
            else:
                tokens.append(Token('STRING', stroke[string_token_position[0]: string_token_position[1]], tuple(string_token_position)))
        return tokens

    def string_tokenization(self) -> list[Token]:
        tokens: list[Token] = []
        string_token_position: list[int, int] = [0, 0]
        for stroke in self.code.split('\u000A'):
            first: bool = False
            second: bool = False
            for element in stroke.split(' '):
                if STRING_TOKENS in element and not first:
                    print(element)
                    string_token_position[0] = element.index(STRING_TOKENS) + stroke.index(element)
                    first = True
                elif STRING_TOKENS in element and not second:
                    print(element)
                    string_token_position[1] = element.index(STRING_TOKENS) + stroke.index(element) + 1
                    second = True
            else:
                tokens.append(Token('STRING', stroke[string_token_position[0]: string_token_position[1]], tuple(string_token_position)))
        else:
            return tokens


if __name__ == """__main__""":
    cd: str = open('test.txt', 'r+').read()
    t = Tokenizer(cd)
    t.tokenization()
    result: list = t.tokenization()
    for elem in result:
        print(str(elem))

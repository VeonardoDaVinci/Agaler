import os
import lexer

def main():
    os.chdir(r'D:\Moje Pliki\Python\Agaler\src')
    #Read the content of the  Agaler snippet file
    content=""
    with open('test.lang', 'r') as file:
        content = file.read()

    lex = lexer.Lexer(content)

    tokens = lex.tokenize()

main()

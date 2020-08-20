
def main():
    #Read the content of the  Agaler snippet file
    content=""
    with open('test.lang', 'r') as file:
        content = file.read()
    print(content)

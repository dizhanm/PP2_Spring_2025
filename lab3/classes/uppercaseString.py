class MyClass:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter string: ")

    def printString(self):
        print(self.text.upper())
strUp = MyClass()
strUp.getString()
strUp.printString()

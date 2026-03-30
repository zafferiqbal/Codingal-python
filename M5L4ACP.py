class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reverse(self):
        return self.s[::-1]

word = input("Enter a word: ")
obj = Reverse(word)

print("Reversed string:", obj.get_reverse())
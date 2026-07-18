class ReverseString:
    def __init__(self, text):
        self.__text = text      # private data member

    def reverse_words(self):
        words = self.__text.split()
        return " ".join(words[::-1])

    def __str__(self):
        return self.reverse_words()


# Example usage
s = ReverseString("Python is easy to learn")
print(s)
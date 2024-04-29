class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class BidirectionalIterator:
    def __init__(self, data):
        self.data = data
        self.forward_iterator = iter(data)
        self.reverse_iterator = ReverseIterator(data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.forward_iterator)
        except StopIteration:
            return next(self.reverse_iterator)

if __name__ == "__main__":
    text = "Holis"
    bidirectional_iter = BidirectionalIterator(text)

    print("Recorrido directo:")
    for char in bidirectional_iter:
        print(char, end=" ")

    print("\nRecorrido inverso:")
    for char in reversed(text):
        print(char, end=" ")

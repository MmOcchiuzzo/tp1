class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, number):
        if self.successor:
            return self.successor.handle_request(number)
        else:
            return f"El número {number} no fue consumido."

class PrimeHandler(Handler):
    def handle_request(self, number):
        if self.is_prime(number):
            return f"El número {number} fue consumido por el manejador de números primos."
        else:
            return super().handle_request(number)

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

class EvenHandler(Handler):
    def handle_request(self, number):
        if number % 2 == 0:
            return f"El número {number} fue consumido por el manejador de números pares."
        else:
            return super().handle_request(number)

class NumberProcessor:
    def __init__(self):
        self.chain = PrimeHandler(EvenHandler())

    def process_numbers(self, start=1, end=100):
        results = []
        for num in range(start, end + 1):
            results.append(self.chain.handle_request(num))
        return results

if __name__ == "__main__":
    processor = NumberProcessor()
    results = processor.process_numbers()
    for result in results:
        print(result)

class Greeter:
    def __init__(self, greeter):
        self.greeter = greeter
    def greet(self):
        return self.greeter.greet()
class EnglishGreeter:
    def greet(self):
        return 'Hello!'


class SpanishGreeter:
    def greet(self):
        return '¡Hola!'


class FrenchGreeter:
    def greet(self):
        return 'Bonjour!'


# Membuat objek greeter dalam berbagai bahasa
english_greeter = EnglishGreeter()
spanish_greeter = SpanishGreeter()
french_greeter = FrenchGreeter()
# Membuat objek Greeter dan menggreet dalam berbagai bahasa
greeter = Greeter(english_greeter)
print(greeter.greet()) # Output: Hello!

greeter = Greeter(spanish_greeter)
print(greeter.greet()) # Output: ¡Hola!

greeter = Greeter(french_greeter)
print(greeter.greet()) # Output: Bonjour!
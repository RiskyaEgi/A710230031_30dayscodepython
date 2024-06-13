class Bird:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I'm a {self.name}."
class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"


class NonFlyingBird(Bird):
    def walk(self):
        return "I can walk!"


class Duck(FlyingBird):
    def quack(self):
        return "Quack!"


class Ostrich(NonFlyingBird):
    def run(self):
        return "I can run fast!"


# Membuat objek Duck dan Ostrich
duck = Duck("Duck")
ostrich = Ostrich("Ostrich")

# Duck bisa terbang dan berbunyi "quack"
print(duck.introduce()) # Output: Hello, I'm a Duck.
print(duck.fly()) # Output: I can fly!
print(duck.quack()) # Output: Quack!

# Ostrich tidak bisa terbang, dan bisa berjalan dan berlari cepat
print(ostrich.introduce()) # Output: Hello, I'm an Ostrich.
print(ostrich.walk()) # Output: I can walk!
print(ostrich.run()) # Output: I can run fast!
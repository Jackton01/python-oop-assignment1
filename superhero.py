# Base class
class Superhero:
    def __init__(self, name, superpower, age):
        self.name = name        # Attribute for hero's name
        self.superpower = superpower  # Attribute for hero's main power
        self.age = age          # Attribute for hero's age

    def introduce(self):
        print(f"Hi, I am {self.name}, I have the power of {self.superpower}!")

    def fight(self):
        print(f"{self.name} is fighting the villains with {self.superpower}!")

# Child class inheriting from Superhero


class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, age, flight_speed):
        super().__init__(name, superpower, age)  # Call the parent constructor
        self.flight_speed = flight_speed          # Unique attribute for FlyingSuperhero

    # Polymorphism: Overriding the fight method
    def fight(self):
        print(
            f"{self.name} is soaring at {self.flight_speed} km/h while fighting villains!")

    # New method unique to this subclass
    def fly(self):
        print(f"{self.name} is flying through the sky at {self.flight_speed} km/h!")

# Another child class to show encapsulation


class SecretSuperhero(Superhero):
    def __init__(self, name, superpower, age, secret_identity):
        super().__init__(name, superpower, age)
        # Private attribute (encapsulation)
        self.__secret_identity = secret_identity

    # Getter method to access private attribute
    def reveal_identity(self):
        print(f"My secret identity is {self.__secret_identity}.")


# Creating objects
hero1 = Superhero("IronMind", "Telepathy", 28)
hero2 = FlyingSuperhero("SkyBlazer", "Super Strength", 25, 300)
hero3 = SecretSuperhero("ShadowStrike", "Invisibility", 30, "John Doe")

# Using methods
hero1.introduce()
hero1.fight()

hero2.introduce()
hero2.fight()  # Uses overridden method
hero2.fly()    # Unique method

hero3.introduce()
hero3.reveal_identity()

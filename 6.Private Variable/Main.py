class Hero:
    # class varible (static variable)
    amount = 0
    # private class varible (static variable)
    __privateAmount = 0

    def __init__(self, name, health, power) -> None:
        # instance variable
        self.name = name
        self.health = health
        self.power = power
        Hero.amount += 1
        # private instance variable
        self.__private = "private"
        # protected instance variable
        self._protected = "protected"

    # void method
    def who(self):
        print(f"This hero name is {self.name}")

    # method with parameter
    def powerBuff(self, buff):
        self.health += buff

    # method with return
    def getPower(self):
        return self.power


# initiate object
h1 = Hero("Saber", 100, 15)
h2 = Hero("Lancelot", 80, 18)
print("\n")

# accessing public method
print(h1.__dict__)

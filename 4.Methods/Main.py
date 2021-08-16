class Hero:
    # class varible (static variable)
    amount = 0

    def __init__(self, name, health, power) -> None:
        # instance variable
        self.name = name
        self.health = health
        self.power = power
        Hero.amount += 1
        print(
            f"Creating A Hero Name {self.name}\nThe total amount of heroes now {Hero.amount}")

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

# using method
h1.who()
h2.who()

h1.powerBuff(10)
print(h1.getPower())

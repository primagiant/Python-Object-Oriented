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


h1 = Hero("Saber", 100, 15)
h2 = Hero("Lancelot", 80, 18)
h3 = Hero("Angela", 120, 5)

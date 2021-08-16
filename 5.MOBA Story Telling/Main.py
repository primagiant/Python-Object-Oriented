# Moba Story Telling Versi Beta
class Hero:

    def __init__(self, name, health, power, armor) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def getStatus(self):
        print(f"{self.name} Status :")
        print(f"Health : {self.health}")
        print(f"Power  : {self.power}")
        print(f"Armor  : {self.armor}")

    def attack(self, target):
        print(f"{self.name} Attacking {target.name}")
        target.defence(self)

    def defence(self, enemy):
        self.health -= (enemy.power - self.armor)
        print(f"Now {self.name} Health = {self.health}")


saber = Hero("Saber", 100, 10, 10)
lancelot = Hero("Lancelot", 80, 15, 5)

saber.getStatus()
print('\n')
lancelot.getStatus()
print('\n')
saber.attack(lancelot)

print('\n')
lancelot.getStatus()

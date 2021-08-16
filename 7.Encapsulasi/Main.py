# Encapsulasi
class Hero:
    def __init__(self, name, health, power) -> None:
        self.__name = name
        self.__health = health
        self.__power = power

    # Getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getPower(self):
        return self.__power

    # Setter
    def setHealth(self, newHealth):
        self.__health = newHealth

    def powerBuff(self, buff):
        self.__power += buff


# initiate object
h = Hero("Lancelot", 80, 18)

class Hero:
    # private class variable
    __ammount = 0

    def __init__(self, name) -> None:
        self.__name = name
        Hero.__ammount += 1

    # hanya berlaku untuk object bukan untuk class
    def getAmmountObj(self):
        return Hero.__ammount

    # berlaku untuk class, tidak berlaku untuk object
    def getAmmountCls():
        return Hero.__ammount

    # berlaku untuk object dan class (static method)
    @staticmethod
    def getAmmount():
        return Hero.__ammount

    @classmethod
    def getAmmountTry(cls):
        return cls.__ammount


h1 = Hero("Jhonson")
print(Hero.getAmmount())
h2 = Hero("Odete")
print(h2.getAmmountTry())

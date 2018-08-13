class Toy:
    def __init__(self, newdescr: str, newlovable: float):
        self.__description = newdescr
        self.__lovable = newlovable

    def getDescription(self) -> str:
        return self.__description

    def getLovable(self) -> float:
        return self.__lovable

    def setDescription(self, newdescr: str):
        if newdescr == None or newdescr == '':
            raise ValueError

        self.__description = newdescr

    def setLovable(self, newlovable: float):
        self.__lovable = newlovable

    def __repr__(self) -> str:
        return '{0} (love factor: {1})'.format(self.__description, self.__lovable)

class ToyChest:
    def __init__(self):
        self.items = []

    def addToy(self, toy: Toy):
        self.items.append(toy)

    def __repr__(self):
        return str(self.items)


chest = ToyChest()

mytoy = Toy('G.I. Joe', 1)
chest.addToy(mytoy)
print(str(chest))

descr = mytoy.getDescription()
mytoy.setDescription('')

nothing = None

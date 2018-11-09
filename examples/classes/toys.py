class Toy:
    def __init__(self, newdescr: str, newlovable: float):
        self.description = newdescr
        self.lovable = newlovable

    def getDescription(self) -> str:
        return self.description

    def getLovable(self) -> float:
        return self.lovable

    def setDescription(self, newdescr: str):
        self.description = newdescr

    def setLovable(self, newlovable: float):
        self.lovable = newlovable


    def __repr__(self) -> str:
        return '{0} (love factor: {1})'.format(self.description, self.lovable)

class ToyChest:
    def __init__(self):
        self.items = []

    def addToy(self, toy: Toy):
        self.items.append(toy)

    def findToy(self, descr: str) -> Toy:
        for toy in self.items:
            if descr == toy.getDescription():
                return toy

        return None

    def loveMore(self, descr: str):
        toy = self.findToy(descr)
        if toy != None:
            toy.lovable += 1     

    def disposeToy(self, descr: str):
        for i in range(len(self.items)):
            if descr == self.items[i].description:
                del self.items[i]
                return

    def disposeUnlovedToys(self):
        i = 0
        while i < len(self.items):
            if self.items[i].lovable < 3:
                del self.items[i]
            else:
                i += 1

    def __repr__(self):
        return str(self.items)


chest = ToyChest()

mytoy = Toy('G.I. Joe', 1)
chest.addToy(Toy('G.I. Joe', 1))
chest.addToy(Toy('Baby', 9))
chest.addToy(Toy('Teddy Bear', 7))

chest.loveMore('Teddy Bear')


print(str(chest))

#----------------------------
# Lab Test 3 - Abraham Jaar
#----------------------------

# 80 VERSION

class Product:
    def __init__(self, partNo: int, desc: str, quant: int):
        self.partNo = partNo
        self.description = desc
        self.quantity = quant



class ProductList:
    def __init__(self):
        self.prodList = []

    def add(self, prod: Product):
        self.prodList.append(prod)
        
    def getProducts(self):
        thisString = "/"
        for i in self.prodList:
            thisString += " Product " + str(i.partNo) + ": " + i.description + " (" + str(i.quantity) + ") /"
        
        return thisString

# 90 VERSION
    
    def find(self, itemNum: int):
        setProd = None
        for i in self.prodList:
            if itemNum == i.partNo:
                setProd = i
        
        return setProd

# 100 VERSION

    def getSorted(self):
        self.prodList.sort(self.partNo ,True)
        return self.prodList.getProduct()



# UNIT TESTS

def test_Product():
    p1 = Product(123, 'Apple juice', 3)
    assert p1.partNo == 123
    assert p1.description == 'Apple juice'
    assert p1.quantity == 3

    p2  = Product(42, "Wat", 99)
    assert p2.partNo == 42
    assert p2.description == "Wat"
    assert p2.quantity == 99


def test_add_getProducts():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    products = pl.getProducts()
    assert products == '/ Product 301: Frying Pan (10) / Product 101: Baby Ruth (50) / Product 201: Pencil (25) /'

    pl2 = ProductList()
    pl2.add(Product(97, "Foo", 1000))
    pl2.add(Product(99, "Bar", 2000))
    pl2.add(Product(98, "Baz", 3000))
    pl2.add(Product(94, "Wat", 2500))
    pl2.add(Product(101, "Zoomp", 3100))
    products = pl2.getProducts()
    assert products == "/ Product 97: Foo (1000) / Product 99: Bar (2000) / Product 98: Baz (3000) / Product 94: Wat (2500) / Product 101: Zoomp (3100) /"


def test_find():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    p = pl.find(101)
    assert p != None
    assert p.partNo == 101
    assert p.description == 'Baby Ruth'

    p = pl.find(102)
    assert p == None

    pl2 = ProductList()
    pl2.add(Product(97, "Foo", 1000))
    pl2.add(Product(99, "Bar", 2000))
    pl2.add(Product(98, "Baz", 3000))
    pl2.add(Product(94, "Wat", 2500))
    pl2.add(Product(101, "Zoomp", 3100))

    p = pl2.find(99)
    assert p is not None
    assert p.partNo == 99
    assert p.description == "Bar"
    assert p.quantity == 2000

    p = pl2.find(101)
    assert p is not None
    assert p.description == "Zoomp"

    p = pl2.find(42)
    assert p is None


def test_getSorted():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    products = pl.getSorted()
    assert products == '/ Product 301: Frying Pan (10) / Product 201: Pencil (25) / Product 101: Baby Ruth (50) /'

    pl2 = ProductList()
    pl2.add(Product(97, "Foo", 1000))
    pl2.add(Product(99, "Bar", 2000))
    pl2.add(Product(98, "Baz", 3000))
    pl2.add(Product(94, "Wat", 2500))
    pl2.add(Product(101, "Zoomp", 3100))
    products = pl2.getSorted()
    assert products == "/ Product 101: Zoomp (3100) / Product 99: Bar (2000) / Product 98: Baz (3000) / Product 97: Foo (1000) / Product 94: Wat (2500) /"



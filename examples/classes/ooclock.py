class Clock:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def getSeconds(self) -> int:
        return self.minutes * 60 + self.hours * 60 * 60

    def addMinutes(self, minutes: int):
        self.hours = (self.hours + (self.minutes + minutes) // 60)
        self.minutes = (self.minutes + minutes) % 60

    def addHours(self, hours: int):
        self.addMinutes(hours * 60)

    def __str__(self) -> str:
        return "{}:{:02}".format(self.hours, self.minutes)

def test_Clock_toString():
    c = Clock(10, 5)
    assert str(c) == "10:05"

def test_Clock_addMinutes():
    c = Clock(5, 45)
    c.addMinutes(120)
    assert c.hours == 7
    assert c.minutes == 45

def test_Clock_constructor():
    c = Clock(5, 15)
    assert c.hours == 5
    assert c.minutes == 15

def test_Clock_getSeconds():
    c1 = Clock(2, 10)
    c2 = Clock(0, 30)
    assert c1.getSeconds() == 2 * 60 * 60 + 10 * 60
    assert c2.getSeconds() == 30 * 60

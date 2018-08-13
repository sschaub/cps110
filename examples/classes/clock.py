
def makeClock(hours: int, minutes: int) -> dict:
    return { "hours": hours, "minutes": minutes }

def getSeconds(c: dict) -> int:
    return c['minutes'] * 60 + c['hours'] * 60 * 60

def addMinutes(c: dict, minutes: int):
    c['hours'] = (c['hours'] + (c['minutes'] + minutes) // 60)
    c['minutes'] = (c['minutes'] + minutes) % 60

def addHours(c: dict, hours: int):
    addMinutes(c, hours * 60)

def toString(c: dict) -> str:
    return "{}:{:02}".format(c['hours'], c['minutes'])

def test_addHours():
    c = makeClock(5, 45)
    addHours(c, 2)
    assert c['hours'] == 7
    assert c['minutes'] == 45

def test_addMinutes():
    c = makeClock(5, 45)
    addMinutes(c, 120)
    assert c['hours'] == 7
    assert c['minutes'] == 45

def test_makeClock():
    c = makeClock(5, 15)
    assert c['hours'] == 5
    assert c['minutes'] == 15

def test_toString():
    c = makeClock(5, 15)
    assert toString(c) == "10:05"


# Generators, a lot of data in making functions = fulling memory and a lot of time and not unlimited doing(like while)
# So we need generators(Yiels), Yield is not ining datas so no fulling memory
def Mohammad(Age):
    Counter = 0
    while Age < 30:
        Age += 1
        Counter += 1
    print(Counter, "Years Left")
    return print


Mohammad(24)

from random import randrange, seed

seed()
for vibration in range(0, randrange(1, 101)):
    print(vibration)


def Yield():
    yield randrange(0, 100)
    yield randrange(25, 100)
    yield randrange(50, 100)
    yield randrange(75, 100)


for vibration_0 in Yield():
    print("this is", vibration_0)


def Yield0(n):
    for vibration0 in range(0, n):
        yield vibration0


print(list(Yield0(50)))


def Yield1(n0):
    Zero = 0
    while Zero < n0:
        yield Zero
        Zero += 1


print(list(Yield1(50)))

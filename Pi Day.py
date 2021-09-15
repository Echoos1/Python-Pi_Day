import math

# terms = input("How many terms to calculate? ")

finalmultiplier = 12/(640320 ** (3/2))


def doMath():
    global st
    global solution
    solution = 0
    st = 0
    for i in range(100):
        mt = (math.factorial((4 * i)) * (1103 + 26390 * i)) / (math.factorial(i) ** 4) * (396 ** (4 * i))
        st = st + mt
    solution = st * finalmultiplier

doMath()
print(solution)
print(1 / math.pi)

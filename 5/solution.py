def getPrimeFactorsDict(number):
    current = number
    checking = 2
    factors = dict()
    while checking <= current:
        while current % checking == 0:
            current = current / checking
            factors[checking] = factors.get(checking, 0)+ 1
        checking+=1
    return factors

def getSmallestDividable(number):
    soFar = dict()
    for i in range(number+1):
        primes = getPrimeFactorsDict(i)
        for a in primes:
            if primes[a] < soFar.get(a, 0):
                primes[a] = soFar[a]
        soFar.update(primes)
    total = 1
    for a in soFar:
        for x in range(soFar[a]):
            total = total * a
    return total

print(getSmallestDividable(int(input("Input number to find smallest dividable of: "))))

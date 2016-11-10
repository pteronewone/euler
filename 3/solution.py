current = 600851475143
checking = 2
while checking < current:
    while current % checking == 0 and checking < current:
        current = current / checking
    checking+=1

print(current)


def isPalindrome(number):
    myList = []
    while number > 0:
        remainder = number%10
        myList.append(remainder)
        number = (number - remainder)/10
    for i in range(len(myList)):
        if myList[i] != myList[len(myList)-i-1]:
            return False
    return True

def largestPalindromeOfThree():
    largest = 0
    for i in range(100,1000):
        for j in range(i, 1000):
            multiplied = i * j
            if multiplied > largest and isPalindrome(multiplied):
                largest = multiplied
    return largest

print(largestPalindromeOfThree())

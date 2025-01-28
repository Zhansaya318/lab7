#1
def to_ounces(grams):
    return 28.3495231 * grams

print(to_ounces(3))


#2
def to_centigrade(F):
    return (5 / 9) * (F - 32)

print(to_centigrade(3))

#3
def solve(numheads, numlegs):
    for i in range (1 , numheads + 1):
        if i*2 + (numheads - i) * 4 == numlegs:
            return i, numheads - i
    return 0, 0

print(solve(35, 94))

#4
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True

numlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

prime_numlist = list(filter(lambda x: isprime(x), numlist))

print(prime_numlist)



#5
def next_permutation(s):
    if len(s)==1:
        return [s]
    new=[]
    for i in range(len(s)):
        for x in next_permutation(s[:i]+s[i+1:]):
            new.append(s[i]+x)
    return new
print(next_permutation("hello"))

#6
string = input("write: ")
sentence = string.split()
sentence.reverse()
print(*sentence)

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if(nums[i] == 3 and nums[i] == nums[i-1]):
            print(True)
            return True
    print(False)
    return False

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3])
has_33([3, 1, 3]) 


print('\n')
#8
def spy_game(nums):
    numzero = 0
    numseven = 0
    for i in nums:
        if i == 0:
            numzero+=1
        elif numzero == 2 and i == 7:
            print(True)
            return True
    print(False)
    return False
    

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])


#9
import math
def areaOfSphere(r):
    print(4/3 *math.pi * r**3)
    return 4/3 *math.pi * r**3

areaOfSphere(4)

#10
def uniquelist(arr):
    arr.sort()
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    print(*unique_arr)
    return unique_arr

uniquelist([1, 4, 5, 2, 5, 3, 1, 5, 8, 5, 3, 4, 5, 1, 7])

#11
def is_polindrom(s):
    revs = s[::-1]
    if revs == s:
        print(True)
        return True
    print(False)
    return False

is_polindrom("Hello")
is_polindrom("kazak")


#12
def histogram(length):
    for i in length:
        print('*' * i)

histogram([4, 9, 7])

#13
import random
n = random.randint(1,21)

print("Hello! What is your name?")
name = input("")
print("Well, KBTU, I am thinking of a number between 1 and 20.\nTake a guess.")
g = int(input())
while g != n:
    if g < n:
        print("\nYour guess is too low.\nTake a guess.")
    else:
        print("\nYour guess is too low.\nTake a guess.")
    g = int(input())
print(f"Good job, KBTU! You guessed my number in {n} guesses!")
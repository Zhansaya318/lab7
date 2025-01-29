#1
def to_ounces(grams):
    return 28.3495231 * grams



#2
def to_centigrade(F):
    return (5 / 9) * (F - 32)


#3
def solve(numheads, numlegs):
    for i in range (1 , numheads + 1):
        if i*2 + (numheads - i) * 4 == numlegs:
            return i, numheads - i
    return 0, 0


#4
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True



#5
def next_permutation(s):
    if len(s)==1:
        return [s]
    new=[]
    for i in range(len(s)):
        for x in next_permutation(s[:i]+s[i+1:]):
            new.append(s[i]+x)
    return new


#6
def revstring(string):
    sentence = string.split()
    sentence.reverse()
    return sentence

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if(nums[i] == 3 and nums[i] == nums[i-1]):
            return True
    return False



#8
def spy_game(nums):
    numzero = 0
    numseven = 0
    for i in nums:
        if i == 0:
            numzero+=1
        elif numzero == 2 and i == 7:
            return True
    return False
    



#9
import math
def areaOfSphere(r):
    return 4/3 *math.pi * r**3


#10
def uniquelist(arr):
    arr.sort()
    unique_arr = []
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    return unique_arr

#11
def is_polindrom(s):
    revs = s[::-1]
    if revs == s:
        return True
    return False


#12
def histogram(length):
    for i in length:
        print('*' * i)


#13
import random
def guess_num():
    n = random.randint(1,21)

    print("Hello! What is your name?")
    name = input("")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    g = int(input())
    while g != n:
        if g < n:
            print("\nYour guess is too low.\nTake a guess.")
        else:
            print("\nYour guess is too low.\nTake a guess.")
        g = int(input())
    print(f"Good job, KBTU! You guessed my number in {n} guesses!")
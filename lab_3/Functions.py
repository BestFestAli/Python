# 1. Convert grams to ounces:
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(123))

# 2. Convert Fahrenheit to centigrade:
def fahrenheit_to_centigrade(F):
    return (5/9)*(F-32)

print(fahrenheit_to_centigrade(104))

# 3. Program to solve a classic puzzle:
def solve(numheads, numlegs):
    return "chickens: ", 2*numheads - numlegs/2, " rabbits: ", numlegs/2-numheads

print(solve(35, 94))

# 4. Filtering prime numbers:
import numpy as np
def converter(abc):
    answer = []
    num_str = ""
    j = 0
    for i in range(len(abc)):
        if abc[i] != " ":
            num_str += abc[i]
            j += 1
        else:
            answer.append(float(num_str))
            num_str = ""
    answer.append(float(num_str))
    return answer

def filter_prime(str):
    nums = converter(str)
    answer = []
    for x in nums:
        if x <= 0:
            continue
        elif type(x) == "float":
            continue
        i = 1
        primer = 0
        while i <= np.sqrt(x):
            if primer > 1:
                break
            if (int(x/i) * i) == x:
                primer += 1
            i += 1
        if primer <= 1:
            answer.append(x)
    return answer

print(filter_prime("132 7 0 -1.23 5 100 101"))

# 5. All string permutations

def permut(slovoo, idx):
    res = ''
    slovo = list(slovoo)
    if idx == len(slovo):
        for x in slovo:
            res += x
        print(res)
    else:
        for i in range(idx, len(slovo)):
            a = slovo[idx]
            slovo[idx] = slovo[i]
            slovo[i] = a
            permut(slovo, idx+1)
            a = slovo[idx]
            slovo[idx] = slovo[i]
            slovo[i] = a
        
permut('Ali', 0)
        
# 6 Return a sentence with the words reversed

def reverse(slovoo):
    slovo = list(slovoo)
    answer = []
    word_str = ""
    j = 0
    for i in range(len(slovo)):
        if slovo[i] != " ":
            word_str += slovo[i]
            j += 1
        else:
            answer.append(word_str)
            word_str = ""
    answer.append(word_str)
    res = ''
    i = len(answer)-1
    while i>0:
        res += answer[i]
        res += " "
        i -= 1
    res += answer[i]
    return res

print(reverse("Menin atym Ali jane men studentpin"))

# 7 Array contains 3 3

def has_33(nums):
    answer = False
    for i in range(len(nums)-1):
        if i!=len(nums):
            if nums[i] == 3 and nums[i+1] == 3:
                answer = True
    return answer
            

print(has_33([1, 3, 3]) )
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 

# 8 List contains 0 0 7

def spy_game(nums):
    zeros = 0
    answer = False
    for i in nums:
        if zeros >= 2 and i == 7:
            answer = True
        elif i == 0:
            zeros += 1
    return answer

print("SPY GAME")
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))

# 9 Volume of sphere

import numpy as np

def sp_vol(radius):
    return 4*radius*radius*radius*np.pi/3

print(sp_vol(4))

# 10 Unique elements of list

def unique(slovo):
    good = []
    bad = []
    for i in slovo:
        if i in good:
            bad.append(i)
            good.remove(i)
        if i not in bad:
            good.append(i)
    return good
    
print(unique([1, 1, 4, 1, 2, 5, 2, 9, 3, 2, 3, 1, 1, 3, 5]))

# 11 Checking palindroms

def palindrome(slovoo):
    slovo = list(slovoo)
    answer = True
    for i in range(len(slovo)-1):
        if slovo[i] != slovo[len(slovo)-1-i]:
            answer = False
            break 
    return answer

print(palindrome("qaza"))

# 12 histogram

def histogram(nums):
    for n in nums:
        word = ''
        i = 0
        while i < n:
            word += "*"
            i += 1
        print(word)
        
histogram([4, 9, 7])
print("==============")

# 13 Guess the number

import numpy as np
print("Before starting our game choose minimal possible number")
min_n = input()
print("Let's choose maximal possible number")
max_n = input()
my_num = np.random.randint(min_n, max_n, dtype=int) 
print("Hello! What is your name?")
x = input()

print ("Well,", x, ", I am thinking of a number between", min_n, "and", max_n)
print("Take a guess.")
a = input()
gues_num = 1
while int(a) != my_num:
    if int(a)>my_num:
        print("Your guess is too big.")
    else:
        print("Your guess is too low.")
    print("Take a guess.")
    a = input()
    gues_num += 1

print("Good job, KBTU! You guessed my number in ", gues_num, " guesses!")
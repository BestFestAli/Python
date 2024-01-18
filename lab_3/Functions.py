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
            answer.append(int(num_str))
            num_str = ""
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
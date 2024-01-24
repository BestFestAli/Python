# 1 answer 
n = input("Enter the n: ") # для первых двух задании
answer_1 = []
for i in range(1, int(n)+1):
    answer_1.append(i*i)
print(answer_1)

print("===================")
# 2 answer
for i in range(int(n)+1):
    if int(i/2)*2 == i:
        if i == int(n) or i == int(n) - 1: 
            print(i)
        else:
            print(i, end=", ")

print("===================")
# 3 answer

# не хочу это писать 1000 раз, поэтому просто супер класс сделаю
# это можно было добавить в gen_3_4 или squares, но снова предыдущая причина
class p_algo():
    def print_gen(self):
        for i in range(len(self.answer)):
            if i == len(self.answer)-1: 
                print(self.answer[i])
            else:
                print(self.answer[i], end=", ")
                
class algo_3(p_algo):
    def __init__(self, n):
        self.n = n
        self.answer = []
        
    def gen_3_4(self):
        answer = []
        for i in range(int(self.n)+1):
            if i/3 == i//3 or i/4 == i//4:
                answer.append(i)
        self.answer = answer    

prob_3 = algo_3(100)
prob_3.gen_3_4()
prob_3.print_gen()

print("===================")
# 4 answer
class algo_4(p_algo):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.answer = []
        
    def squares(self):
        answer = []
        for i in range(self.a, self.b+1):
                answer.append(i**2)
        self.answer = answer 
                
prob_4 = algo_4(20,30)
prob_4.squares()
prob_4.print_gen()

print("===================")
# 5 answer
for x in range(int(n) + 1):
    i = int(n) - x
    if i == 0: 
        print(i)
    else:
        print(i, end=", ")
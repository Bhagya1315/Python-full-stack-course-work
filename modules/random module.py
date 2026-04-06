import random

'''random.seed(7)#it will repeat the same iteration same output
# the random value defaltly gives 0 to 1 values
print(random.random)
print(random.randint(1,6))#integer values
print(random.uniform(1,6))#Float vales


l=['java','python','c++','css','html']

print(random.choice(l))
print(random.choices(l,k=2))'''

l=[9,2,3,4,5,6]
random.shuffle(l)
print(l)

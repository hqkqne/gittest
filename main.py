import random
#game culculator
def level():
    pass

def random_gen_chisel():
    a = []
    n = 2
    for i in range(n):
        a[i] = random.randint(0,10)
    return a

def random_gen_znak():
    znak = ["+", '-', '*', '/', '+/-']
    return random.choice(znak)

def rnd_gen_level():
    source = []
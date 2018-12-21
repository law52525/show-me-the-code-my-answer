import random


def random_char(number=16):
    for i in range(number):
        yield chr(random.choice(list(range(65, 90 + 1)) + list(range(97, 122 + 1)) + list(range(48, 57 + 1))))


def factory():
    a = ""
    for s in random_char():
        a += s
    return a + "\n"


n = int(input("How many Activation Code are you need?\n> "))

code = set()
while len(code) < n:
    code.add(factory())

with open('ActivationCode.txt', 'w', encoding='utf-8') as f:
    f.writelines(code)

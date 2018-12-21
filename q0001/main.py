import random


def activation_codes(n=200):
    def random_char(number=16):
        for i in range(number):
            yield chr(random.choice(list(range(65, 90 + 1)) + list(range(97, 122 + 1)) + list(range(48, 57 + 1))))

    def factory():
        a = ""
        for s in random_char():
            a += s
        return a + "\n"

    codes = set()
    while len(codes) < n:
        codes.add(factory())

    return codes


if __name__ == '__main__':
    with open('ActivationCode.txt', 'w', encoding='utf-8') as f:
        f.writelines(activation_codes())

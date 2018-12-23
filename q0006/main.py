import os
from q0004.main import main

# http://www.newxue.com/mingzhu/anniriji/
diary_path = "Het Achterhuis"


def filter_words(t):
    s = t[0].upper()
    j = list()
    with open("filter_words.txt", encoding='utf-8') as f:
        j.append(f.read().upper().split('\n'))
    j.append(chr(v) for v in range(ord('A'), ord('Z') + 1))
    for i in range(len(j)):
        j[i] = s not in j[i]
    return all(j)


if __name__ == '__main__':
    for file in os.listdir(diary_path):
        path = diary_path + os.sep + file
        print(*next(filter(filter_words, main(path))))

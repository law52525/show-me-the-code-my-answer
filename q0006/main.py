import os
from q0004.main import main

# http://www.newxue.com/mingzhu/anniriji/
diary_path = "Het Achterhuis"


def filter_words(t):
    s = t[0].upper()
    j = []
    with open("filter_words.txt", encoding='utf-8') as f:
        j.append(f.read().upper().split('\n'))
    j.append(chr(v) for v in range(ord('A'), ord('Z') + 1))
    judge = []
    for i in j:
        judge.append(s not in i)
    return all(judge)


if __name__ == '__main__':
    for file in os.listdir(diary_path):
        print(*next(filter(filter_words, main(diary_path + os.sep + file))))

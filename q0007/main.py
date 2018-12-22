import os
import sys


def is_blank_line(s):
    return not s


def is_note(s):
    return s.strip().startswith("#")


if __name__ == '__main__':
    # 从命令行参数中读入路径列表
    dirs = sys.argv[1:]
    cnt = [0, 0, 0]
    for d in dirs:
        d = ".." + os.sep + d
        for file in os.listdir(d):
            if file.endswith(".py"):
                file = d + os.sep + file
                with open(file, encoding='utf-8') as f:
                    data = f.read().split('\n')
                    v = [len(data), len(list(filter(is_note, data))), len(list(filter(is_blank_line, data)))]
                    for i in range(len(cnt)):
                        cnt[i] += v[i]
                    print("{}:\t行数({})\t注释({})\t空行({})".format(file, *v))
    print("统计:\t总行数({})\t注释({})\t空行({})".format(*cnt))

import re


def main(filename):
    with open(filename, encoding='utf-8') as f:
        s = f.read()
    results = list(filter(None, re.split(r'["-:?!.;,\s]+', s)))
    a = {r: 0 for r in results}
    for r in results:
        a[r] += 1
    return sorted(a.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    for v in main('data.txt'):
        print("{}: {}".format(*v))

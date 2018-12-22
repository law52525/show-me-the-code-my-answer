import re

if __name__ == '__main__':
    with open('data.txt', encoding='utf-8') as f:
        s = f.read()
    results = list(filter(None, re.split(r'["-:?!.;,\s]+', s)))
    a = {r: 0 for r in results}
    for r in results:
        a[r] += 1
    for v in sorted(a.items(), key=lambda x: x[1], reverse=True):
        print("{}: {}".format(v[0], v[1]))

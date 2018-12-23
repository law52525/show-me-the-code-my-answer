from functools import reduce
from werkzeug.security import generate_password_hash, check_password_hash
from itertools import permutations

password = "123456"
hashed = generate_password_hash(password)
print(reduce(lambda x, y: x * y, range(1, len(password) + 1)))
a = {True: 0, False: 0}
for i in permutations(password):
    a[check_password_hash(hashed, ''.join(i))] += 1
print(a)

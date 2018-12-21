import pymysql
import os
import random
from DBUtils.PooledDB import PooledDB

database_pool = PooledDB(pymysql, maxcached=2, maxconnections=20, blocking=True,
                         host=os.environ.get('MYSQL_HOST', default='localhost'),
                         port=int(os.environ.get('MYSQL_PORT', default='3306')),
                         user=os.environ.get('MYSQL_USER', default='root'),
                         passwd=os.environ['MYSQL_PASSWORD'],
                         db=os.environ.get('MYSQL_DB', default='smyc'), charset='utf8')

connection = database_pool.connection()


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


try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO ActivationCode (activation_code) VALUES (%s)"
        cursor.executemany(sql, activation_codes())
    connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT * from ActivationCode"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

import pymysql
import os
from DBUtils.PooledDB import PooledDB
from q0001.main import activation_codes

database_pool = PooledDB(pymysql, maxcached=2, maxconnections=20, blocking=True,
                         host=os.environ.get('MYSQL_HOST', default='localhost'),
                         port=int(os.environ.get('MYSQL_PORT', default='3306')),
                         user=os.environ.get('MYSQL_USER', default='root'),
                         passwd=os.environ['MYSQL_PASSWORD'],
                         db=os.environ.get('MYSQL_DB', default='smyc'), charset='utf8')

connection = database_pool.connection()

if __name__ == '__main__':
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

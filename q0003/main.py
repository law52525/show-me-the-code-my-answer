import os
import redis
from q0001.main import activation_codes

redis_conn = redis.StrictRedis(host=os.environ.get('REDIS_HOST', default='localhost'),
                               port=int(os.environ.get('REDIS_PORT', default='6379')),
                               decode_responses=True)

if __name__ == '__main__':
    redis_conn.sadd("ActivationCode", *activation_codes())
    print(redis_conn.smembers("ActivationCode"))

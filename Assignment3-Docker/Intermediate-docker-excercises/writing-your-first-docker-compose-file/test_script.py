
from redis import Redis
redis = Redis(host='redis', port=6379,password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')

redis.incr('hits')
print('This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits'))
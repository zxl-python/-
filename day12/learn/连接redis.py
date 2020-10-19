import redis
import json
red = redis.Redis(host='127.0.0.1',port=6379)    # 连接redis数据库
res = red.lrange('hehe:items',0,-1)
for n in res:
    print(json.loads(n.decode('utf-8')))
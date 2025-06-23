import time
from flask import Flask

from rediscluster import RedisCluster

startup_nodes = [
    {'host': "redis-cluster-0.redis-cluster-service.default.svc.cluster.local", 'port': 6379},
    {'host': "redis-cluster-1.redis-cluster-service.default.svc.cluster.local", 'port': 6379},
    {'host': "redis-cluster-2.redis-cluster-service.default.svc.cluster.local", 'port': 6379},
]

redis_cluster = RedisCluster(startup_nodes=startup_nodes)

app = Flask(__name__)


def get_hit_count():
    return redis_cluster.incr('hits')


@app.route('/')
def hit():
    count = get_hit_count()
    return 'I have been hit %i times since deployment.\n' % int(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


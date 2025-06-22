import rediscluster
from rediscluster import RedisCluster
import time
from flask import Flask

startup_nodes = [
    {'host': "10.1.1.11", 'port': 6379},
    {'host': "10.1.1.12", 'port': 6379},
    {'host': "10.1.1.13", 'port': 6379},
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


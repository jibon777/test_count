import time

import redis
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route("/", methods=["GET"])
def get_my_ip():
    count = get_hit_count() 
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr) + ' I have been seen {} times.\n'.format(count)




if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=80, debug=False)

from flask import Flask
#from redis import Redis
from flask import request
from flask import jsonify


app = Flask(__name__)
#redis = Redis(host= "redis", port=6379)


#    return 'ip_address Hello ! You have seen this page {0} times' . format (redis.get( 'hits' ))


@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=80, debug=False)

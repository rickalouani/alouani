#!/usr/bin/python
#  Added this 
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
#        redis.print("counter")
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Cannot Connect to Redis, counter disable</i>"

    html = "<h3>Hello (name}!</h3>" \
            "<b>Hostname:</b>" \
            "<b>Visit:</b> {visits}"

    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname(), visits=visits)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)

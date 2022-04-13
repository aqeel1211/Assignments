# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello world!'

# if __name__ == "__main__":
#     app.run(host="0.0.0.0",debug=True)


from redis import Redis
from flask  import Flask
app = Flask(__name__)
redis = Redis(host='redis', port=6379,password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

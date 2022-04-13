from flask import Flask
from redis import Redis
app = Flask(__name__)
redis_cli = Redis(host='redis', port=6379)
@app.route("/")
def index():
    redis_cli.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis_cli.get('hits')


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8090)
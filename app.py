from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    # Increment a counter in Redis on each visit
    redis.incr('visit_count')

    # Retrieve the visit count from Redis
    visit_count = redis.get('visit_count').decode('utf-8')

    return f'Hello, Welcome to My Docker experiment! \n- Visit Count: {visit_count}\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)

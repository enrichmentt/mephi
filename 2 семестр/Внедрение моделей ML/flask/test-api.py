import datetime

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Test message. The server is running"

@app.route('/hello')
def say_hallo():
    name = request.args.get('name')
    return f'Hello, {name}'

@app.route('/time')
def current_time():
    now = datetime.datetime.now()
    return {'time' : now}

@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')

    if num > 10:
        return "too much", 400
    else:
        return jsonify({
            'result': num + 1
        })

if __name__ == '__main__':
    app.run('localhost', 5000)

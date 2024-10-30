from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == 'main':
    app.run(host='0.0.0.0', port=5252)

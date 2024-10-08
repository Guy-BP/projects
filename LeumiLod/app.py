from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, HTTPS Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('/etc/ssl/certs/flask.crt', '/etc/ssl/private/flask.key'))

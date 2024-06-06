from flask import Flask, send_from_directory
from os import environ

app = Flask(__name__)


@app.route('/favicon.ico')
def fav():
    return send_from_directory(
        app.root_path,
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


@app.route('/')
def hello():
    return 'DONE'


if __name__ == "__main__":
    app.run(
        debug=True,
        port=int(environ.get('APP_PORT', 1234)),
        host='0.0.0.0'
    )

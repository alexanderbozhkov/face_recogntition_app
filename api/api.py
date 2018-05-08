import os
from sys import argv
from flask import Flask
from flask_uploads import configure_uploads
from apis import api
from apis.upload_images import image
from flask_cors import CORS

app = Flask(__name__)
api.init_app(app)
UPLOAD_FOLDER = os.getcwd() + '/database/'
app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_FOLDER
configure_uploads(app, image)
CORS(app, resources=r'*')


def int_port_conv(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    DEFAULT_PORT = 5000
    if len(argv) > 1 and int_port_conv(argv[1]) and 0 < int(argv[1]) < 9999:
        app.run(debug=True, port=int(argv[1]))
    else:
        app.run(debug=True, port=DEFAULT_PORT)

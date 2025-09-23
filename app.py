import sys
sys.path.append('/home/ec2-user/.local/lib/python3.9/site-packages')
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
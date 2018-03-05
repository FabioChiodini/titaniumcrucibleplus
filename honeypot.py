from flask import Flask, jsonify, request
import os
import logging
import logstash
import sys
import requests

if 'LOG_HOST' not in os.environ:
    raise(Exception("LOG_HOST NOT DEFINED"))

host = os.environ['LOG_HOST']
API_ENDPOINT = os.environ['LOG_HOST']

data1 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

datak = {'honeypotsourceip':data1}

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))

app = Flask(__name__)

def log_request(req):
    extra = {
        'ip': request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        'url': req.full_path,
    }
    test_logger.info('honeypot: ', extra=extra)

#    data_to_log.update(req.headers)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def honey(path):
    #log_request(request)
    requests.post(url = API_ENDPOINT, data = datak)
    return jsonify({'result': 'ok'})
    # Test to return the client ip
    # return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

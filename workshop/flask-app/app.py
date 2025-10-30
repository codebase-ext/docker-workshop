from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello World from Flask!',
        'container_id': socket.gethostname(),
        'environment': os.getenv('ENV', 'production')
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/data')
def get_data():
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Docker'},
            {'id': 2, 'name': 'Containers'},
            {'id': 3, 'name': 'Flask'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
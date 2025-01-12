from flask import Flask, request, jsonify, send_from_directory
import subprocess

app = Flask(__name__)

# Serve the HTML file for the root URL
@app.route('/')
def home():
    return send_from_directory('', 'index.html')  # Make sure 'index.html' is in the same directory as app.py

# API to run Python code
@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    try:
        result = subprocess.check_output(
            ['python', '-c', code],  # Use 'python' instead of 'python3'
            stderr=subprocess.STDOUT,
            text=True
        )
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output}), 400


if __name__ == '__main__':
    app.run(debug=True)

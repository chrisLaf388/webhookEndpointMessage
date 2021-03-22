from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/webhook', methods=['POST'])
def respond():
        message = request.json
        messages.append(message)
        print(message)
        return jsonify(messages)

@app.route('/api', methods=['GET'])
def home():
    return jsonify(messages);
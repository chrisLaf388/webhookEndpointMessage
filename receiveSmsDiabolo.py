from flask import Flask, request, redirect, url_for,Response, render_template, jsonify

app = Flask(__name__)

messages = []

@app.route('/api', methods=['GET','POST'])
def respond():
    member = request.json
    messages.append(member)
    print(member)
    return jsonify(messages)

@app.route('/')
def home():
    return'welcome';
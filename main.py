from flask import Flask
from flask_cors import CORS

users = {}
chat = []
max = 0

app = Flask(__name__)
CORS(app)

@app.route("/adduser/<name>/<password>")
def add(name, password):
    users[name] = password

@app.route("/login/<name>/<password>")
def login(name, password):
    if users[name] == password:
        return 1
    else:
        return 0

@app.route("/remuser/<name>/<password>")
def rm(name, password):
    if users[name] == password:
        del users[name]
    return 1

@app.route("/send/<user>/<mes>")
def send(user, mes):
    global max
    max += 1
    chat.append([max, user, mes])
    return 1

@app.route("/getchat")
def get():
    return chat

app.run(debug=False, port=10000)

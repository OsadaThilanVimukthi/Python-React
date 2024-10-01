from flask import Flask,render_template,request
from flask_socketio import SocketIO,emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

#Python dict(user_dictatory). store connected users. key is socketid value is username and avatar url
users ={}

@app.route('/')
def index():
    return render_template('index.html')

#User Connect
#We are listening the connect event
@socketio.on("connect")
def handle_connect():
    username = f"User_{random.randint(1000,9999)}"
    gender = random.choice(["girl","boy"])
    avatar_url = f"https://avatar.iran.liara.run/public/{gender}?username={username}"

    users[request.sid] = { "username": username, "avatar_url": avatar_url}

    #Notify User Is Join
    emit("user_joined",{username:"username","avatar_url": avatar_url},broadcast=True)

    #Random Name For User
    emit("set_username",{"username":username})

#Disconnect User
@socketio.on("disconnect")
def handle_disconnect():
    #Delete From Dictionary
    user = users.pop(request.sid, None)
    if user:
        emit("user_left",{"username":user["username"]},broadcast=True)


#Send Massages
@socketio.on("send_massages")
def handle_massages(data):
    user = users.get(request.sid)
    if user:
        emit("new_massage",{
            "username":user["username"],
            "avatar_url":user["avatar_url"],
            "message":data["message"]

        },broadcast=True)

@socketio.on("update_username"):
def update_username(data):
    old_username = users[request.sid["username"]]
    new_username = data["username"]
    users[request.id]["username"] = new_username

    emit("username_updated",{
        "old_username": old_username,
        "new_username": new_username,
    },broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
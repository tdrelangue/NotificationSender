# notification_server.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

@app.route("/")
def home():
    return "✅ Notification server is running"

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    title = data.get("title", "📢 Notification")
    message = data.get("message", "")
    token = data.get("expo_push_token", None)

    # 1. Emit to all connected Socket.IO clients
    socketio.emit("notification", {"title": title, "message": message})

    # 2. Optionally send to Expo Push if token provided
    if token:
        payload = {
            "to": token,
            "title": title,
            "body": message,
        }
        headers = {"Content-Type": "application/json"}
        res = requests.post(EXPO_PUSH_URL, json=payload, headers=headers)
        print("Expo push status:", res.status_code, res.text)

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

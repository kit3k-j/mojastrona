from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

def save_ip(ip):
    with open("ip_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {ip}\n")

@app.route("/")
def home():
    ip = request.remote_addr
    save_ip(ip)

    return f"""
    <h1>Właśnie zmarnowales jakies 5 sekund życia 😄</h1>
    <p>Twoje IP(jakbyś zaponiał): {ip}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
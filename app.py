from flask import Flask, request
from datetime import datetime
import requests
import os

app = Flask(__name__)

LOG_FILE = "ip_log.txt"

def get_location(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"{res.get('country')} - {res.get('city')}"
    except:
        return "unknown"

def save_ip(ip):
    location = get_location(ip)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {ip} - {location}\n")

def read_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return f.readlines()
    except:
        return []

@app.route("/")
def home():
    ip = request.remote_addr
    save_ip(ip)

    return f"""
    <h1>Strona działa 😄</h1>
    <p>Twoje IP: {ip}</p>
    <a href="/panel">Panel</a>
    """

@app.route("/panel")
def panel():
    logs = read_logs()
    logs_html = "<br>".join(logs)

    return f"""
    <h1>Panel IP 🌍</h1>
    <pre>{logs_html}</pre>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

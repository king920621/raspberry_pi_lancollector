import os
from flask import Flask, Response

app = Flask(__name__)
LOG_FILE = "/data/ping.log"

@app.route("/")
def home():
    return "Ping Monitor API is running. Use /api/csv to get data."

@app.route("/api/csv")
def get_csv():
    if not os.path.exists(LOG_FILE):
        return Response("timestamp,latency\n", mimetype="text/csv")

    def generate():
        yield "timestamp,latency\n"
        with open(LOG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield line + "\n"
    return Response(generate(), mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import argparse
import time
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/logger", methods=["POST"])
def log():
    if not request.method == "POST":
        return

    app_name, msg = request.form.get("appName", default="", type=str), request.form.get("msg", default="", type=str)

    if app_name != "":
        print(time.strftime("%Y-%m-%d %H:%M"), "-", app_name, msg)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    return json.dumps({'success': False}), 201, {'ContentType': 'application/json'}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple RESTAPI logger to log workload juggling")
    parser.add_argument("--port", default=3000, type=int, help="port number")
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port)
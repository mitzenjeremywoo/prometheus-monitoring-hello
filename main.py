# app.py
from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter("myapp_custom_requests_total", "Total requests received")

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.route("/")
def index():
    REQUESTS.inc()
    return "Hello, Prometheus!"

# GET endpoint
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST endpoint
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        "id": len(items) + 1,
        "name": data["name"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

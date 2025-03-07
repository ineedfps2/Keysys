from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import os

app = Flask(__name__)
CORS(app)

# Simulated database
keys_db = {}

@app.route('/generate_key', methods=['POST'])
def generate_key():
    new_key = str(uuid.uuid4())
    keys_db[new_key] = {"used": False}
    return jsonify({"key": new_key})

@app.route('/validate_key', methods=['POST'])
def validate_key():
    data = request.json
    key = data.get("key")

    if key in keys_db and not keys_db[key]["used"]:
        keys_db[key]["used"] = True
        return jsonify({"status": "success", "message": "Key validated!"})
    
    return jsonify({"status": "error", "message": "Invalid or used key."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

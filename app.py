from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pre-call', methods=['POST'])
def pre_call_callback():
    print("=== Pre-Call Triggered ===")
    data = request.json
    client_number = data.get('user_number')  # expects a number like '966502104776'

    # Dummy client database (phone -> name)
    client_db = {
        '966580323262': "Mohammed",
        '966502104776': "Eyad"
    }

    client_name = client_db.get(client_number)

    if client_name:
        print(f"✅ Found client: {client_name}")
        return jsonify({
            "client_name": client_name
        })
    else:
        print("❌ Unknown phone number")
        return jsonify({"error": "Client not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=10000)

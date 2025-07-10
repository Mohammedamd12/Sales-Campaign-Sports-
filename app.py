from flask import Flask, request, jsonify
from twilio.rest import Client
import os
import json
import requests

app = Flask(__name__)

# Load credentials from environment variables (for Render)
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM_WHATSAPP_NUMBER = os.environ.get('FROM_WHATSAPP', 'whatsapp:+14155238886')

# Load credentials from environment variables (for Hugging Face)
HF_API_KEY = os.environ.get('HF_API_KEY')
HF_MODEL_URL = os.environ.get('HF_MODEL_URL', 'https://api-inference.huggingface.co/models/joeddav/xlm-roberta-large-xnli')
HF_headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}


client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.route('/pre-call', methods=['POST'])
def pre_call_callback():
    print("=== Pre-Call Triggered ===")
    data = request.json
    client_id = data.get('client_id')  # or use 'phone' if you're using the phone directly

    # Dummy client database
    client_db = {
        'c001': {"phone": "966580323262", "client_name": "Mohammed"},
        'c002': {"phone": "966502104776", "client_name": "Eyad"}
    }

    client_info = client_db.get(client_id)

    if client_info:
        print(f"✅ Found client {client_id}")
        return jsonify({
            "phone": client_info["phone"],
            "client_name": client_info["client_name"]
        })
    else:
        print("❌ Unknown client_id")
        return jsonify({"error": "Client not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=10000)

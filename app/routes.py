from flask import Blueprint, request, jsonify

webhook = Blueprint('webhook', __name__)

@webhook.route('/webhook', methods=['POST'])
def handle_webhook():
    # Extract data from the incoming request
    data = request.json

    # Perform some action with the data (e.g., log it or process it)
    print("Received data:", data)

    # Return a response
    return jsonify({"message": "Webhook received!", "status": "success"}), 200

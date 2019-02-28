from os import environ
from flask import Flask, request, jsonify
import requests

BOT_TOKEN = environ.get('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = environ.get('TELEGRAM_WEBHOOK_URL')
def set_webhook():
    set_webhook_url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebHook?url={WEBHOOK_URL}'
    webhook_response = requests.get(set_webhook_url)
    return webhook_response

set_webhook_response = set_webhook()
print(set_webhook_response.text)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def telegram():
    data_body = request.get_json()
    print(data_body)
    message = data_body.get('message')
    print(message)
    username = message.get('from').get('username')
    print(username)
    chat_id = message.get('chat').get('id')
    answer = f"{username}: {message['text']}"

    resp = requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?POST',
                         json={'chat_id': chat_id, 'text': answer})
    return jsonify(resp.json()), resp.status_code

# app.run()


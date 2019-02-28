from os import environ
from flask import Flask, request, jsonify
import requests


# https://core.telegram.org/bots/api#setwebhook

def set_webhook():
    bot_token = environ.get('TELEGRAM_BOT_TOKEN')
    webhook_url = environ.get('TELEGRAM_WEBHOOK_URL')
    set_webhook_url = f'https://api.telegram.org/bot{bot_token}/setWebHook?url={webhook_url}'
    webhook_response = requests.get(set_webhook_url)
    return webhook_response


set_webhook_response = set_webhook()
#if set_webhook_response.status_code != 200:
 #   raise ValueError('Set webhook fail')

print(set_webhook_response.text)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def telegram():
    data_body = request.get_json()
    print(data_body)
    return jsonify(data_body)

#app.run()

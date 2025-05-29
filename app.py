from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7969471192:AAGVzlilJRwz6q3AX6OV2nCzmb6-4hgQwBA'
TELEGRAM_CHAT_ID = '1990590089'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.data.decode('utf-8')

    if "BUY_SIGNAL" in data:
        message = "🚀 اشارة دخول شراء على الذهب!"
    elif "SELL_SIGNAL" in data:
        message = "🔻 اشارة دخول بيع على الذهب!"
    else:
        message = "❓ تم استلام تنبيه غير معروف."

    send_telegram_message(message)
    return 'ok'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

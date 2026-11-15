from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get("hub.verify_token") == "rahasia123":
        return request.args.get("hub.challenge")
    return "Gagal", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json)
    return "OK", 200

@app.route('/')
def home():
    return "Bot Booking Mobil Jalan!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

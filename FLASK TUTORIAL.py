from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Hello from my mobile server!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Хост 0.0.0.0 нужен, чтобы сервер был доступен в локальной сети
    app.run(host='0.0.0.0', port=5000, debug=True)

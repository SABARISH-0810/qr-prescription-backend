from flask import Flask, request, send_file, jsonify
from flask_cors import CORS  # Import CORS
import qrcode
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

QR_FOLDER = "qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "QR Prescription API is running!"

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get("prescription", "")
    filename = request.json.get("filename", "default_qr")

    if not data:
        return jsonify({"error": "Prescription data is required"}), 400

    qr_path = os.path.join(QR_FOLDER, f"{filename}.png")

    qr = qrcode.make(data)
    qr.save(qr_path)

    return send_file(qr_path, mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True, port=5001)

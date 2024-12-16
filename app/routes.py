from flask import Blueprint, jsonify
import shutil


# Create a Blueprint for routes
bp = Blueprint('routes', __name__)


def read_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone1/temp", "r") as temp_file:
            temp = int(temp_file.read().strip()) / 1000.0
        return temp
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)


# CPU temperature endpoint
@bp.route('/cpu/temp', methods=['GET'])
def cpu_temp():
    temp = read_cpu_temperature()
    if temp is None:
        return jsonify({"error": "Temperature sensor not found"}), 500
    elif isinstance(temp, str):
        return jsonify({"error": temp}), 500
    else:
        return jsonify({"Temperature (C)": temp})


# CPU temperature error-checking endpoint
@bp.route('/cpu/temp/error', methods=['GET'])
def cpu_temp_error():
    try:
        temperature = read_cpu_temperature()
        status = "too hot" if temperature > 60 else "fine"
        return jsonify({"Status": status, "Temperature (C)": temperature})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Disk usage endpoint
@bp.route('/disk/usage', methods=['GET'])
def disk_usage():
    try:
        total, used, free = shutil.disk_usage("/")
        usage_percent = (used / total) * 100
        return jsonify({"Disk Usage (%)": usage_percent})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

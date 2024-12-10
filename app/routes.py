from flask import Blueprint, jsonify
from gpiozero import CPUTemperature
import shutil


# Create a Blueprint for routes
bp = Blueprint('routes', __name__)


def read_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            temp = int(temp_file.read()) / 1000.0
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
        return jsonify({"temp": temp})


# CPU temperature error-checking endpoint
@bp.route('/cpu/temp/error', methods=['GET'])
def cpu_temp_error():
    try:
        cpu = CPUTemperature()
        temperature = cpu.temperature
        status = "too hot" if temperature > 60 else "fine"
        return jsonify({"status": status, "temp": temperature})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Disk usage endpoint
@bp.route('/disk/usage', methods=['GET'])
def disk_usage():
    try:
        total, used, free = shutil.disk_usage("/")
        usage_percent = (used / total) * 100
        return jsonify({"disk_usage_percent": usage_percent})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

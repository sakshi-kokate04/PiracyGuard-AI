import platform
import uuid
import hashlib
import socket
import os
import json
from datetime import datetime


def get_hardware_id():
    """
    Hardware-based values (stable)
    """
    system_info = {
        "machine": platform.machine(),
        "processor": platform.processor(),
        "node": platform.node(),
        "mac": hex(uuid.getnode()),
    }
    raw = json.dumps(system_info, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def get_software_id():
    """
    Software / OS-based values
    """
    software_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
        "hostname": socket.gethostname(),
    }
    raw = json.dumps(software_info, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def get_plugin_id():
    """
    Project / app specific ID (simulates plugin identity)
    """
    plugin_info = {
        "project": "PiracyGuardAI",
        "install_path": os.getcwd(),
        "created": datetime.now().strftime("%Y-%m"),
    }
    raw = json.dumps(plugin_info, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def generate_device_fingerprint():
    hardware_id = get_hardware_id()
    software_id = get_software_id()
    plugin_id = get_plugin_id()

    combined = hardware_id + software_id + plugin_id
    device_fingerprint = hashlib.sha512(combined.encode()).hexdigest()

    return {
        "hardware_id": hardware_id,
        "software_id": software_id,
        "plugin_id": plugin_id,
        "device_fingerprint": device_fingerprint
    }


if __name__ == "__main__":
    fingerprint = generate_device_fingerprint()
    print("\n🔐 DEVICE SCAN RESULT 🔐\n")
    for key, value in fingerprint.items():
        print(f"{key.upper()}:\n{value}\n")

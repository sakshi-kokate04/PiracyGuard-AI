# PiracyGuard AI - Device Identification Module

import platform
import uuid
import hashlib

# -------------------------------
# HARDWARE ID (HWID)
# -------------------------------
def generate_hardware_id():
    """
    Unique ID for physical machine
    """
    system = platform.system()
    machine = platform.machine()
    processor = platform.processor()
    mac_address = uuid.getnode()

    raw_data = f"{system}-{machine}-{processor}-{mac_address}"
    hardware_id = hashlib.sha256(raw_data.encode()).hexdigest()

    return hardware_id


# -------------------------------
# SOFTWARE KEY
# -------------------------------
def generate_software_key():
    """
    Unique software installation key
    """
    os_name = platform.system()
    node_name = platform.node()
    processor = platform.processor()
    mac_address = uuid.getnode()

    raw_data = f"{os_name}-{node_name}-{processor}-{mac_address}"
    hashed = hashlib.sha256(raw_data.encode()).hexdigest()

    software_key = f"SOFT-{hashed[:4]}-{hashed[4:8]}-{hashed[8:12]}"
    return software_key


# -------------------------------
# PLUGIN ID
# -------------------------------
def generate_plugin_id(software_key, hardware_id):
    """
    Plugin bound to software + hardware
    """
    raw_data = f"{software_key}-{hardware_id}"
    plugin_hash = hashlib.sha256(raw_data.encode()).hexdigest()

    plugin_id = f"PLUGIN-{plugin_hash[:6]}-{plugin_hash[6:12]}"
    return plugin_id


# -------------------------------
# TEST RUN
# -------------------------------
if __name__ == "__main__":
    software_key = generate_software_key()
    hardware_id = generate_hardware_id()
    plugin_id = generate_plugin_id(software_key, hardware_id)

    print("\n🔐 PIRACYGUARD AI – DEVICE KEYS\n")
    print("Software Key :", software_key)
    print("Hardware ID  :", hardware_id[:24], "...")
    print("Plugin ID    :", plugin_id)

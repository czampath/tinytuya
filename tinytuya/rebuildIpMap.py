import argparse
import shutil
import subprocess
import os
import json

def readFile():
        
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the path to the 'device_map.json' file in the same directory
    json_path = os.path.join(script_dir, 'device_map.json')

    with open(json_path, 'r') as file:
        data = json.load(file)
        for device in data:
            mac_addr = device['mac'].replace(":", "-")
            dev_name = device['name']
            try:
                command = f'arp -a | findstr {mac_addr}'
                res = subprocess.check_output(command, shell=True, text=True)
                ip_address = res.split()[0]
                device["ip"] = ip_address
                print(f"Mac Address: {mac_addr} -> IP Address found: {ip_address} -> {dev_name}")
            except:
                print(f"No IP address found for MAC: {mac_addr} -> {dev_name}")

        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Device map saved successfully!")

def installDeviceMap():
    print('Installing IPs...')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'device_map.json')

    if not os.path.exists(json_path):
        print("device_map.json not found!")
        return

    # Local PC Path
    local_path = os.path.expandvars(r"%CODE_SPACE%\\Py\\tinytuya\\dist\\run\\")
    os.makedirs(local_path, exist_ok=True)
    
    try:
        shutil.copy(json_path, local_path)
        print(f"Copied to Local PC Path: {local_path}")
    except Exception as e:
        print(f"Failed to copy to Local PC Path: {e}")

    # Network PC Path
    network_path = r"\\HOUSTON\\home-res\\tuya-local\\"
    os.makedirs(network_path, exist_ok=True)

    try:
        shutil.copy(json_path, network_path)
        print(f"Copied to Network PC Path: {network_path}")
    except Exception as e:
        print(f"Failed to copy to Network PC Path: {e}")

def autorun():
    readFile()
    installDeviceMap()

def main():
    parser = argparse.ArgumentParser(description="Rebuild IP Map Script")
    parser.add_argument("--install", action="store_true", help="Copy device_map.json to specified locations")
    args = parser.parse_args()

    readFile()

    if args.install:
        installDeviceMap()

if __name__ == "__main__":
    main()
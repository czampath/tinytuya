import subprocess
import os
import json

def readFile():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(script_dir, 'device_map.json')

    with open(json_path, 'r') as file:
        data = json.load(file)
        for device in data:
            mac_addr = device['mac'].replace(":", "-")
            try:
                command = f'arp -a | findstr {mac_addr}'
                res = subprocess.check_output(command, shell=True, text=True)
                ip_address = res.split()[0]
                device["ip"] = ip_address
                print(f"Mac Address: {mac_addr} -> IP Address found: {ip_address}")
            except:
                print(f"No IP address found for MAC: {mac_addr}")

        with open(json_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Device map saved successfully!")

def main():
    readFile()

if __name__ == "__main__":
    main()
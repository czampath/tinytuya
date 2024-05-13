import sys
import json
from tinytuya import OutletDevice

def findDeviceByName(name):
    with open('device_map.json', 'r') as file:
        data = json.load(file)
        for device in data:
            if device['name'] == name:
                return OutletDevice(
                    dev_id=device['dev_id'],
                    address=device['ip'],
                    local_key=device['local_key'],
                    version=device['version']
                )
        return None

def main():
    args = sys.argv[1:]  # Exclude the script name
    if not args:
        print("Please provide arguments. Usage: python run.py <name> [<status1> <status2> <status3> <status4>]")
        return

    name = args[0]
    device = findDeviceByName(name)
    if device:
        if len(args) == 1:
            data = device.status()
            print(data)
        else:
            statuses = [arg.lower() == 'true' for arg in args[1:]]
            if len(statuses) == 1:
                device.set_status(statuses[0])
            else:
                for i, status in enumerate(statuses, start=1):
                    if i > 4:
                        break
                    device.set_status(status, i)
    else:
        print("Device not found.")

if __name__ == "__main__":
    main()

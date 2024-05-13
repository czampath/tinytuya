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

d = findDeviceByName("Bedroom lights")
if d:
    d.set_status(False, 1)
else:
    print("Device not found.")
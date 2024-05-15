import sys
import json
import argparse
from tinytuya import OutletDevice

def findDevice(identifier, search_by='name'):
    with open('device_map.json', 'r') as file:
        data = json.load(file)
        for device in data:
            if search_by == 'name' and device['name'] == identifier:
                return OutletDevice(
                    dev_id=device['dev_id'],
                    address=device['ip'],
                    local_key=device['local_key'],
                    version=device['version']
                )
            elif search_by == 'id' and device['dev_id'] == identifier:
                return OutletDevice(
                    dev_id=device['dev_id'],
                    address=device['ip'],
                    local_key=device['local_key'],
                    version=device['version']
                )
        return None

def main():
    parser = argparse.ArgumentParser(description="Control smart devices by name or ID.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--name', type=str, help="The name of the device.")
    group.add_argument('--id', type=str, help="The device ID.")
    parser.add_argument('statuses', nargs='*', help="Status values (True/False) to set.")

    args = parser.parse_args()

    if args.name:
        device = findDevice(args.name, search_by='name')
    elif args.id:
        device = findDevice(args.id, search_by='id')

    if device:
        if not args.statuses:
            # Get Status
            data = device.status()
            print('get_status() result:', data)
        else:
            statuses = [arg.lower() == 'true' for arg in args.statuses]
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

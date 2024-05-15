import sys
import json
import argparse
import os
import concurrent.futures
from tinytuya import OutletDevice

TIMEOUT = 4  # Timeout in seconds

def findDevice(identifier, search_by='name'):
    # Determine the path to the JSON file relative to the executable
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the path will be relative to the executable
        script_dir = os.path.dirname(sys.executable)
    else:
        # If run in a normal Python environment, the path will be relative to the script
        script_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(script_dir, 'device_map.json')
    
    with open(json_path, 'r') as file:
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

def execute_with_timeout(function, *args, **kwargs):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(function, *args, **kwargs)
        try:
            result = future.result(timeout=TIMEOUT)
            return result
        except concurrent.futures.TimeoutError:
            print(f"Error: Operation timed out after {TIMEOUT} seconds")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Control smart devices by name or ID.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--name', type=str, help="The name of the device.")
    group.add_argument('--id', type=str, help="The device ID.")
    parser.add_argument('statuses', nargs='*', help="Status values (True/False/null) to set.")

    args = parser.parse_args()

    if args.name:
        device = findDevice(args.name, search_by='name')
    elif args.id:
        device = findDevice(args.id, search_by='id')

    if device:
        if not args.statuses:
            # Get Status
            data = execute_with_timeout(device.status)
            print(data)
        else:
            for i, arg in enumerate(args.statuses, start=1):
                if arg.lower() == 'null':
                    continue  # Skip null values
                status = arg.lower() == 'true'
                execute_with_timeout(device.set_status, status, i)
    else:
        print("Device not found.")

if __name__ == "__main__":
    main()
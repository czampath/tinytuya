## Compile the code

```bash
pyinstaller --add-data "device_map.json:." run.py --noconsole
```


## In case IPs changed

### Run IP Installer

tuya_wizard_ip_installer (IP Installer) was build combining  `tinytuya wizard` with `rebuild-ip-map.py`.
Tinytuya Wizard scans local devices, and then the custom code will re-assign IPs for devices in device_map.json.

In case IP Builder is unable to pick up IPs:

- Reset the breakers
- Turn firewall OFF temporarily -> run `python -m tinytuya wizard` -> run polling to grab the IPs
- Ping the IPs to `wake up` the device to ensure its in the APR Cache
- run `tuya_wizard_ip_installer.exe`


## Build IP Installer

1. Build the installer app:

    ```bash
    pyinstaller  tinytuya\tuya_wizard_ip_installer.py
    ```

2. Copy `device_map.json` to `\tinytuya\dist\tuya_wizard_ip_installer\_internal\tinytuya\device_map.json`

3. Copy `tinytuya.json` to `\tinytuya\dist\tuya_wizard_ip_installer`

4. Run `tuya_wizard_ip_installer.exe`
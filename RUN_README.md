## Compile the code

```
pyinstaller --add-data "device_map.json:." run.py --noconsole
```


## In case IPs changed

run `rebuild-ip-map.py` to rescan and auto map ip addresses to corresponding mac addresss

In case rebuilder is unable to pick up IPs:

- Reset the breakers
- Turn firewall OFF temporarily -> run `python -m tinytuya wizard` -> run polling to grab the IPs
- Ping the IPs to `wake up` the device to ensure its in the APR Cache
- run `rebuild-ip-map.py`
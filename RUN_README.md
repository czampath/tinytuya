## Compile the code

```
pyinstaller --add-data "device_map.json:." run.py --noconsole
```


## In case IPs changed

run `rebuild-ip-map.py` to rescan and auto map ip addresses to corresponding mac addresss
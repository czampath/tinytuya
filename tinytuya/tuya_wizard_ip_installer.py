# run.py
from tinytuya import wizard, rebuildIpMap, scanner, version, SCANTIME, DEVICEFILE, SNAPSHOTFILE, CONFIGFILE, RAWFILE, set_debug


creds = { 'file': None, 'apiKey': None, 'apiSecret': None, 'apiRegion': None, 'apiDeviceID': None }

wizard.wizard( color=False, retries=None, forcescan=None, nocloud=False, assume_yes=False, discover=False, skip_poll=False, credentials=creds )

rebuildIpMap.autorun()
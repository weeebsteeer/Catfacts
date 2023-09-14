#!/usr/bin/env python
import requests
import subprocess
cat = requests.get("https://catfact.ninja/fact").json() ["fact"]
subprocess.run(["/usr/bin/notify-send", "--icon=info", cat])

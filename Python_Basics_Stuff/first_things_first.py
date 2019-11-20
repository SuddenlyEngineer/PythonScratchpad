# Simple script, just trying to mess about with PyCharms and some tutorials.

import requests

resp = requests.get("https://realpython.com")
html = resp.text

sample_output = html[205:294]

print(sample_output)
print()

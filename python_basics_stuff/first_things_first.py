# Trying to get back into the swing of Python. Using PyCharms as an IDE.

import requests

resp = requests.get("https://realpython.com")
html = resp.text

snippet = html[205:294]

print(snippet)
print()

import requests
import sys

def help():
    print("Usage: postman_py.py <METHOD> <URL> -H 'key:value' -d DATA")

args = sys.argv[1:]
if len(args) < 2:       # Print help if no URL porvided
    help()
    sys.exit(1)

# Correct number of args passed
method = args[0].upper()
url = args[1]
header = {}
data = None

i = 2
while i < len(args):
    if args[i] == '-H' and i + 1 < len(args):
        h = args[i+1]
        key, val = h.split(":", 1)
        header[key.strip()] = val.strip()
        i += 2
    elif args[i] == 'd' and i + 1 < len(args):
        data = args[i+1]
        i += 2
    else:
        i += 1

# print(args, method, url, header, data)

try:
    response = requests.request(method, url, headers=header, data=data)
except requests.RequestException as err:
    print("Error:", err)
    sys.exit(1)


# Status
print(f"Status: {response.status_code}, {response.reason}")

# Content
print(response.text)

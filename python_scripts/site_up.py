import requests

url =input("Enter websites's url")

try:
    r=requests.get(url,timeout=5)
    print("Website is UP")
    print("Status code:", r.status_code)
except:
    print("Website is DOWN")

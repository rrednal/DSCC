import requests

server_url = "http://127.0.0.1:5000"

while True:
    try:
        a = int(input("Number to send (-1 to exit) -> "))
    except ValueError:
        print("Incorrect data")
        continue
    if a == -1:
        break
    payload = {"number": a}
    res = requests.post(server_url, json=payload)
    if res.status_code == 200:
        print("Server response:", res.json()["result"])
    else:
        print("Request send error")
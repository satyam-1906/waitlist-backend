import threading

def ping():
    import requests
    response = requests.get('https://waitlist-backend-wihf.onrender.com/')
    print(response.status_code)
    threading.Timer(600, ping).start()

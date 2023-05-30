import requests

def send_fibo_request():
    url = "http://192.168.56.11:31112/function/fibo1"
    data = "10" # example data to send
    response = requests.post(url, data=data)
    print(int(response.text))


send_fibo_request()
import requests

url = "http://192.168.56.11:31112/function/fibo1-1-h"
data = "20" # example data to send
response = requests.post(url, data=data)

print(type(response.status_code))
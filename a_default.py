import http.server
import socketserver
import os
import threading
import requests
import random
import time

PORT = 31113
fibo1_weight = 6
fibo2_weight = 3
fibo3_weight = 1
weight_sum = fibo1_weight + fibo2_weight + fibo3_weight

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

class MyHandler(http.server.BaseHTTPRequestHandler):
    lock = threading.Lock()
    
    def do_GET(self):
        if self.path == '/fibo-default':
            count = self.get_count('default-count.txt', 12)
            if count == 1:
                    url = "http://192.168.56.11:31112/function/default-2-1"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-1\n"
                            break
                        
            elif count == 2:
                    url = "http://192.168.56.11:31112/function/default-2-2"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-2\n"
                            break
            elif count == 3:
                    url = "http://192.168.56.11:31112/function/default-2-3"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-3\n"
                            break

            elif count == 4:
                    url = "http://192.168.56.11:31112/function/default-2-4"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-4\n"
                            break

            elif count == 5:
                    url = "http://192.168.56.11:31112/function/default-2-5"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-5\n"
                            break

            elif count == 6:
                    url = "http://192.168.56.11:31112/function/default-2-6"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-6\n"
                            break

            elif count == 7:
                    url = "http://192.168.56.11:31112/function/default-2-7"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-7\n"
                            break

            elif count == 8:
                    url = "http://192.168.56.11:31112/function/default-2-8"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-8\n"
                            break

            elif count == 9:
                    url = "http://192.168.56.11:31112/function/default-2-9"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-9\n"
                            break

            elif count == 10:
                    url = "http://192.168.56.11:31112/function/default-2-10"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-10\n"
                            break
            elif count == 11:
                    url = "http://192.168.56.11:31112/function/default-2-11"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-11\n"
                            break
            elif count == 12:
                    url = "http://192.168.56.11:31112/function/default-2-12"
                    data = "20" # example data to send
                    while True:
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()                        
                            message = f"Fibonacci value: {int(response.text)} fibo1-12\n"
                            break

            self.wfile.write(bytes(message, "utf8"))

        else:
            self.send_error(404)

    def get_count(self, filename, limit):
        count = 0
        with self.lock:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    try:
                        count = int(f.read())
                    except:
                        count = 1
            with open(filename, 'w') as f:
                if count >= limit:
                    f.write(str(1))
                else:
                    f.write(str(count + 1))
        return count

httpd = ThreadedHTTPServer(("", PORT), MyHandler)
print("serving at port", PORT)
httpd.serve_forever()
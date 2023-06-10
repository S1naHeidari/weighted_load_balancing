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
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-1"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-1\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-1\n"
                            break
                    else:
                        time.sleep(2)
                        
            elif count == 2:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-2"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-2\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-2\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 3:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-3"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-3\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-3\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 4:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-4"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-4\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-4\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 5:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-5"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-5\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-5\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 6:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-6"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-6\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-6\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 7:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-7"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-7\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-7\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 8:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-8"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-8\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-8\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 9:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-9"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-9\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-9\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 10:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-10"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-10\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-10\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 11:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-11"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-11\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-11\n"
                            break
                    else:
                        time.sleep(2)

            elif count == 12:
                while True:
                    url = "http://192.168.56.11:31112/function/default-2-12"
                    data = "20" # example data to send
                    with open('g1_overcommitted.txt', 'r') as f:
                        tf1 = f.read()

                    with open('g2_overcommitted.txt', 'r') as f:
                        tf2 = f.read()
                    
                    with open('g3_overcommitted.txt', 'r') as f:
                        tf3 = f.read()
                    # print(tf)
                    if tf1 == 'false' and tf2 == 'false' and tf3 == 'false':
                        response = requests.post(url, data=data)
                        if response.status_code == 200:
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()
                            print(f"Fibonacci value: {int(response.text)} fibo-1-12\n")
                            message = f"Fibonacci value: {int(response.text)} fibo-1-12\n"
                            break
                    else:
                        time.sleep(2)

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
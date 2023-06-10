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

        if self.path == '/fibo-rr':
            fibo1_weight = 1
            fibo2_weight = 1
            fibo3_weight = 1
            count = self.get_count('count.txt', 3)
            if count > 3:
                count = 3
            if count > 0 and count < fibo1_weight + 1:
                f1_count = self.get_count('f1-count.txt', 8)
                if f1_count == 1:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-1"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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
                
                elif f1_count == 2:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-2"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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

                elif f1_count == 3:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-3"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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

                elif f1_count == 4:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-4"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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

                elif f1_count == 5:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-5"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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
                
                elif f1_count == 6:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-6"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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

                elif f1_count == 7:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-7"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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

                elif f1_count == 8:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-8"
                        data = "20" # example data to send
                        with open('g1_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
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
                    
            elif count > fibo1_weight and count < fibo1_weight + fibo2_weight + 1:
                f2_count = self.get_count('f2-count.txt', 4)
                if f2_count == 1:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-1"
                        data = "20" # example data to send
                        with open('g2_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-2-1\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-1\n"
                                break
                        else:
                            time.sleep(2)

                elif f2_count == 2:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-2"
                        data = "20" # example data to send
                        with open('g2_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-2-2\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-2\n"
                                break
                        else:
                            time.sleep(2)

                elif f2_count == 3:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-3"
                        data = "20" # example data to send
                        with open('g2_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-2-3\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-4\n"
                                break
                        else:
                            time.sleep(2)

                elif f2_count == 4:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-4"
                        data = "20" # example data to send
                        with open('g2_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-2-4\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-4\n"
                                break
                        else:
                            time.sleep(2)

            elif count > fibo1_weight + fibo2_weight:
                f3_count = self.get_count('f3-count.txt', 2)
                if f3_count == 1:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-3-1"
                        data = "20" # example data to send
                        with open('g3_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-3-1\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-3-1\n"
                                break
                        else:
                            time.sleep(2)

                elif f3_count == 2:
                    while True:
                        url = "http://192.168.56.11:31112/function/fibo-3-2"
                        data = "20" # example data to send
                        with open('g3_overcommitted.txt', 'r') as f:
                            tf = f.read()
                        # print(tf)
                        if tf == 'false':
                            response = requests.post(url, data=data)
                            if response.status_code == 200:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()
                                print(f"Fibonacci value: {int(response.text)} fibo-3-2\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-3-2\n"
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
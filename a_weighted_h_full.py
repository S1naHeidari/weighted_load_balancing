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
        
        if self.path == '/fibo-heterogeneous':
            fibo1_weight = 6
            fibo2_weight = 3
            fibo3_weight = 1
            weight_sum = fibo1_weight + fibo2_weight + fibo3_weight
            count = self.get_count('count.txt', weight_sum)
            while True:
                if count > 0 and count < fibo1_weight + 1:
                    f1_count = self.get_count('f1-count-h.txt', 2)
                    if f1_count == 1:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-1-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-1-1-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-1-1-h\n"
                                break
                        else:
                            count = fibo1_weight + 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue
                    
                    elif f1_count == 2:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-1-2-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-1-2-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-1-2-h\n"
                                break
                        else:
                            count = fibo1_weight + 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue

                elif count > fibo1_weight and count < fibo1_weight + fibo2_weight + 1:
                    f2_count = self.get_count('f2-count-h.txt', 2)
                    if f2_count == 1:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-1-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-2-1-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-1-h\n"
                                break
                        else:
                            count = fibo1_weight + fibo2_weight + 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue

                    elif f2_count == 2:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-2-2-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-2-2-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-2-2-h\n"
                                break
                        else:
                            count = fibo1_weight + fibo2_weight + 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue
                            

                elif count > fibo1_weight + fibo2_weight:
                    f3_count = self.get_count('f3-count-h.txt', 2)
                    if f3_count == 1:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-3-1-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-3-1-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-3-1-h\n"
                                break
                        else:
                            count = 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue

                    elif f3_count == 2:
                        #while True:
                        url = "http://192.168.56.11:31112/function/fibo-3-2-h"
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
                                print(f"Fibonacci value: {int(response.text)} fibo-3-2-h\n")
                                message = f"Fibonacci value: {int(response.text)} fibo-3-2-h\n"
                                break
                        else:
                            count = 1
                            self.write_count(count)
                            #time.sleep(2)
                            continue
                
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
    
    def write_count(self, filename, value):
        with self.lock:
            with open(filename, 'w') as f:
                f.write(str(value))

httpd = ThreadedHTTPServer(("", PORT), MyHandler)
print("serving at port", PORT)
httpd.serve_forever()
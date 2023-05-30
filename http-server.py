import http.server
import socketserver
import os
import threading
import requests
import random

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
        if self.path == '/fibo-weighted':
            fibo1_weight = 6
            fibo2_weight = 3
            fibo3_weight = 1
            weight_sum = fibo1_weight + fibo2_weight + fibo3_weight
            count = self.get_count('count.txt', weight_sum)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if count > 0 and count < fibo1_weight + 1:
                f1_count = self.get_count('f1-count.txt', 6)
                if f1_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo1-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-1\n"
                
                elif f1_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo1-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-2\n"
                elif f1_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo1-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-3\n"
                elif f1_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo1-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-4\n"

                elif f1_count == 5:
                    url = "http://192.168.56.11:31112/function/fibo1-5"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-5\n"
                
                elif f1_count == 6:
                    url = "http://192.168.56.11:31112/function/fibo1-6"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-6\n"
                    
            elif count > fibo1_weight and count < fibo1_weight + fibo2_weight + 1:
                f2_count = self.get_count('f2-count.txt', 4)
                if f2_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo2-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-1\n"
                elif f2_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo2-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-2\n"
                elif f2_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo2-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-3\n"
                elif f2_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo2-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-4\n"

            elif count > fibo1_weight + fibo2_weight:
                f3_count = self.get_count('f3-count.txt', 2)
                if f3_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo3-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-1\n"

                elif f3_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo3-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-2\n"
            
            self.wfile.write(bytes(message, "utf8"))

        if self.path == '/fibo-heterogeneous':
            fibo1_weight = 6
            fibo2_weight = 3
            fibo3_weight = 1
            weight_sum = fibo1_weight + fibo2_weight + fibo3_weight
            count = self.get_count('count.txt', weight_sum)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if count > 0 and count < fibo1_weight + 1:
                f1_count = self.get_count('f1-count-h.txt', 2)
                if f1_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo1-1-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-1-h\n"
                
                elif f1_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo1-2-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-2-h\n"
                    
            elif count > fibo1_weight and count < fibo1_weight + fibo2_weight + 1:
                f2_count = self.get_count('f2-count-h.txt', 2)
                if f2_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo2-1-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-1-h\n"
                elif f2_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo2-2-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-2-h\n"

            elif count > fibo1_weight + fibo2_weight:
                f3_count = self.get_count('f3-count-h.txt', 2)
                if f3_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo3-1-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-1-h\n"

                elif f3_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo3-2-h"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-2-h\n"
            
            self.wfile.write(bytes(message, "utf8"))

        elif self.path == '/fibo-rr':
            fibo1_weight = 1
            fibo2_weight = 1
            fibo3_weight = 1
            count = self.get_count('count.txt', 3)
            if count > 3:
                count = 3
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if count > 0 and count < fibo1_weight + 1:
                f1_count = self.get_count('f1-count.txt', 6)
                if f1_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo1-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-1\n"
                
                elif f1_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo1-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-2\n"
                elif f1_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo1-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-3\n"
                elif f1_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo1-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-4\n"

                elif f1_count == 5:
                    url = "http://192.168.56.11:31112/function/fibo1-5"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-5\n"
                
                elif f1_count == 6:
                    url = "http://192.168.56.11:31112/function/fibo1-6"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-6\n"
                    
            elif count > fibo1_weight and count < fibo1_weight + fibo2_weight + 1:
                f2_count = self.get_count('f2-count.txt', 4)
                if f2_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo2-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-1\n"
                elif f2_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo2-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-2\n"
                elif f2_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo2-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-3\n"
                elif f2_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo2-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-4\n"

            elif count > fibo1_weight + fibo2_weight:
                f3_count = self.get_count('f3-count.txt', 2)
                if f3_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo3-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-1\n"

                elif f3_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo3-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-2\n"
            
            self.wfile.write(bytes(message, "utf8"))

        elif self.path == '/fibo-default':
            count = self.get_count('default-count.txt', 10)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if count == 1:
                    url = "http://192.168.56.11:31112/function/default-1-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-1\n"
            elif count == 2:
                    url = "http://192.168.56.11:31112/function/default-1-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-2\n"
            elif count == 3:
                    url = "http://192.168.56.11:31112/function/default-1-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-3\n"

            elif count == 4:
                    url = "http://192.168.56.11:31112/function/default-1-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-4\n"
            elif count == 5:
                    url = "http://192.168.56.11:31112/function/default-1-5"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-5\n"
            elif count == 6:
                    url = "http://192.168.56.11:31112/function/default-1-6"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-6\n"
            elif count == 7:
                    url = "http://192.168.56.11:31112/function/default-1-7"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-7\n"
            elif count == 8:
                    url = "http://192.168.56.11:31112/function/default-1-8"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-8\n"
            elif count == 9:
                    url = "http://192.168.56.11:31112/function/default-1-9"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-9\n"
            elif count == 10:
                    url = "http://192.168.56.11:31112/function/default-1-10"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} default-10\n"
            self.wfile.write(bytes(message, "utf8"))

        elif self.path == '/fibo-random':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            my_set = {1, 2, 3}
            random_number = random.choice(list(my_set))
            if random_number == 1:
                f1_count = self.get_count('f1-count.txt', 6)
                if f1_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo1-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-1\n"
                
                elif f1_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo1-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-2\n"
                elif f1_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo1-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-3\n"
                elif f1_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo1-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-4\n"

                elif f1_count == 5:
                    url = "http://192.168.56.11:31112/function/fibo1-5"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-5\n"
                
                elif f1_count == 6:
                    url = "http://192.168.56.11:31112/function/fibo1-6"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo1-6\n"
                    
            elif random_number == 2:
                f2_count = self.get_count('f2-count.txt', 4)
                if f2_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo2-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-1\n"
                elif f2_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo2-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-2\n"
                elif f2_count == 3:
                    url = "http://192.168.56.11:31112/function/fibo2-3"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-3\n"
                elif f2_count == 4:
                    url = "http://192.168.56.11:31112/function/fibo2-4"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo2-4\n"

            elif random_number == 3:
                f3_count = self.get_count('f3-count.txt', 2)
                if f3_count == 1:
                    url = "http://192.168.56.11:31112/function/fibo3-1"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-1\n"

                elif f3_count == 2:
                    url = "http://192.168.56.11:31112/function/fibo3-2"
                    data = "20" # example data to send
                    response = requests.post(url, data=data)
                    message = f"Fibonacci value: {int(response.text)} fibo3-2\n"
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
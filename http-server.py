import http.server
import socketserver
import os
import threading
PORT = 8000

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

class MyHandler(http.server.BaseHTTPRequestHandler):

    lock = threading.Lock()
    
    def do_GET(self):
        if self.path == '/counter':
            count = self.get_count()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if count > 0 and count < 7:
                # 192.168.56.11:31112/function/fibo1
                message = f"The current count is: {count} fibo1\n"
            elif count > 6 and count < 10:
                # 192.168.56.11:31112/function/fibo2
                message = f"The current count is: {count} fibo2\n"
            elif count > 9:
                # 192.168.56.11:31112/function/fibo3
                message = f"The current count is: {count} fibo3\n"
            self.wfile.write(bytes(message, "utf8"))
        else:
            self.send_error(404)

    def get_count(self):
        count = 0
        with self.lock:
            if os.path.exists('count.txt'):
                with open('count.txt', 'r') as f:
                    try:
                        count = int(f.read())
                    except:
                        count = 1
            with open('count.txt', 'w') as f:
                if count == 10:
                    f.write(str(1))
                else:
                    f.write(str(count + 1))
        return count

httpd = ThreadedHTTPServer(("", PORT), MyHandler)
print("serving at port", PORT)
httpd.serve_forever()
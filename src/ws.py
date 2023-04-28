"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Molly Ruley
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import is_square
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            status, content, content_type = 200, "OK", "text/html"
        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            if self.headers.get('Content-Type') == 'application/json':
                content_type = "application/json"
                if number.isnumeric():
                    d = {
                        "number": int(number),
                        "square": is_square(int(number)),
                        "schemaVersion": 1,
                        "label": "erau02",
                        "message": f"square checker Web-service",
                        "color": "blue"
                    }
                    status, content = 200, json.dumps(d)
                else:
                    status, content = 400, "Bad Request"
            else:
                content_type = 'text/html'
                result = f"{number} is {'a perfect square' if is_square(int(number)) else 'not a perfect square'}." if number.isnumeric() else ""
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        else:
            status, content = 404, "Not Found"
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")

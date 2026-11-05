from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            hostname = socket.gethostname()
            pod_ip = os.environ.get("POD_IP", "unknown")
            message = f"OK - hostname: {hostname}, pod IP: {pod_ip}\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Server running on port {port}")
    server.serve_forever()

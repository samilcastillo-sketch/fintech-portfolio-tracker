"""
Fintech Portfolio HTTP Server & REST API
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from .portfolio import PortfolioEngine

PORT = int(os.environ.get("PORT", "5004"))
HOST = os.environ.get("HOST", "0.0.0.0")

class PortfolioHandler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, data: dict):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            file_path = os.path.join(os.path.dirname(__file__), "public", "index.html")
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == "/health":
            self._send_json(200, {"status": "healthy", "service": "fintech-portfolio-tracker"})
        elif self.path == "/api/v1/portfolio":
            summary = self.server.engine.calculate_summary()
            self._send_json(200, summary)
        else:
            self._send_json(404, {"error": "Not Found"})

    def do_POST(self):
        if self.path == "/api/v1/positions":
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            try:
                data = json.loads(raw)
                result = self.server.engine.add_position(
                    symbol=data["symbol"],
                    quantity=data["quantity"],
                    buy_price=data["buy_price"]
                )
                self._send_json(201, result)
            except Exception as e:
                self._send_json(400, {"error": str(e)})
        else:
            self._send_json(404, {"error": "Not Found"})

def run():
    server = HTTPServer((HOST, PORT), PortfolioHandler)
    server.engine = PortfolioEngine()
    print(f"[Portfolio Tracker] Web Dashboard active on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    run()

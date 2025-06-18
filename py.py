from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ('10.203.50.100', 443)  # HTTPS стандартный порт 443
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Добавляем SSL
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="key.pem",
    certfile="cert.pem",
    server_side=True
)

print(f"HTTPS сервер запущен на https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
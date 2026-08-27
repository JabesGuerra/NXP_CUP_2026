import http.server
import socketserver

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Permitir iframe y comunicación sin restricciones locales
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

Handler = CustomHTTPRequestHandler

print(f"==================================================")
print(f" Servidor Vaporwave corriendo en:")
print(f" http://localhost:{PORT}")
print(f"==================================================")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
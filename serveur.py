from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        """Définit les en-têtes de la réponse."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_POST(self):
        """Gère les requêtes POST."""
        if self.path == "/player_data":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                # Charger les données envoyées par le client
                player_data = json.loads(body)
                print("Données reçues du joueur :", player_data)

                # Exemple : Calculer une position fictive en fonction des données reçues
                position = {
                    "x": 10 + player_data.get("deplacement", 0),
                    "y": 5,
                    "z": 3
                }

                # Envoyer la position calculée au client
                self._set_headers(200)
                self.wfile.write(json.dumps(position).encode())
            except json.JSONDecodeError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

# Lancer le serveur
def run_server(server_class=HTTPServer, handler_class=RequestHandler, host="localhost", port=9999):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur {host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

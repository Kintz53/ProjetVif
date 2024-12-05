from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 9999

# Grille 3x3 initiale
grid = [[".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]]

# Position initiale des joueurs
players = {}

def get_environment(x, y):
    """Renvoie les cases adjacentes à la position (x, y) dans la grille."""
    environment = {}
    if x > 0:
        environment["gauche"] = grid[x-1][y]
    if x < len(grid) - 1:
        environment["droite"] = grid[x+1][y]
    if y > 0:
        environment["haut"] = grid[x][y-1]
    if y < len(grid[0]) - 1:
        environment["bas"] = grid[x][y+1]
    return environment

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        """Définit les en-têtes de réponse."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_POST(self):
        """Gère les requêtes POST."""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        if self.path == "/player_data":
            pseudo = data.get("pseudo")
            if pseudo not in players:
                # Ajouter un nouveau joueur
                players[pseudo] = {"x": 1, "y": 1, "type": data.get("type", "Vif")}
                grid[1][1] = pseudo  # Position initiale
                response = {
                    "message": f"Bienvenue, {pseudo} !",
                    "position": (1, 1),
                    "environment": get_environment(1, 1),
                    "status": "non"
                }
            else:
                # Déplacer un joueur existant
                player = players[pseudo]
                direction = data.get("deplacement", "")
                x, y = player["x"], player["y"]

                # Nettoie l'ancienne position
                grid[x][y] = "."

                # Mise à jour de la position selon la direction
                if direction == "haut" and y > 0:
                    y -= 1
                elif direction == "bas" and y < len(grid[0]) - 1:
                    y += 1
                elif direction == "gauche" and x > 0:
                    x -= 1
                elif direction == "droite" and x < len(grid) - 1:
                    x += 1

                # Applique la nouvelle position
                player["x"], player["y"] = x, y
                grid[x][y] = pseudo

                response = {
                    "message": f"{pseudo} s'est déplacé vers {direction}.",
                    "position": (x, y),
                    "environment": get_environment(x, y),
                    "status": "non"
                }

            self._set_headers(200)
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            response = {"error": "Chemin inconnu."}
            self.wfile.write(json.dumps(response).encode())

def run():
    """Démarre le serveur."""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Serveur démarré sur {HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

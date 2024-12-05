import http.client
import json

HOST = "localhost"
PORT = 9999


def send_player_data(file_path):
    try:
        # Charger le fichier JSON
        with open(file_path, "r") as file:
            player_data = json.load(file)

        # Préparer la connexion et envoyer les données
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "application/json"}
        body = json.dumps(player_data)
        conn.request("POST", "/player_data", body=body, headers=headers)

        # Recevoir la réponse
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode()
            return json.loads(data)  # On suppose une réponse JSON
        else:
            return f"Erreur : {response.status} {response.reason}"
    except Exception as e:
        return f"Erreur lors de l'envoi des données : {e}"
    finally:
        conn.close()


# Programme principal
if __name__ == "__main__":
    file_path = "player.json"  # Chemin vers le fichier JSON du joueur
    print("Envoi des données du joueur...")
    response = send_player_data(file_path)
    print("Réponse du serveur :", response)

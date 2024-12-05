import http.client
import json

HOST = "localhost"
PORT = 9999
def connexion(pseudo,type_de_joueur):
    try:
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "str"}
        joueur = {'pseudo': pseudo,'type':type_de_joueur}
        body=json.dumps(joueur)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode()
            return json.loads(data)
        else:
            return f"Erreur : {response.status} {response.reason}"
    except Exception as e:
        return f"Erreur lors de l'envoi des données : {e}"

def deplacement(pseudo,type_de_joueur):
    try:
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "str"}
        deplac=input('Donner votre direction : droite,gauche,haut ou bas')
        joueur = {'pseudo': pseudo, 'type': type_de_joueur, 'deplacement':deplac}
        body = json.dumps(joueur)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode()
            return json.loads(data)
        else:
            return f"Erreur : {response.status} {response.reason}"
    except Exception as e:
        return f"Erreur lors de l'envoi des données : {e}"

if __name__ == "__main__":
    pseudo = input('pseudo')
    type_de_joueur = input('Type de joueur : "Loup" ou "Vif" ')
    connexion(pseudo,type_de_joueur)


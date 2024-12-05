import http.client
import json

HOST = "localhost"
PORT = 9999

def connexion(pseudo, type_de_joueur):
    try:
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "application/json"}
        joueur = {'pseudo': pseudo, 'type': type_de_joueur}
        body = json.dumps(joueur)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return {"error": f"Erreur : {response.status} {response.reason}"}
    except Exception as e:
        return {"error": f"Erreur lors de la connexion : {e}"}

def deplacement(pseudo, type_de_joueur, connect):
    try:
        print("Environnement :", connect.get("environment", {}))
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "application/json"}
        deplac = input("Donner votre direction : droite, gauche, haut ou bas : ").lower()
        joueur = {'pseudo': pseudo, 'type': type_de_joueur, 'deplacement': deplac}
        body = json.dumps(joueur)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return {"error": f"Erreur : {response.status} {response.reason}"}
    except Exception as e:
        return {"error": f"Erreur lors du déplacement : {e}"}
def ValidationTour(pseudo,type_de_joueur):
    try:
        conn = http.client.HTTPConnection(HOST, PORT)
        headers = {"Content-Type": "application/json"}
        joueur = {'pseudo': pseudo, 'type': type_de_joueur}
        body = json.dumps(joueur)
        conn.request("POST", "/player_data", body=body, headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return {"error": f"Erreur : {response.status} {response.reason}"}
    except Exception as e:
        return {"error": f"Erreur lors du déplacement : {e}"}

if __name__ == "__main__":
    pseudo = input("Entrez votre pseudo : ")
    type_de_joueur = input('Type de joueur ("Loup", "Vif") : ')

    connect = connexion(pseudo, type_de_joueur)
    if "error" in connect:
        print(connect["error"])
    else:
        print(connect["message"], "\nPosition :", connect["position"])

    # Boucle principale
    while connect["status"] not in ['Win', 'Lose']:
        connect = deplacement(pseudo, type_de_joueur, connect)
        if "error" in connect:
            print(connect["error"])
            break
        else:
            print(connect["message"], "\nPosition :", connect["position"])

        continuer=ValidationTour(pseudo,type_de_joueur)
        while(continuer['status']!='Action'):
            continuer = ValidationTour(pseudo, type_de_joueur)



    if connect["status"] == "Win":
        print("Félicitations, vous avez gagné !")
    elif connect["status"] == "Lose":
        print("Dommage, vous avez perdu !")

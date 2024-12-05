import socket

HOST = 'localhost'
PORT = 50007

def get_position(s):
    """Demander la position actuelle au serveur."""
    s.sendall(b"GET_POSITION")
    data = s.recv(1024)
    return data.decode()

def set_position(s, new_position):
    """Envoyer une nouvelle position au serveur."""
    command = f"SET_POSITION {new_position}"
    s.sendall(command.encode())
    data = s.recv(1024)
    return data.decode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Connexion au serveur
        s.connect((HOST, PORT))
        print("Connecté au serveur.")

        # Récupérer la position actuelle
        current_position = get_position(s)
        print("Position actuelle :", current_position)

        # Changer de position
        new_position = "x=3,y=4"  # Exemple de nouvelle position
        response = set_position(s, new_position)
        print("Réponse après mise à jour :", response)

        # Vérifier la nouvelle position
        updated_position = get_position(s)
        print("Nouvelle position :", updated_position)
    except Exception as e:
        print("Erreur :", e)
import socket

HOST = 'localhost'
PORT = 50007

def get_position(s):
    s.sendall(b"GET_POSITION")
    data = s.recv(1024)
    return data.decode()

def set_position(s, new_position):
    command = f"SET_POSITION {new_position}"
    s.sendall(command.encode())
    data = s.recv(1024)
    return data.decode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connecté au serveur.")

        current_position = get_position(s)
        print("Position actuelle :", current_position)
        new_position = '''json{
                "pseudo":"player",
                "role":"vif"
                "deplacement"=
        }
        '''
        response = set_position(s, new_position)
        print("Réponse après mise à jour :", response)

        updated_position = get_position(s)
        print("Nouvelle position :", updated_position)
    except Exception as e:
        print("Erreur :", e)

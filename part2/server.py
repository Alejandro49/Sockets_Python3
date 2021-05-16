import socket

# header de longitud constante que indica el tamaño de mensaje que vamos a mandar
HEADERSIZE = 10   # 9.999.999.999  nº máximo de caracteres del mensaje

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 10000)
s.bind(server_address)
s.listen(3)

while True:
    # ns = nuevo socket que responde al cliente conectado
    print("Waiting for a connection...")
    ns, client_address = s.accept()
    print(f"Connection from {client_address} has been established!")

    msg = "holas"
    # fString
    mensaje = f"{len(msg):<{HEADERSIZE}}" + msg

    ns.send(bytes(mensaje, "utf-8"))




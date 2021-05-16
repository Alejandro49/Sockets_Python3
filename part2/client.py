import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 10000)
s.connect(server_address)

while True:
    mensajeCompleto = ""
    nuevoMensaje = True
    while True:
        # Tengo que leer al menos 10 caracteres de golpe para ver el tamaño del mensaje
        msg = s.recv(16)
        # Leo la cabecera
        if nuevoMensaje:
            print(f"longitud del nuevo mensaje: {msg[:HEADERSIZE]}")
            # parseo a int los 10 primeros caracteres
            # que se que contienen la longitud exacta del mensaje que viene
            msglength = int(msg[:HEADERSIZE])
            nuevoMensaje = False

        mensajeCompleto += msg.decode("utf-8")

        # Comprobación de que hemos recbido el mensaje completo
        # HEADERSIZE no forma parte de la longitud de mensaje establecida
        if len(mensajeCompleto) - HEADERSIZE == msglength:
            print("Mensaje completo recibido")
            # Esconder la cabecera
            print(mensajeCompleto[HEADERSIZE:])
            # Esperando al siguiente mensaje
            nuevoMensaje = True
            mensajeCompleto = ""

    print(mensajeCompleto)







import socket
port = 1244
address = "127.0.0.1"
BUFF_SIZE = 1024

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message = input("Enter Message")
con.send(bytes(message, "utf-8"))


data = con.recv(BUFF_SIZE)
con.close()
print(data.decode("utf-8"))
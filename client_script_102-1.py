import socket


ip_add_input = input("Please enter the IP address of Machine you want to connect to; example: (174.158.64.2): ")
username_input = input("Please enter your name in the organization: ")

client_To_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_To_server_socket.connect((ip_add_input, 5001))
client_To_server_socket.send(username_input.encode("utf-8"))

response = client_To_server_socket.recv(1024).decode("utf-8")
client_To_server_socket.close()

print("Server response for user access request:", response)
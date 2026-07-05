import socket
import csv



database = {}
with open("/root/user_database.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    database[row["username"]] = row["status"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    # |             |-->we're using TCP Why not UDP(SOCK_DGRAM)? Because UDP can drop or reorder packets.   ; STREAM means data flows continuously like a stream, in order, guaranteed. Opposite of SOCK_DGRAM where DGRAM = Datagram = individual packets, no guarantee.
                                    # |
                                    # |-->we're using IPv4 (regular IP addresses like 192.168.x.x) ;  AF stands for Address Family, INET stands for Internet (IPv4)

server_socket.bind(("0.0.0.0", 5001)) #what is bind? It's like telling the OS: "this socket owns this address and port; any message arriving on port 5001 belongs to me." why port 5001?   it's just a free port. Ports below 1024 are reserved for system services, like 80 for HTTP ...
server_socket.listen(5)  # what is listen?   bind said "this is my door", listen says "I'm now open for visitors."  and 5 it is the backlog or let say the maximum number of connections  Why specificlly 5? It's a common default for small systems if the infrastruce was big the number should scale

while True:  #What is this? This tells the server to run forever; keep accepting connections non-stop

  client_socket, client_address= server_socket.accept() #What is accept?  accept() is the moment someone knocks and you open the door.
  request = client_socket.recv(1024).decode("utf-8") #what is recv()? ; it waits for the client to send data, like waiting for someone to speak after you pick up the phone.
                              # |    # |     # |--> Why UTF-8?  ir is a universal text encoding  supports most languages English, Arabic, French, basically every language.                             # |    # |
                              # |    # |
                              # |    # |-->Network data travels as raw bytes, not text  decode('utf-8')  converts it to readable python string
                              # |
                              # |--> what is 1024 between () --->it's the maximum number of bytes to receive at once  (such small verification mlike username is maybe about 20 bytes so 1024 is more than enough)
                              
  username= request.strip()  # when the client sends the username, it might come with extra invisible characters  like "\n"  a space " " at the end; strip() removes those so we get "ibrahim" not "ibrahim\n" and get no macth
  if username in database and database[username] == "active": # so we check here the username row and status row from above (in line 6-10)
    response="YES"
  else: 
    response = "NO"

  client_socket.send(response.encode("utf-8")) 
               # |             # |-->    before we used decode because we were recieving data as bytes, but now we have raw python string and we need to send it to client as bytes so he can read it therefore we used encode
               # |     
               # |--> opposite of recv above (in line 23) this time we send data back to client which is response (in line 31-34)
  client_socket.close() #we closed it so we free up resources like pressing read icon phone in the call, without it we will like (staying on the line in phone)




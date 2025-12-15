import socket 

target = input("Enter IP or domain: ")
ports=[21,22,80,443,3306]
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result= s.connect_ex((target,port))
    if result ==0:
        print(f"Port {port} is open")
    else: 
        print(f"Port {port} is closed")
    s.close()


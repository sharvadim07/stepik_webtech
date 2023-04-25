import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 2222))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        print(f"new connection with {addr}")
        data = conn.recv(1024)
        print(f"recieved data = {data.decode()}")
        if not data or data.decode() == "close":
	    print(f"close connection with {addr}")
	    conn.close()
            break
	print(f"send data to {addr}")
        conn.sendall(data)
        print(f"close connection with {addr}")
        conn.close()

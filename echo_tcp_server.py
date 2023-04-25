import socket
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 2222))
    max_connections = 10
    s.listen(max_connections)
    for i in range(max_connections):
        worker_pid = os.fork()
        if not worker_pid:
            conn, addr = s.accept()
            print(f"new connection with {addr}")
            data = conn.recv(1024)
            print(f"recieved data = {data.decode()}")
            if not data or data.decode() == "close":
                print(f"close connection with {addr}")
                conn.close()
                exit(0)
            print(f"send data to {addr}")
            conn.sendall(data)
            print(f"close connection with {addr}")
            conn.close()
            exit(0)
        else:
            print(f"process started {worker_pid}")
    for i in range(max_connections):
       exit_pit, exit_status = os.wait()
       print(f"process finished {exit_pit} with status {exit_status}")
from socket import *
import socket
import threading
import logging
from datetime import datetime

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        try:
            while True:
                data = self.connection.recv(1024)
                if not data:
                    break

                request = data.decode('utf-8').strip()
                
                if request == "TIME":
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    response = f"JAM {current_time}\r\n"
                    self.connection.sendall(response.encode('utf-8'))

                elif request == "QUIT":
                    break
                else:
                    # Optional: ignore unrecognized commands
                    continue

        except Exception as e:
            logging.warning(f"Error with client {self.address}: {e}")
        finally:
            self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('172.16.16.101', 45000))
        self.my_socket.listen(5)

        ip, port = self.my_socket.getsockname()
        logging.warning(f"Server is listening on {ip}:{port}")

        while True:
            connection, client_address = self.my_socket.accept()
            logging.warning(f"Connection from {client_address}")
            client_thread = ProcessTheClient(connection, client_address)
            client_thread.start()
            self.the_clients.append(client_thread)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    main()
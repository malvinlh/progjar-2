import socket
import threading
import time

SERVER_HOST = '172.16.16.101'
SERVER_PORT = 45000

def time_request(client_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print(f"[Client-{client_id}] Connected to server")

            # Kirim permintaan waktu
            client_socket.sendall(b"TIME\r\n")
            response = client_socket.recv(1024).decode()
            print(f"[Client-{client_id}] Server replied: {response.strip()}")

            # Tutup koneksi dengan QUIT
            client_socket.sendall(b"QUIT\r\n")
            print(f"[Client-{client_id}] Sent QUIT")

    except Exception as e:
        print(f"[Client-{client_id}] Error: {e}")

def main():
    num_clients = 5  # Bisa diubah sesuai kebutuhan
    threads = []

    for i in range(num_clients):
        t = threading.Thread(target=time_request, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.1)  # Optional: jeda kecil antar thread start

    for t in threads:
        t.join()

    print("All client threads finished.")

if __name__ == "__main__":
    main()
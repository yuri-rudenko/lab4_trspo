import socket

# Спочатку запустити сервер в одному вікні, потім клієнт в іншому

# Server
def start_server():
    host = '0.0.0.0' 
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(data) 

# Client 
def start_client():
    host = '127.0.0.1' 
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    choice = input("Start as server or client? (s/c): ").lower()
    if choice == 's':
        start_server()
    elif choice == 'c':
        start_client()
    else:
        print("Invalid choice. Please run the program again.")
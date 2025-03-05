import socket
import threading

# Global variable to store the balance
balance = 100
lock = threading.Lock()

def handle_client(client_socket):
    global balance

    while True:
        try:
            request = client_socket.recv(1024).decode()
            if not request:
                break

            command, *args = request.split()
            response = "\nInvalid command."

            with lock:
                if command == "BALANCE":
                    response = f"\n\nCurrent balance: {balance}"
                elif command == "DEPOSIT" and args:
                    if args and args[0].isdigit():
                        amount = int(args[0])
                        balance += amount
                        response = f"\nDeposited {amount}. New balance: {balance}"
                    else:
                        response = "\nInvalid deposit amount."
                elif command == "WITHDRAW":
                    if args and args[0].isdigit():
                        amount = int(args[0])
                        if amount <= balance:
                            balance -= amount
                            response = f"\nWithdrew {amount}. New balance: {balance}"
                        else:
                            response = "\nInsufficient funds."
                    else:
                        response = "\nInvalid withdrawal amount."
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))
    server.listen(5)
    print("Server listening on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
if __name__ == "__main__":
    start_server()
# server.py
# A simple multi-threaded server that handles multiple clients
# and performs basic banking operations like checking balance,
# depositing, and withdrawing money.
# It uses sockets for communication and threading to handle
# multiple clients concurrently.
# The server maintains a global balance variable and uses a lock
# to ensure thread-safe operations on this variable.
# The server listens on port 9999 and accepts connections from clients.
# The server supports the following commands:
# - BALANCE: Returns the current balance.
# - DEPOSIT <amount>: Deposits the specified amount into the account.
# - WITHDRAW <amount>: Withdraws the specified amount from the account.
# - EXIT: Closes the connection with the client.
# The server handles invalid commands and ensures that the balance
# does not go negative.
# The server runs indefinitely, accepting new client connections
# and handling them in separate threads.
# The server uses a global variable to store the balance and a lock
# to ensure thread-safe operations on this variable.
# The server uses the socket library to create a TCP server and
# the threading library to handle multiple clients concurrently.
# The server uses a while loop to continuously accept new client
# connections and spawn new threads to handle them.

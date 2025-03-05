# KAI POKRANDT
# 010925472

import socket

def start_client():
    print("Starting client...")
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client.connect(("127.0.0.1", 9999))
    print("Connected to server.")

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ")
    
        if choice == "1":
            client.send("\nBALANCE".encode())
        elif choice == "2":
            amount = input("\nEnter amount to deposit: ")
            if amount.isdigit():
                client.send(f"\nDEPOSIT {amount}".encode())
            else:
                print("\nInvalid amount.")
                continue
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            if amount.isdigit():
                client.send(f"\nWITHDRAW {amount}".encode())
            else:
                print("\nInvalid amount.")
                continue
        elif choice == "4":
            print("\nExiting...")
            client.send("EXIT".encode())
            client.close()
            break
        else:
            print("\nInvalid choice.")
            continue

        response = client.recv(1024).decode()
        print(f"\nServer response: {response}")


if __name__ == "__main__":
    start_client()

# client.py

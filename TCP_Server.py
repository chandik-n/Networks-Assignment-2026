from socket import *
import Protocol # Custom made, see Protocol.py
import threading 

accounts = dict() # A dictionary of the accounts present in the textfile.


def handle_client(connectionSocket: socket, address: tuple):
    temp = connectionSocket.recv(1024).decode().split("\n")
    try:
        if temp[0] == Protocol.initiate_protocol(1): # Logs into account. 
            handle_login(connectionSocket, address)
        elif temp[0] == Protocol.initiate_protocol(2): # Creates an account.
            handle_account_creation(connectionSocket, address)
        elif temp[0] == Protocol.initiate_protocol(3): # Closes the program.
             handle_program_close(connectionSocket, address)
        
        else:
                print("Not a valid protocol. Closing connection.")

    except: # Possible exception of temp not being split appropriately.
        print("Error: Check how temp has been configured:")
        print(temp)

    finally:
        connectionSocket.close()

    pass

def handle_login(connectionSocket: socket, address: tuple):
    print("Method successfully checked.")
    connectionSocket.close()

def handle_account_creation(connectionSocket: socket, address: tuple):
    pass

# This will be much more important later.
def handle_program_close(connectionSocket: socket, address: tuple):
    connectionSocket.close()
    print("User:\t", "disconnected.") 


# Loads the accounts from the accounts.txt.
def load_accounts(txt: str = "accounts.txt") -> None:
    accounts.clear()
    with open(txt, 'r') as f:
        for line in f:
            username, password = line.split(",")
            accounts[username] = password

# Appends an account into accounts.txt.
def write_account(username: str, password: str) -> None:
    load_accounts() #HACK: May remove.
    if username not in accounts:
        with open("accounts.txt", "a") as f:
            f.write("f:{username},{password}\n")

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    load_accounts() # Loading the accounts from accounts.txt.
    print("The server is up and running.")
    while True:
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target = handle_client, args = (connectionSocket, addr))
        thread.start()
    
# Sends a message to the client for simplicity.
def send_message(connectionSocket: socket, message: str) -> None:
    connectionSocket.send(message.encode())
    pass

# Receives a message from the client.
def receive_message(connectionSocket: socket) -> str:
    return connectionSocket.recv(1024).decode()
    
if __name__ == "__main__":
    main()
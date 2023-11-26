import cryptography.fernet as Fernet
from cryptography import fernet
from cryptography.fernet import Fernet
import mysql.connector

print("                              E  N  C  R  Y  P  T  E  R    A  N  D    D  E  C  R  Y  P  T  E  R  ")
print("                           ________________________________________________________________________")
print()

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message.decode()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode()).decode()
    return decrypted_message

def store_encrypted_data(connection, encrypted_data, encryption_key):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO encrypted_messages (encrypted_data, encryption_key) VALUES (%s, %s)", (encrypted_data, encryption_key) )
    connection.commit()

def retrieve_encrypted_data(connection, key):
    cursor = connection.cursor()
    cursor.execute("SELECT encrypted_data FROM encrypted_messages where encryption_key = %s ", (key,))
    encrypted_data = cursor.fetchone()[0]
    return encrypted_data

def connect_to_mysql():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="chicken",
        database="encrypted_stuff"
    )
    return connection

def main():
    connection = connect_to_mysql()

    while True:
        print()
        print("Choose an option:")
        print()
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message you want to encrypt: ")
            key = generate_key()
            encrypted_message = encrypt_message(message, key)
            store_encrypted_data(connection, encrypted_message, key)
            print("Encrypted message: ", encrypted_message)
            print("Key: ", key)

        elif choice == "2":
            key = input("Enter the key: ")
            encrypted_message = retrieve_encrypted_data(connection, key)
            decrypted_message = decrypt_message(encrypted_message, key)
            print("Decrypted message: ", decrypted_message)

        elif choice == "3":
            connection.close()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
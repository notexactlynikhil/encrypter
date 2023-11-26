# Encrypter & Decrypter
Basic program to encrypt and decrypt text using the Fernet library (my 12th grade project)

## Prerequisites
 * Have MySQL installed.
 * Have python 3 installed.
 * Have the fernet library and mysql-connector installed using (in pwsh/cmd)-
```
   pip3 install fernet
   pip3 install mysql-connector
   pip3 install mysql-connector-python
```
## Setting up your database in MySQL
 * Run the following commands in the mysql shell -
```
   create database encrypted_stuff;
   use encrypted_stuff
   create table encrypted_messages (encrypted_data varchar(900), key varchar(900));
```
## Things to keep in mind
 * Set your host as localhost in encrypter.py
 * Set your password according to whatever you set while isntalling MySQL

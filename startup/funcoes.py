from cryptography.fernet import Fernet
import os
import time as t
import getpass
import random as r
import sys
import msvcrt
from colorama import Fore, Back, Style, init
import datetime

def cripto():
    # Gera uma chave e salva em um arquivo
    def generate_key():
        key = Fernet.generate_key()
        with open('filekey.key', 'wb') as key_file:
            key_file.write(key)

    # Carrega a chave
    def load_key():
        return open('filekey.key', 'rb').read()

    # Criptografa o arquivo
    def encrypt_file(filename):
        key = load_key()
        fernet = Fernet(key)
        
        with open(filename, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)

        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    # Gera a chave uma vez
    generate_key()

    # Criptografa o arquivo 'meuarquivo.txt'
    encrypt_file('listasenha.txt')

    #print("Arquivo criptografado com sucesso!")
########################################################################################

def uncripto():
        # Carrega a chave
    def load_key():
        return open('filekey.key', 'rb').read()

    # Descriptografa o arquivo
    def decrypt_file(filename):
        key = load_key()
        fernet = Fernet(key)
        
        with open(filename, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        
        decrypted = fernet.decrypt(encrypted)

        with open(filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

    # Descriptografa o arquivo 'meuarquivo.txt'
    decrypt_file('listasenha.txt')

    #print("Arquivo descriptografado com sucesso!")
########################################################################################

def criptosenha():

    def generate_keysenha():
        key = Fernet.generate_key()
        with open('filekeysenha.key', 'wb') as key_file:
            key_file.write(key)

    def load_keysenha():
        return open('filekeysenha.key', 'rb').read()

    def encrypt_filesenha(filename):
        key = load_keysenha()
        fernet = Fernet(key)
        
        with open(filename, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)

        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    generate_keysenha()

    encrypt_filesenha('1senhamestre.txt')

########################################################################################
def uncriptosenha():

    def load_keysenha():
        return open('filekeysenha.key', 'rb').read()

    def decrypt_filesenha(filename):
        key = load_keysenha()
        fernet = Fernet(key)
        
        with open(filename, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        
        decrypted = fernet.decrypt(encrypted)

        with open(filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

    decrypt_filesenha('1senhamestre.txt')

########################################################################################
def custom_getpass(prompt="Senha:", char_mask='•'):
    print(prompt, end='', flush=True)
    senha = ""
    while True:
        char = msvcrt.getch()
        if char == b'\r':  # Enter key pressed
            print('')
            break
        elif char == b'\x08':  # Backspace pressed
            if len(senha) > 0:
                senha = senha[:-1]
                sys.stdout.write('\b \b')
        else:
            senha += char.decode('utf-8')
            sys.stdout.write(char_mask)
        sys.stdout.flush()
    return senha

########################################################################################
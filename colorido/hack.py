import time
import random
from colorama import Fore, Back, Style, init

# Inicializa o colorama para garantir a compatibilidade com Windows
init()

# Cores para escolher
colors = [Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.RED]

# Mensagens aleatórias para simular dados ou códigos
messages = [
    "Accessing secure server...",
    "Decrypting secret data...",
    "Bypassing firewall...",
    "Compiling malicious code...",
    "Data packet received: {} bytes".format(random.randint(1000, 10000)),
    "Running brute-force attack...",
    "Connection established with {}.{}".format(random.randint(1, 255), random.randint(1, 255)),
    "Exploiting vulnerability...",
    "Downloading confidential files...",
    "Data analysis in progress...",
    "Transmission successful!",
]

# Número de mensagens para exibir
num_messages = 100

# Exibe as mensagens com cores aleatórias
for _ in range(num_messages):
    color = random.choice(colors)
    message = random.choice(messages)
    print(color + message + Style.RESET_ALL)
    
    # Intervalo de tempo entre mensagens para simular atividade
    time.sleep(random.uniform(0.1, 0.3))  # Ajuste conforme necessário

import pygame
import string

import random
import pyfiglet
import os
import time
from tqdm import tqdm
from termcolor import colored
from colorama import init, Fore, Style

init()
os.system('cls' if os.name == 'nt' else 'clear')

music_file = os.path.join(os.path.dirname(__file__), 'PHANTOGRAM - BLACK OUT DAYS SLOWED.mp3')
# Inicializar pygame
pygame.init()

# Configurar el mezclador de audio
pygame.mixer.init()

# Cargar archivo de música
pygame.mixer.music.load(music_file)

# Reproducir música en bucle
pygame.mixer.music.play(-1)

# Resto del código...

print(colored(pyfiglet.figlet_format("Secure password generator"), "magenta"))
print()
print()
print(colored("Author   : Evil Bryan Hernandez", "magenta"))
print(colored("TikTok   : https://www.tiktok.com/@seguidores_del_temach", "magenta"))
print(colored("github   : https://github.com/EvilZyBH", "magenta"))
print()
print()


def generate_password(length, keywords):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    with tqdm(total=length, desc="Generando contraseña", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        for _ in range(length):
            time.sleep(0.1)  # Pausa para una barra de progreso lenta
            if keywords:
                keyword = random.choice(keywords)
                keywords.remove(keyword)  # Eliminar la palabra clave seleccionada para evitar repeticiones
                password += keyword + random.choice(characters)
            else:
                password += random.choice(characters)
            pbar.update(1)
        pbar.set_postfix(security=verificar_seguridad(password), refresh=True)
    return password


def verificar_seguridad(password):
    security = 'No tan fuerte'
    if len(password) >= 10 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
        security = 'Más o menos segura'
        if any(c.islower() for c in password) and any(c.isupper() for c in password):
            security = 'Segura'
            if any(c in string.punctuation for c in password):
                security = 'Muy segura'
    return security


def main():
    while True:
        length_input = input(Fore.GREEN + "Ingresa la longitud deseada para la contraseña (debe ser un número entero): ")
        if not length_input.isdigit():
            print("Error: Ingresa solo números enteros.")
        else:
            length = int(length_input)
            break

    while True:
        num_keywords_input = input(Fore.GREEN + f"Ingresa el número de palabras clave a combinar (debe ser un número entero, no mayor que {length}): ")
        if not num_keywords_input.isdigit():
            print("Error: Ingresa solo números enteros.")
        else:
            num_keywords = int(num_keywords_input)
            if num_keywords > length:
                print(f"Error: El número de palabras clave debe ser menor o igual a la longitud deseada ({length}).")
            else:
                break

    keywords = []
    for i in range(num_keywords):
        keyword = input(f"Ingrese la palabra clave {i+1}: ")
        keywords.append(keyword)

    password = generate_password(length, keywords)
    print(colored("Contraseña generada:", "green"), password)
    print()
    print(colored("Verificando la seguridad de la contraseña:", "cyan"))
    with tqdm(total=100, desc="Progreso", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        for _ in range(100):
            time.sleep(0.03)  # Pausa para una barra de progreso lenta
            pbar.update(1)
        pbar.set_postfix(security=verificar_seguridad(password), refresh=True)

    security_label = verificar_seguridad(password)
    if security_label == 'Muy segura':
        print(colored("Contraseña: Muy segura.", "blue"))
    elif security_label == 'Segura':
        print(colored("Contraseña: Segura.", "green"))
    elif security_label == 'Más o menos segura':
        print(colored("Contraseña: Más o menos segura.", "yellow"))
    else:
        print(colored("Contraseña: No tan fuerte.", "red"))

    reiniciar = input(Fore.CYAN + "¿Deseas generar otra contraseña? (S/N): ")
    if reiniciar.upper() == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        print(colored(pyfiglet.figlet_format("Hasta pronto!"), "blue"))


if __name__ == "__main__":
    main()

# Detener la música al finalizar el programa
pygame.mixer.music.stop()
import time
import requests
from colorama import init, Fore

init(autoreset=True)


def main():
    print(f"{Fore.WHITE}--- Pornire Monitorizare URLWatch ---")

    while True:
        try:
            with open("sites.txt", "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue

                url = parts[0]
                importance = parts[1]
                check_site(url, importance)

            print(f"{Fore.WHITE}\nVerificare completa. Astept 10 secunde...\n")
            time.sleep(10)

        except FileNotFoundError:
            print(f"{Fore.RED}Eroare: Nu gasesc fisierul sites.txt")
            break


def check_site(url, importance):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[REACHABLE] {url} este online.")
        else:
            print_error(url, importance)

    except requests.RequestException:
        print_error(url, importance)


def print_error(url, importance):
    color = Fore.WHITE

    if importance == "INFO":
        color = Fore.BLUE
    elif importance == "WARNING":
        color = Fore.YELLOW
    elif importance == "CRITICAL":
        color = Fore.RED

    print(f"{color}[UNREACHABLE] {url} ({importance})")


if __name__ == "__main__":
    main()

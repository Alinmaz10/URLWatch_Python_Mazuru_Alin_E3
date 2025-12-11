import time
import requests
import argparse
from colorama import init, Fore

init(autoreset=True)


def parse_arguments():
    parser = argparse.ArgumentParser(description='URLWatch Monitoring Tool')
    parser.add_argument('-i', '--interval', type=int, default=5, help='Interval in secunde')
    parser.add_argument('-f', '--filter', type=str, choices=['INFO', 'WARNING', 'CRITICAL'], help='Filtru importanta')
    return parser.parse_args()


def main():
    args = parse_arguments()

    print(f"{Fore.WHITE}--- Pornire URLWatch ---")
    print(f"{Fore.CYAN}Setari: Interval={args.interval}s | Filtru={args.filter if args.filter else 'TOATE'}")

    while True:
        try:
            with open("sites.txt", "r") as file:
                lines = file.readlines()

            active_sites = 0

            for line in lines:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue

                url = parts[0]
                importance = parts[1]

                if args.filter and importance != args.filter:
                    continue

                check_site(url, importance)
                active_sites += 1

            if active_sites == 0:
                print(f"{Fore.MAGENTA}Niciun site gasit pentru filtrul {args.filter}")

            print(f"{Fore.WHITE}\nVerificare completa. Astept {args.interval} secunde...\n")
            time.sleep(args.interval)

        except FileNotFoundError:
            print(f"{Fore.RED}Eroare: Nu gasesc fisierul sites.txt")
            break
        except KeyboardInterrupt:
            print(f"\n{Fore.WHITE}Oprire fortata.")
            break


def check_site(url, importance):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{Fore.GREEN}[REACHABLE] {url} este online.")
        else:
            print_error(url, importance, f"Status: {response.status_code}")

    except requests.RequestException:
        print_error(url, importance, "Eroare Conexiune")


def print_error(url, importance, details):
    color = Fore.WHITE

    if importance == "INFO":
        color = Fore.BLUE
    elif importance == "WARNING":
        color = Fore.YELLOW
    elif importance == "CRITICAL":
        color = Fore.RED

    print(f"{color}[UNREACHABLE] {url} ({importance}) - {details}")


if __name__ == "__main__":
    main()

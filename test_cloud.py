import os
import time
import random
import requests
from dotenv import load_dotenv

load_dotenv()
WRITE_API_KEY = os.getenv('THINGSPEAK_API_KEY')
URL = 'https://api.thingspeak.com/update'

def testowe_wysylanie():
    if not WRITE_API_KEY:
        print("BŁĄD: Brak klucza API w pliku .env!")
        return

    dane_testowe = {
        'api_key': WRITE_API_KEY,
        'uva_raw': round(random.uniform(10, 100), 2),
        'uvb_raw': round(random.uniform(5, 50), 2),
        'time_ms': 64,                          
        'gain': 1
    }

    print(f"Próba wysłania danych: {dane_testowe}")

    try:
        odpowiedz = requests.post(URL, data=dane_testowe, timeout=10)
        
        if odpowiedz.status_code == 200:
            wynik = odpowiedz.text
            if wynik == '0':
                print("[-] Serwer odebrał żądanie, ale odrzucił dane (limit 15 sekund).")
            else:
                print(f"[+] SUKCES! Dane dotarły do ThingSpeak. Numer wpisu: {wynik}")
        else:
            print(f"[!] Błąd serwera. Kod HTTP: {odpowiedz.status_code}")

    except Exception as e:
        print(f"Błąd połączenia: {e}")

if __name__ == "__main__":
    print("--- START TESTU KOMUNIKACJI ---")
    testowe_wysylanie()
    print("--- KONIEC TESTU ---")
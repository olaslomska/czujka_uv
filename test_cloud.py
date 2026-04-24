import os
import time
import random
import requests
from dotenv import load_dotenv


katalog_skryptu = os.path.dirname(os.path.abspath(__file__))
sciezka_env = os.path.join(katalog_skryptu, '.env')

print(f"Lokalizacja env: {sciezka_env}")
print(f"Czy plik widzi env:: {os.path.exists(sciezka_env)}")

load_dotenv(dotenv_path=sciezka_env)

WRITE_API_KEY = os.getenv('THINGSPEAK_API_KEY')
URL = 'https://api.thingspeak.com/update'

def test():
    if not WRITE_API_KEY:
        print("BŁĄD: Brak klucza API w pliku .env!")
        return

    test_data = {
        'api_key': WRITE_API_KEY,
        'field1': round(random.uniform(10, 100), 2), # Symulacja UVA
        'field2': round(random.uniform(5, 50), 2),   # Symulacja UVB
        'field3': 64,                                # Symulacja czasu (ms)
        'field4': 1                                  # Symulacja Gain
    }

    print(f"Próba wysłania danych: {test_data}")

    try:
        odpowiedz = requests.post(URL, data=test_data, timeout=10)
        if odpowiedz.status_code == 200:
            wynik = odpowiedz.text
            if wynik == '0':
                print("Rządanie odrzucone.")
            else:
                print(f"Numer wpisu: {wynik}")
        else:
            print(f"Błąd serwera. Kod HTTP: {odpowiedz.status_code}")

    except Exception as e:
        print(f"Błąd połączenia: {e}")

if __name__ == "__main__":
    print("start")
    test()
    print("koniec")
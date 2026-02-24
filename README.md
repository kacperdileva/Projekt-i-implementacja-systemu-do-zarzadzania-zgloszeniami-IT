1. Sklonuj repozytorium
git clone https://github.com/TWOJ-LOGIN/Projekt-i-implementacja-systemu-do-zarzadzania-zgloszeniami-IT.git

2. Wejdż do katalogu projektu
cd ".../Projekt i implementacja systemu do zarządzania zgłoszeniami IT"

3. Zainstaluj zalezności Pythona (Django)
pip install -r requirements.txt

4. Zastosuj migracje bazy danych
python3 manage.py migrate lub python manage.py migrate

5. Uruchom serwer deweloperski
python3 manage.py runserver lub python manage.py runserver

6. Otwórz projekt w przeglądarce
http://127.0.0.1:8000/

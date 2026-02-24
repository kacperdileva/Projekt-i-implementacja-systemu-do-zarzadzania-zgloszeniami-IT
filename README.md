# System do zarządzania zgłoszeniami IT

Projekt realizowany przyrostowo w ramach pracy dyplomowej. Aplikacja webowa do obsługi zgłoszeń wsparcia IT, zbudowana w Django.

## Technologie

- **Python** 3.14  
- **Django** 5.3.8 
- **SQLite** 3.51  
- **Bootstrap** 5.3

## Role w systemie

- **Użytkownik końcowy** — Zgłaszanie problemów i zapytań (Prosta obsługa, informacja o statusie zgłoszenia)
- **Pracownik IT** — Obsługa i realizacja zgłoszeń (Zarządzanie zgłoszeniami, priorytety, historia)
- **Administrator systemu** — Konfiguracja i utrzymanie systemu (Zarządzanie użytkownikami, bezpieczeństwo)
- **Kierownik** — Nadzór i analiza (Raporty, statystyki, ocena efektywności)

## Zakres funkcjonalny (WF-01 – WF-07)

| Faza | Opis |
|------|------|
| WF-01 | Rejestracja użytkowników (Zakładanie kont użytkowników) |
| WF-02 | Logowanie (Uwierzytelnianie użytkowników) |
| WF-03 | Zgłaszanie problemów (Tworzenie zgłoszeń przez użytkowników) |
| WF-04 | Zarządzanie zgłoszeniami (Edycja statusów i priorytetów) |
| WF-05 | Historia zmian zgłoszeń (Rejestr zmian i działań) |
| WF-06 | Zarządzanie rolami (Definiowanie uprawnień) |
| WF-07 | Raporty i statystyki (Generowanie zestawień) |

---

## Konfiguracja i uruchomienie projektu

### Wymagania

- Python 3.14
- pip
- Git

### 1. Sklonowanie repozytorium

W terminalu, w katalogu, w którym chcesz umieścić projekt:

git clone https://github.com/TWOJ-LOGIN/Projekt-i-implementacja-systemu-do-zarzadzania-zgloszeniami-IT.git

### 2. Wejście do katalogu projektu
cd ".../Projekt-i-implementacja-systemu-do-zarzadzania-zgloszeniami-IT"

### 3. Instalacja zależności (Django)
pip install -r requirements.txt

### 4.Migracje bazy danych
python manage.py migrate (Windows) / python3 manage.py migrate (MacOS)

### 5. Uruchomienie serwera deweloperskiego
python manage.py runserver (Windows) / python3 manage.py runserver (MacOS)

### 6. Otwarcie aplikacji w przeglądarce
Wejdź na adres:
http://127.0.0.1:8000/

Aby zatrzymać serwer, naciśnij w terminalu Ctrl+C

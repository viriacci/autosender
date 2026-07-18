# 📩 Message Scheduler

Desktopowa aplikacja do planowania i automatycznego wysyłania wiadomości o określonej godzinie.

Program posiada nowoczesny interfejs w stylu **Windows 11 Fluent Design** (ciemny motyw) i pozwala przygotować wiadomość, ustawić czas wysyłki, a następnie automatycznie wpisać ją do aktywnego okna komunikatora i wysłać klawiszem **Enter**.

---

# ✨ Funkcje

## 🖥️ Interfejs

* 🌙 Ciemny motyw (Dark Mode)
* 🎨 UI oparte na CustomTkinter
* 🪟 Styl inspirowany Windows 11 Fluent Design
* 📱 Responsywny układ
* 📋 Lista zaplanowanych wiadomości
* ℹ️ Pasek statusu aplikacji

---

## ⏰ Planowanie wiadomości

* Dodawanie wiadomości z określoną godziną wysyłki
* Automatyczna normalizacja czasu

Obsługiwane formaty:

```
3
```

zamienia na:

```
03:00:00
```

---

```
3:42
```

zamienia na:

```
03:42:00
```

---

```
03:42:15
```

pozostaje:

```
03:42:15
```

Aplikacja zawsze zapisuje czas w formacie:

```
HH:MM:SS
```

---

# 📤 Automatyczne wysyłanie

Po osiągnięciu ustawionej godziny aplikacja:

1. Wykrywa zaplanowaną wiadomość
2. Blokuje ponowne wykonanie tego samego zadania
3. Odczekuje ustawione opóźnienie bezpieczeństwa
4. Wkleja wiadomość przez schowek
5. Wysyła ją klawiszem Enter

---

# 🛡️ Bezpieczeństwo wysyłania

System posiada:

* zabezpieczenie przed wielokrotnym wysłaniem tej samej wiadomości
* możliwość anulowania wysyłania
* bezpieczne używanie schowka
* osobny wątek harmonogramu
* blokadę podczas aktywnej wysyłki

---

# 📝 Edytor wiadomości

Edytor obsługuje:

* wielolinijkowe wiadomości
* zachowanie ręcznych przejść do nowej linii
* poprawne zawijanie tekstu

Długie słowa bez spacji nie są dzielone w środku — zostają przeniesione do następnej linii.

---

# 💾 Zapisywanie danych

Zaplanowane wiadomości są przechowywane w pliku:

```
messages.json
```

Konfiguracja aplikacji znajduje się w:

```
config.json
```

---

# 📂 Struktura projektu

```
Message Scheduler
│
├── main.py
├── ui.py
├── widgets.py
├── scheduler.py
├── sender.py
├── storage.py
├── config.py
│
├── messages.json
├── config.json
├── requirements.txt
├── icon.ico
└── README.md
```

---

# 📦 Instalacja

## 1. Pobierz projekt

Sklonuj repozytorium lub pobierz pliki aplikacji.

---

## 2. Zainstaluj wymagane biblioteki

W terminalu wykonaj:

```bash
pip install -r requirements.txt
```

---

## 3. Uruchom aplikację

```bash
python main.py
```

---

# 📋 Wymagania

* Python 3.10+
* Windows
* Aktywne okno programu docelowego do wysyłania wiadomości

Biblioteki:

```
customtkinter
pyautogui
pyperclip
pillow
```

---

# ⚙️ Konfiguracja

Przykładowy plik `config.json`:

```json
{
    "app": {
        "title": "📩 Message Scheduler",
        "width": 950,
        "height": 700,
        "theme": "Dark",
        "color_theme": "blue"
    },
    "sender": {
        "delay_before_send": 5
    }
}
```

Parametr:

```
delay_before_send
```

określa czas oczekiwania przed wysłaniem wiadomości.

---

# 🧩 Technologie

Projekt wykorzystuje:

* Python
* CustomTkinter
* PyAutoGUI
* PyPerClip
* Pillow
* JSON Storage

---

# 📜 Licencja

Projekt przeznaczony do użytku prywatnego i edukacyjnego.

---

# 👨‍💻 Autor

**PanSzczesniak Development**

# Metin2 Automated Dungeon Testing Script

## ⚠️ OSTRZEŻENIE / WARNING

**POLSKI:**
Ten skrypt jest przeznaczony TYLKO do testowania zabezpieczeń na własnym serwerze Metin2 w kontrolowanych warunkach. Używanie narzędzi automatyzacji może naruszać regulamin gry. Autor nie ponosi odpowiedzialności za niewłaściwe użycie tego skryptu.

**ENGLISH:**
This script is intended ONLY for security testing on your own Metin2 server in controlled conditions. Using automation tools may violate the game's terms of service. The author is not responsible for improper use of this script.

---

## Opis / Description

**POLSKI:**
Skrypt automatyzuje testowanie przechodzenia dungeonów w Metin2 przy użyciu rozpoznawania obrazu (OpenCV) i automatyzacji interakcji (PyAutoGUI). Główne funkcje:

1. **Rozpoznawanie obrazów z gry** - Użycie OpenCV do identyfikacji NPC, przeciwników, wejść do dungeonów
2. **Automatyzacja kliknięć** - PyAutoGUI do poruszania postacią i interakcji
3. **Atakowanie przeciwników** - Symulacja klikania klawiszy umiejętności
4. **Raportowanie wyników** - Informacja o ukończeniu dungeonu i wykrytych problemach zabezpieczeń

**ENGLISH:**
The script automates dungeon traversal testing in Metin2 using image recognition (OpenCV) and interaction automation (PyAutoGUI). Main features:

1. **Game image recognition** - Using OpenCV to identify NPCs, enemies, dungeon entrances
2. **Click automation** - PyAutoGUI for character movement and interactions
3. **Enemy attacks** - Simulating skill key presses
4. **Result reporting** - Information about dungeon completion and detected security issues

---

## Instalacja / Installation

### Wymagania / Requirements
- Python 3.8 or higher
- Windows/Linux/macOS
- Screen resolution: 1920x1080 (recommended)

### Instalacja zależności / Install dependencies

```bash
pip install -r requirements.txt
```

lub / or:

```bash
pip install opencv-python numpy Pillow PyAutoGUI
```

---

## Konfiguracja / Configuration

### 1. Przygotowanie obrazów wzorcowych / Prepare Template Images

Utwórz folder `images/` i dodaj następujące zrzuty ekranu z gry / Create `images/` folder and add the following game screenshots:

- `dungeon_npc.png` - NPC przy wejściu do dungeonu / NPC at dungeon entrance
- `enter_button.png` - Przycisk wejścia / Enter button
- `enemy_indicator.png` - Wskaźnik wroga / Enemy indicator
- `dungeon_complete.png` - Ekran ukończenia / Completion screen
- `exit_portal.png` - Portal wyjściowy / Exit portal

**Jak zrobić zrzuty ekranu / How to take screenshots:**
1. Uruchom grę i przejdź do odpowiedniego miejsca / Start game and go to the location
2. Zrób zrzut ekranu (Print Screen) / Take screenshot (Print Screen)
3. Wytnij tylko potrzebny element / Crop only the needed element
4. Zapisz jako PNG w folderze `images/` / Save as PNG in `images/` folder

### 2. Edycja konfiguracji / Edit Configuration

Edytuj plik `config.json`:

```json
{
  "images_path": "images",
  "confidence": 0.8,
  "delay": 0.5,
  "max_attempts": 3,
  "max_dungeon_time": 300,
  "skill_keys": ["1", "2", "3"]
}
```

**Parametry / Parameters:**
- `images_path` - Ścieżka do folderu z obrazami / Path to images folder
- `confidence` - Pewność rozpoznawania (0.0-1.0) / Recognition confidence (0.0-1.0)
- `delay` - Opóźnienie między akcjami (sekundy) / Delay between actions (seconds)
- `max_attempts` - Max prób wejścia do dungeonu / Max dungeon entry attempts
- `max_dungeon_time` - Max czas w dungeonie (sekundy) / Max dungeon time (seconds)
- `skill_keys` - Klawisze umiejętności / Skill keys

---

## Użycie / Usage

### Podstawowe uruchomienie / Basic Usage

```bash
python dungeon_test.py
```

### Krok po kroku / Step by step:

1. **Przygotuj grę / Prepare game:**
   - Uruchom Metin2
   - Ustaw postać przed wejściem do dungeonu
   - Ustaw okno gry w trybie okienkowym (windowed mode)

2. **Uruchom skrypt / Run script:**
   ```bash
   python dungeon_test.py
   ```

3. **Obserwuj / Monitor:**
   - Skrypt wyświetli ostrzeżenie i odliczanie
   - Następnie automatycznie rozpocznie test
   - Logi są zapisywane do `dungeon_test.log`

4. **Awaryjne zatrzymanie / Emergency stop:**
   - Przesuń mysz do rogu ekranu (fail-safe)
   - lub naciśnij Ctrl+C

---

## Bezpieczeństwo / Security

### Zabezpieczenia wbudowane / Built-in safeguards:

1. **PyAutoGUI Fail-Safe** - Przesuń mysz do rogu ekranu, aby przerwać / Move mouse to corner to abort
2. **Logging** - Wszystkie akcje są zapisywane / All actions are logged
3. **Timeout** - Automatyczne zatrzymanie po określonym czasie / Auto-stop after time limit

### Dobre praktyki / Best practices:

- ✅ Używaj tylko na własnym serwerze testowym / Use only on your own test server
- ✅ Przeprowadzaj testy w kontrolowanych warunkach / Conduct tests in controlled conditions
- ✅ Nie zostawiaj skryptu bez nadzoru / Don't leave script unattended
- ❌ Nie używaj na serwerach produkcyjnych / Don't use on production servers
- ❌ Nie udostępniaj skryptu osobom trzecim do nadużyć / Don't share script for abuse

---

## Struktura projektu / Project Structure

```
METIN2/
├── dungeon_test.py      # Główny skrypt / Main script
├── config.json          # Konfiguracja / Configuration
├── requirements.txt     # Zależności Python / Python dependencies
├── README.md           # Ten plik / This file
├── images/             # Folder na obrazy wzorcowe / Template images folder
│   ├── dungeon_npc.png
│   ├── enter_button.png
│   ├── enemy_indicator.png
│   ├── dungeon_complete.png
│   └── exit_portal.png
└── dungeon_test.log    # Plik z logami (tworzony automatycznie) / Log file (auto-created)
```

---

## Rozwiązywanie problemów / Troubleshooting

### Problem: Skrypt nie znajduje obrazów / Script can't find images

**Rozwiązanie / Solution:**
1. Upewnij się, że obrazy są w formacie PNG / Ensure images are in PNG format
2. Sprawdź ścieżkę w `config.json` / Check path in `config.json`
3. Zmniejsz parametr `confidence` (np. do 0.7) / Lower `confidence` parameter (e.g., to 0.7)

### Problem: Skrypt działa zbyt szybko/wolno / Script is too fast/slow

**Rozwiązanie / Solution:**
- Dostosuj parametr `delay` w `config.json` / Adjust `delay` parameter in `config.json`
- Zwiększ dla wolniejszego działania / Increase for slower operation
- Zmniejsz dla szybszego działania / Decrease for faster operation

### Problem: Fail-safe nie działa / Fail-safe not working

**Rozwiązanie / Solution:**
- Upewnij się, że PyAutoGUI jest poprawnie zainstalowany / Ensure PyAutoGUI is properly installed
- Przesuń mysz do lewego górnego rogu (0,0) / Move mouse to top-left corner (0,0)
- Użyj Ctrl+C jako alternatywy / Use Ctrl+C as alternative

---

## Raportowanie / Reporting

Skrypt generuje raport zawierający / Script generates report containing:

- ✓ Czas trwania testu / Test duration
- ✓ Status ukończenia dungeonu / Dungeon completion status  
- ✓ Wykryte problemy zabezpieczeń / Detected security issues
- ✓ Szczegółowe logi w pliku / Detailed logs in file

Przykładowy raport / Example report:
```
============================================================
Test Report
============================================================
Test Duration: 127.34 seconds
Dungeon Completed: True
No security issues detected
============================================================
```

---

## Licencja / License

Ten skrypt jest udostępniany w celach edukacyjnych i testowych. Używaj na własną odpowiedzialność.

This script is provided for educational and testing purposes. Use at your own risk.

---

## Autor / Author

Created for Metin2 security testing purposes.

**Contact:** Use GitHub Issues for questions and bug reports.

---

## Changelog

### v1.0.0 (2026-02-03)
- Initial release
- Image recognition using OpenCV
- Automated interaction using PyAutoGUI
- Dungeon navigation and combat
- Result reporting and logging
- Configuration file support
- Safety features (fail-safe, timeout)

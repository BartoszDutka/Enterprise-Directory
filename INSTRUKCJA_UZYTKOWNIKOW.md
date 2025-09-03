# 📞 Dostęp do Książki Telefonicznej - Instrukcja dla użytkowników

## 🚀 Główny adres aplikacji

### Oficjalny adres (po konfiguracji DNS przez IT):
```
http://igrabka.ksiazka-tel.company.local
```
✅ **Działa automatycznie na wszystkich urządzeniach firmowych**

### Alternatywny adres (zawsze działa):
```
http://192.168.102.174
```
✅ **Backup - użyj jeśli główny adres nie działa**

---

## 🏢 Dla firm - rozwiązania dostępu

### ✅ **Opcja 1: DNS firmowy (zalecane dla 200+ komputerów)**
👨‍💼 **Administrator IT** konfiguruje DNS na serwerze Windows Server:
- **Wszyscy używają**: `http://igrabka.ksiazka-tel.company.local`
- **Działa automatycznie** na wszystkich urządzeniach
- **Instrukcja dla IT**: Zobacz plik `INSTRUKCJA_ADMIN_DNS.md`

### **Opcja 2: Hosts indywidualnie (małe firmy)**
Każdy użytkownik konfiguruje swoje urządzenie:

#### Windows:
1. Uruchom Notatnik jako Administrator
2. Otwórz: `C:\Windows\System32\drivers\etc\hosts`
3. Dodaj linię: `192.168.102.174   igrabka.ksiazka-tel.pl`
4. Zapisz plik

#### Mac/Linux:
```bash
sudo nano /etc/hosts
# Dodaj linię: 192.168.102.174   igrabka.ksiazka-tel.pl
```

#### Telefony/Tablety:
❌ **Skomplikowane**  
✅ **Użyj adresu IP**: `http://192.168.102.174`

### **Opcja 3: Tylko adres IP**
- **Wszyscy używają**: `http://192.168.102.174`
- **Prosto i niezawodne**
- **Stwórz skróty na pulpitach**

---

## 📋 Funkcje aplikacji

Po wejściu na stronę (przez IP lub nazwę):

- **Lista kontaktów** - wyszukiwanie po imieniu, nazwisku, dziale
- **Numery wewnętrzne** - szybkie znajdowanie numerów
- **Filtry** - sortowanie po dziale
- **Logowanie admina** - zarządzanie kontaktami

**Dane logowania administratora:**
- Email: `admin@firma.pl`  
- Hasło: `REDACTED_SECRET`

---

## ❓ Problemy?

1. **Strona nie ładuje się**: Sprawdź czy jesteś w tej samej sieci WiFi
2. **"Nie można połączyć"**: Skontaktuj się z administratorem IT
3. **Strona działa wolno**: Użyj adresu IP zamiast nazwy domenowej

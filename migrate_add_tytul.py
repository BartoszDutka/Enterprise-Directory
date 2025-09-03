#!/usr/bin/env python3
"""
Skrypt migracji - dodanie kolumny 'tytul' do tabeli kontaktów.
"""

import sqlite3
import os
from pathlib import Path

def migrate_database():
    """Dodaje kolumnę 'tytul' do tabeli kontaktów jeśli jeszcze nie istnieje."""
    
    # Ścieżka do bazy danych
    db_path = Path(__file__).parent / "ksiazka_tele.db"
    
    if not db_path.exists():
        print(f"❌ Baza danych nie istnieje: {db_path}")
        return False
    
    try:
        # Połączenie z bazą danych
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Sprawdzenie czy kolumna już istnieje
        cursor.execute("PRAGMA table_info(kontakty)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'tytul' in columns:
            print("✅ Kolumna 'tytul' już istnieje w tabeli kontaktów")
            conn.close()
            return True
        
        # Dodanie kolumny 'tytul'
        print("📝 Dodawanie kolumny 'tytul' do tabeli kontaktów...")
        cursor.execute("ALTER TABLE kontakty ADD COLUMN tytul TEXT")
        
        # Zatwierdzenie zmian
        conn.commit()
        
        # Sprawdzenie czy kolumna została dodana
        cursor.execute("PRAGMA table_info(kontakty)")
        columns_after = [column[1] for column in cursor.fetchall()]
        
        if 'tytul' in columns_after:
            print("✅ Kolumna 'tytul' została pomyślnie dodana")
            
            # Sprawdzenie liczby kontaktów
            cursor.execute("SELECT COUNT(*) FROM kontakty")
            count = cursor.fetchone()[0]
            print(f"📊 Liczba kontaktów w bazie: {count}")
            
            result = True
        else:
            print("❌ Błąd - kolumna 'tytul' nie została dodana")
            result = False
        
        conn.close()
        return result
        
    except sqlite3.Error as e:
        print(f"❌ Błąd bazy danych: {e}")
        return False
    except Exception as e:
        print(f"❌ Nieoczekiwany błąd: {e}")
        return False

def main():
    print("🔄 Rozpoczęcie migracji bazy danych...")
    print("=" * 50)
    
    success = migrate_database()
    
    print("=" * 50)
    if success:
        print("✅ Migracja zakończona pomyślnie!")
        print("🚀 Możesz teraz uruchomić aplikację i używać pola 'Tytuł/Przedrostek'")
    else:
        print("❌ Migracja nie powiodła się!")
        print("🔧 Sprawdź logi błędów i spróbuj ponownie")

if __name__ == "__main__":
    main()

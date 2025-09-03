#!/usr/bin/env python3
"""
Migracja: Dodanie pola is_favorite do tabeli kontakty
"""

import sqlite3
import sys
from datetime import datetime

def migrate_add_favorites():
    """Dodaje kolumnę is_favorite do tabeli kontakty"""
    
    try:
        # Połączenie z bazą danych
        conn = sqlite3.connect('ksiazka_tele.db')
        cursor = conn.cursor()
        
        print("Rozpoczynam migrację: dodawanie pola is_favorite...")
        
        # Sprawdź czy kolumna już istnieje
        cursor.execute("PRAGMA table_info(kontakty);")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        
        if 'is_favorite' in column_names:
            print("Kolumna is_favorite już istnieje - pomijam migrację")
            return True
        
        # Dodaj kolumnę is_favorite
        cursor.execute("""
            ALTER TABLE kontakty 
            ADD COLUMN is_favorite BOOLEAN DEFAULT 0
        """)
        
        print("✓ Dodano kolumnę is_favorite do tabeli kontakty")
        
        # Zatwierdź zmiany
        conn.commit()
        print("✓ Migracja zakończona pomyślnie")
        
        return True
        
    except Exception as e:
        print(f"❌ Błąd podczas migracji: {e}")
        if 'conn' in locals():
            conn.rollback()
        return False
        
    finally:
        if 'conn' in locals():
            conn.close()

def main():
    """Funkcja główna"""
    print(f"Uruchamianie migracji dodawania pola is_favorite - {datetime.now()}")
    print("-" * 60)
    
    success = migrate_add_favorites()
    
    print("-" * 60)
    if success:
        print("Migracja zakończona sukcesem!")
        sys.exit(0)
    else:
        print("Migracja zakończona niepowodzeniem!")
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sqlite3

def check_database():
    conn = sqlite3.connect('ksiazka_tele.db')
    cursor = conn.cursor()
    
    # Sprawdź tabele
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tabele w bazie danych:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Sprawdź strukturę tabeli kontakty
    if ('kontakty',) in tables:
        cursor.execute("PRAGMA table_info(kontakty);")
        columns = cursor.fetchall()
        print("\nStruktura tabeli kontakty:")
        for col in columns:
            print(f"  {col[1]} ({col[2]}) - {'PRIMARY KEY' if col[5] else ''} {'NOT NULL' if col[3] else ''}")
    
    conn.close()

if __name__ == "__main__":
    check_database()

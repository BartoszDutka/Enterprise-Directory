import sqlite3

# Sprawdzenie struktury bazy danych
conn = sqlite3.connect('ksiazka_tele.db')
cursor = conn.cursor()

# Lista tabel
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tabele w bazie danych:")
for table in tables:
    print(f"  - {table[0]}")

# Sprawdzenie struktury tabeli kontaktów
if tables:
    table_name = tables[0][0]  # Pierwsza tabela
    print(f"\nKolumny w tabeli '{table_name}':")
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  - {column[1]} ({column[2]})")

conn.close()

import sqlite3

connection = sqlite3.connect("sqlite_test_1.db")

# Ein Cursor wird erstellt, um mit der Datenbank zu interagieren
cursor = connection.cursor()

# Eine Tabelle mit dem Namen "Bevoelkerung" wird erstellt
# create_table_sql = """
# CREATE TABLE Bevoelkerung(
#     Stadt TEXT,
#     Eigenschaft_1 REAL,
#     Eigenschaft_2 REAL,
#     Eigenschaft_3 REAL
# )
# """
#cursor.execute(create_table_sql)


# Daten werden in die Tabelle eingefügt
insert_data_sql = "INSERT INTO Bevoelkerung VALUES \
    ('Frankfurt', 30001, 4, 5), \
    ('Frankfurt', 30002, 6, 7.9), \
    ('Frankfurt', 30003, 8, 9), \
    ('Kassel', 20001, 8, 1), \
    ('Kassel', 20002, 2, 3), \
    ('Berlin', 1111, 7, 9), \
    ('Dortmund', 53130, 2, 17)"

for datensatz in insert_data_sql.split('),('):
    stadt, eigenschaft_1, eigenschaft_2, eigenschaft_3 = eval(datensatz.strip())
    
    # Überprüfen, ob ein Datensatz mit den gleichen Werten bereits vorhanden ist
    select_sql = "SELECT * FROM Bevoelkerung WHERE Stadt=? AND Eigenschaft_1=? AND Eigenschaft_2=? AND Eigenschaft_3=?"
    cursor.execute(select_sql, (stadt, eigenschaft_1, eigenschaft_2, eigenschaft_3))
    vorhanden = cursor.fetchone()
    
    # Wenn kein entsprechender Datensatz gefunden wurde, füge den Datensatz ein
    if not vorhanden:
        insert_sql = "INSERT INTO Bevoelkerung VALUES (?, ?, ?, ?)"
        cursor.execute(insert_sql, (stadt, eigenschaft_1, eigenschaft_2, eigenschaft_3))
        
# Die Änderungen werden in der Datenbank gespeichert
connection.commit()

# Die Verbindung zur Datenbank wird geschlossen
connection.close()


connection = sqlite3.connect("sqlite_test_1.db")
cursor = connection.cursor()

# Eine SELECT-Abfrage, um alle Datensätze aus der Tabelle abzurufen
select_data_sql = "SELECT * FROM Bevoelkerung"
cursor.execute(select_data_sql)

# Alle abgerufenen Datensätze werden in einer Liste gespeichert
results = cursor.fetchall()

# Die Liste wird durchlaufen und jeder Datensatz wird angezeigt
for row in results:
    print(row)

connection.close()
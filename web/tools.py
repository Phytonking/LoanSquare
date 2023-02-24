import sqlite3

def sqlToCsv(dbPath, table, filename):
    connection = sqlite3.connect(dbPath)
    cursor = connection.execute('select * from '+table)
    names = list(map(lambda x: x[0], cursor.description))
    csv = ','.join(names) +"\n"
    table = cursor.fetchall()
    for r in table:
        row = ""
        for e in r:
            row += str(e) + ','
        row = row[:-1] + "\n"
        csv+=row

    try:
        file = open(filename, "x")
    except:
        file = open(filename, "w")
    file.write(csv)
    file.close()
    return csv




csv = sqlToCsv("db.sqlite3", "auth_user", "auth_user.csv")
print(csv)

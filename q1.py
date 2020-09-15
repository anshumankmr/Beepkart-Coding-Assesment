import json
import sqlite3
connection  = sqlite3.connect('q1.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employee
       (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        salary INTEGER NOT NULL
        )
        ''')
connection.commit()
with open('q1.json') as f:
    d = json.load(f)
    for i in d:
        # print(i)
        cmd = "INSERT INTO employee('id','name', 'age', 'salary' ) VALUES (  " + str(i["id"]) + " , '" + str(i["name"]) + "' , " + str(i["age"]) + " , " + str(i["salary"]) + " )" 
        # print(cmd)
        try:
            c.execute(cmd)
        except Exception as e:
            print(cmd)
            print(e)
    connection.commit()
for row in c.execute("Select * from employee"):
    print(row)
connection.close()
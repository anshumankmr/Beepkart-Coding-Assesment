import json
import sqlite3
connection  = sqlite3.connect('q13.db')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employee
       (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        salary INTEGER NOT NULL
        )
        ''')#ID must be unique as well as the name, assuming other employees may have same age and/or salary
connection.commit()
with open('q13.json') as f:
    d = json.load(f)
    for i in d:
        cmd = "INSERT INTO employee('id','name', 'age', 'salary' ) VALUES (  " + str(i["id"]) + " , '" + str(i["name"]) + "' , " + str(i["age"]) + " , " + str(i["salary"]) + " )" 
        #since there is a unique constraint on name and id , it will fail if any of those are the same as a record from before
        try:
            c.execute(cmd)
        except Exception as e:
            print(cmd)
            print(e)
    connection.commit()
for row in c.execute("Select * from employee"):
    print(row)
connection.close()
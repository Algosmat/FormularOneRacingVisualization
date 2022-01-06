
import csv, sqlite3
conn = sqlite3.connect('F1ResultsDB')
curs = conn.cursor()
#curs.execute("DROP TABLE CIRCUITS")

#curs.execute("DROP TABLE RACES")

#curs.execute("DROP TABLE CONSTRUCTORS")
#curs.execute("DROP TABLE CONSTRUCTOR_RESULTS")
#curs.execute("DROP TABLE CONSTRUCTOR_STANDINGS")
#curs.execute("DROP TABLE RESULTS")
#curs.execute("DROP TABLE CIRCUITS")


curs.execute("CREATE TABLE CIRCUITS (circuitId INTEGER PRIMARY KEY, circuitRef TEXT, name TEXT, location TEXT,country TEXT,lat REAL, lng REAL,alt REAL,url TEXT);")
curs.execute("CREATE TABLE RACES (raceId INTEGER PRIMARY KEY, year INT, round TEXT, circuitId INTEGER,name TEXT,date TEXT,time TEXT, url TEXT,FOREIGN KEY(circuitId) REFERENCES CIRCUITS(circuitId));")
curs.execute("CREATE TABLE CONSTRUCTORS (constructorId INTEGER PRIMARY KEY, constructorRef TEXT, name TEXT, nationality TEXT,url TEXT);")
curs.execute("CREATE TABLE CONSTRUCTOR_RESULTS (constructorResultsId INTEGER PRIMARY KEY, raceId INTEGER, constructorId INTEGER, points REAL,status TEXT,FOREIGN KEY(constructorId) REFERENCES CONSTRUCTORS(circuitId),FOREIGN KEY(raceId) REFERENCES RACES(raceId));")
curs.execute("CREATE TABLE CONSTRUCTOR_STANDINGS (constructorStandingsId INTEGER PRIMARY KEY, raceId INTEGER, constructorId INTEGER, points REAL,position INTEGER,positionText TEXT, wins REAL,FOREIGN KEY(raceId) REFERENCES RACES(raceId),FOREIGN KEY(constructorId) REFERENCES CONSTRUCTORS(constructorId));")
curs.execute("CREATE TABLE RESULTS (resultId INTEGER PRIMARY KEY, raceId INTEGER, driverId INTEGER, constructorId INTEGER,number REAL,grid TEXT, position REAL,positionText TEXT,positionOrder TEXT, points REAL, laps TEXT,time TEXT, milliseconds TEXT,fastestLap REAL,rank REAL,fastestLapTime REAL,fastestLapSpeed REAL,statusId REAL);")
#curs.execute("CREATE TABLE CIRCUITS (circuitId INTEGER PRIMARY KEY, circuitRef TEXT, name TEXT, location TEXT,country TEXT,lat REAL, lng REAL,alt REAL,url TEXT);")

reader1 = csv.reader(open('dataset/circuits.csv', 'r'), delimiter=',')
reader2 = csv.reader(open('dataset/races.csv', 'r'), delimiter=',')
reader3 = csv.reader(open('dataset/constructors.csv', 'r'), delimiter=',')
reader4 = csv.reader(open('dataset/constructor_results.csv', 'r'), delimiter=',')
reader5 = csv.reader(open('dataset/constructor_standings.csv', 'r'), delimiter=',')
reader6 = csv.reader(open('dataset/results.csv', 'r'), delimiter=',')
#reader7 = csv.reader(open('dataset/circuits.csv', 'r'), delimiter=',')

for row in reader1:
    to_db = [row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
    curs.execute("INSERT INTO CIRCUITS (circuitRef, name, location,country,lat,lng,alt,url) VALUES (?, ?, ?,?,?,?,?,?);", to_db)

for row in reader2:
    to_db = [row[0], row[1],row[2],row[3],row[4],row[5],row[6]]
    curs.execute("INSERT INTO RACES (year, round, circuitId,name,date,time,url) VALUES (?, ?, ?,?,?,?,?);", to_db)
for row in reader3:
    to_db = [row[0], row[1],row[2],row[3]]
    curs.execute("INSERT INTO CONSTRUCTORS (constructorRef, name, nationality,url) VALUES (?, ?, ?,?);", to_db)
for row in reader4:
    to_db = [row[0], row[1],row[2],row[3]]
    curs.execute("INSERT INTO CONSTRUCTOR_RESULTS (raceId, constructorId, points,status) VALUES (?, ?, ?,?);", to_db)
for row in reader5:
    to_db = [row[0], row[1],row[2],row[3],row[4],row[5]]
    curs.execute("INSERT INTO CONSTRUCTOR_STANDINGS (raceId, constructorId, points,position,positionText, wins) VALUES (?, ?, ?,?,?,?);", to_db)
for row in reader6:
    to_db = [row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]]
    curs.execute("INSERT INTO RESULTS (raceId, driverId, constructorId,number,grid,position,positionText,positionOrder,points,laps,time,milliseconds,fastestLap,rank,fastestLapTime,fastestLapSpeed,statusId) VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
#for row in reader1:
#    to_db = [row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
#    curs.execute("INSERT INTO CIRCUITS (circuitRef, name, location,country,lat,lng,alt,url) VALUES (?, ?, ?,?,?,?,?,?);", to_db)

#rows = curs.fetchall()
#print(rows)

conn.commit()

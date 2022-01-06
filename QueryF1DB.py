#Importing the neccessary packages

import csv, sqlite3
conn = sqlite3.connect('F1ResultsDB')
curs = conn.cursor()

#Obtaining the required circuits data from the database
curs.execute("SELECT lat FROM CIRCUITS")
countries = curs.fetchall()

#Obtaining all people who participated in races
curs.execute("SELECT date FROM RACES")
seasons_races = curs.fetchall()

#Need to obtain constructors per nationality => Obtaining all nationalities of contructors
curs.execute("SELECT url FROM CONSTRUCTORS")
nationalities_of_constructors = curs.fetchall()

#Points each constructor scored
curs.execute("SELECT status FROM CONSTRUCTOR_RESULTS")
points_scored = curs.fetchall()
#Thier names as well
curs.execute("SELECT nationality FROM CONSTRUCTORS")
constructors_names = curs.fetchall()
#Their ids as well
curs.execute("SELECT points FROM CONSTRUCTOR_RESULTS")
constructorIds = curs.fetchall()

#In how many races does each constructor participate=>How many times their names appear in results

#Trend of fastest lap times
curs.execute("SELECT fastestLapSpeed FROM RESULTS")
fastestLapTime = curs.fetchall()[1:17]



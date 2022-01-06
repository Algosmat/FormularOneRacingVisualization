from QueryF1DB import*
import pandas as pd
import matplotlib.pyplot as plt

#Task 1
countries = [str(country)[2:-3] for country in countries[1:]]
countries = pd.DataFrame(countries)
countries.value_counts().plot(kind='bar',title="Circuits Per Country")
plt.show()

#Task 2
seasons_races=[str(season)[2:-3] for season in seasons_races[1:]]
pd.DataFrame(seasons_races).value_counts().plot(kind='bar',title="Number of Races Per Season")
plt.show()
#Task 3
nationalities_of_constructors = [str(nationality)[2:-3] for nationality in nationalities_of_constructors[1:]]
pd.DataFrame(nationalities_of_constructors).value_counts().plot(kind='bar',title="Number of constructors based on nationality")
plt.show()
#Task 4
points_per_constructor = {}
points_scored = [float(str(point)[2:-3]) for point in points_scored[1:]]
constructorIds = [int(str((id))[1:-4]) for id in constructorIds[1:]]
for i in range(len(constructorIds)):
    if constructorIds[i] in points_per_constructor:
        points_per_constructor[constructorIds[i]] = points_per_constructor[constructorIds[i]]+points_scored[i]
    else:
        points_per_constructor[constructorIds[i]] = points_scored[i]
plt.bar(list(points_per_constructor.keys()), points_per_constructor.values(), color='g')
plt.show()
constructors_names = [str((name))[2:-3] for name in constructors_names[1:]]
pd.DataFrame(constructors_names).value_counts().plot(kind='bar',title="How Many Races Each Constructor Participated")
plt.show()
fastestLapTime = [float(str(time)[2:-3].split(':')[0])+float(str(time)[2:-3].split(':')[1])/60 for time in fastestLapTime]
plt.hist(fastestLapTime)
plt.title("How Fastest Time Lap Vary Over Years")
plt.show()
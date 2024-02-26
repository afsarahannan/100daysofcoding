import csv

import pandas
import pandas as pd

with open ("weather_data.csv", mode="r") as file:
    data = file.readlines()

lines=[]
for text in data:
    line = text.strip()
    lines.append(line)

print(lines)

temperature = []
with open("weather_data.csv") as file:
    data = csv.reader(file)
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))


weather_data = pd.read_csv("weather_data.csv")
temp_list = weather_data['temp'].to_list()
average_weekly_temp = round(sum(temp_list)/len(temp_list), 2)
print(average_weekly_temp)
print(weather_data['temp'].mean())
print(weather_data['temp'].max())
print(weather_data[weather_data.temp == weather_data.temp.max()])
monday = weather_data[weather_data.day == "Monday"]
mon_temp_F = (9/5 * monday.temp) + 32
print(mon_temp_F)

student_dict = {
    "student" : ['Amy', 'Belal', 'Abel'],
    "scores" : [67, 86, 70]
}
student_dict_df = pandas.DataFrame(student_dict)
student_dict_df.to_csv("student.csv")
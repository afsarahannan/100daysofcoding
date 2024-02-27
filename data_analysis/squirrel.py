import pandas as pd

sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(sq_data.columns)

color = sq_data["Primary Fur Color"].unique()
# print(len(sq_data[sq_data['Primary Fur Color'] == 'Gray']))

color_count = sq_data['Primary Fur Color'].value_counts(dropna=True)

data = {'Fur color': ['grey', 'red', 'black'],
         'Count': [color_count[0], color_count[1], color_count[2]]}

data_df = pd.DataFrame(data)
data_csv = data_df.to_csv('squirrel_count.csv')

# for (index,value) in data_df.iterrows():
#     if value['Fur color'] == 'red':
#         print(value.Count)


data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)
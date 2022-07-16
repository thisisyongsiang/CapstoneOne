import pandas as pd
import json
import CategoryAndFilter as ct

df = pd.read_json("singaporeFnBAll.json")
print(len(df))  # 54753 data points, 494 data points skipped due lack of 'latitude' field
print(df.loc[0, 'name'])    # Spageddies
print(df.loc[54752, 'name']) # Spice Junction


dir="singaporeFnBAll.json"
f=open(dir,encoding='utf-8')
data=json.load(f)
clean_data = ct.simplifyData(data, [1.397427, 103.881539], 1, 2, 3)
print(clean_data[0]['distance'])    # 16931.679249607503
df = pd.DataFrame(clean_data)

df_1 = df[df['distance'] < 1000]
print(len(df_1))    # 175

df_2 = df[df['price'] > 2]
print(len(df_2))    # 1839

df_3 = df.sort_values(['distance'])
print("Top 5 based on Distance")
print(df_3.iloc[:5, [1,7,9,10]])     # Get Top 5

df_4 = df.sort_values(['recommendation'], ascending=False)
print("Top 5 based on Recommendation")
print(df_4.iloc[:5, [1,7,9,10]])     # Get Top 5

df_5 = df.sort_values(['price', 'distance'], ascending=[False, True])
print("Top 5 based on Price")
print(df_5.iloc[:5, [1,7,9,10]])     # Get Top 5

import pandas as pd
data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}
df = pd.DataFrame(data)
powers = {
    'X': [1, 2, 3, 4, 5],  
    'Y': [1, 2, 3, 4, 5], 
    'Z': [1, 2, 3, 4, 5]   
}
for column in df.columns:
    df[column] = df[column] ** powers[column]
print(df)
import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, 4, 5]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
replacement_value = 0 
df.fillna(replacement_value, inplace=True)
print("\nDataFrame after replacing missing values with", replacement_value, ":")
print(df)
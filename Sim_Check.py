pip install pingouin

import pandas as pd
import numpy as np

# Specify the path to your Excel file in Google Drive
Coded1_path = '/content/drive/MyDrive/Food Image Analysis/Analysis/Image/mc_kfc_tweet_image_measure.csv'
Coded2_path = '/content/drive/MyDrive/Food Image Analysis/Analysis/Text/mc_kfc_after_speechAct_coded.xlsx'


# Read the Excel file into a DataFrame
Coded1_df = pd.read_csv(Coded1_path)
Coded2_df = pd.read_excel(Coded2_path)

Data_1 = Coded1_df[['Tweet', 'Assertive_1', 'Expressive_1']]
Data_1.insert(0, 'ID', range(1, 1+len(Data_1)))
Data_1.insert(0, 'Annotator', 1)

Data_2 = Coded2_df[['Tweet', 'Assertive_1', 'Expressive_1']]
Data_2.insert(0, 'ID', range(1, 1+len(Data_2)))
Data_2.insert(0, 'Annotator', 2)

vertical_concat = pd.concat([Data_1, Data_2])

data_assertive = vertical_concat[['Tweet','Assertive_1','Annotator']]

# Calculate the ICC
icc = pg.intraclass_corr(data=data_assertive, targets='Tweet', raters='Annotator', ratings='Assertive_1')

# Print the results
print(icc)



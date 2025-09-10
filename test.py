#testing python
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize

# Specify the path to your Excel file in Google Drive
Combine_path = '/content/drive/MyDrive/Food Image Analysis/Analysis/Image/mc_kfc_tweet_image_measure.csv'


# Read the Excel file into a DataFrame
Image_df = pd.read_csv(Combine_path)

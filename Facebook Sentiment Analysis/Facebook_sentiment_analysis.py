"""
@author: Arpit Somani
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download("vader_lexicon")
file="datafile.xlsx"
xl=pd.ExcelFile(file)   #read from Excel
dfs=xl.parse(xl.sheet_names[0])    #parsing excel sheet to data frame
dfs=list(dfs["Timeline"])  #removes blank rows from data frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
import nltk
import numpy as np
import sklearn
import pandas as pd

df = pd.read_csv('C:\\Users\\AKASH VISHWAKARMA\\Documents\\NLP Dataset\\NLPsample.csv')

print(df['text'])
print(df['text'].values)
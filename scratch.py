import nltk
import numpy as np
import sklearn
import pandas as pd

df = pd.read_csv('C:\\Users\\AKASH VISHWAKARMA\\Documents\\NLP Dataset\\NLPsample.csv')
print(df.columns)
text = df['text'].values
print("first result",text)



split_text = [i.split() for i in text]

print("Second result",split_text)

all_words = [word for sentence in split_text for word in sentence]
print(all_words)



#sklearn.preprocessing.onehotencoding(df)


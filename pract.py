import re

import nltk
from nltk.corpus import stopwords

corpus = "Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5] Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President,[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, Indias highest civilian honour While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours"
print(type(corpus))
print(len(corpus))
sentence = nltk.sent_tokenize(corpus)
print(len(sentence))
print(type(sentence))
#words = nltk.word_tokenize(sentence)

#print(type(words))

#print(len(words))

'''
corpus = "Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5] Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President,[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, Indias highest civilian honour While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours"

#we need to use the stop words removal

#we need to use the regular expression to remove unwanted symbols which will only increase the dimantionality of the corpus

para = nltk.tokenize.sent_tokenize(corpus)
print(para)

for i in para:
    words = nltk.tokenize.word_tokenize(i)
    print(words)

modified_corpus = []
for i in range(len(corpus)):
    modified_corpus.append(re.sub(r'[^a-zA-Z]', ' ', corpus[i]))
print(modified_corpus)





for i in range(len(words)):
    print(i)



import nltk
import re
from nltk.corpus import stopwords

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

corpus = """Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts. He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology. He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974. Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President, he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour. While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83. Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours."""
print(stopwords.words("english"))

# List of stop words
stop_words = set(stopwords.words('english'))

# Function to clean the text by removing unwanted symbols

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text)

# Clean the entire corpus
cleaned_corpus = clean_text(corpus)

# Tokenize the cleaned corpus into sentences
sentences = nltk.tokenize.sent_tokenize(cleaned_corpus)

# Function to tokenize each sentence into words and remove stop words
def tokenize_and_remove_stopwords(sentence):
    words = nltk.tokenize.word_tokenize(sentence)
    words = [word for word in words if word.lower() not in stop_words]
    return words

# Process each sentence
for sentence in sentences:
    cleaned_words = tokenize_and_remove_stopwords(sentence)
    print(cleaned_words)

'''
'''
import nltk
import re

corpus = "Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5] Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President,[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, Indias highest civilian honour While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours"

#we need to use the stop words removal

#we need to use the regular expression to remove unwanted symbols which will only increase the dimantionality of the corpus


para = nltk.tokenize.sent_tokenize(corpus)
#print(para)

for i in para:
    words = nltk.tokenize.word_tokenize(i)
    print(words)
    print(type(words))


#for i in range(len(words)):
#    re.sub(r'[^a-zA-Z]','', words(i))

re.sub(r'[^a-zA-Z]','', words)

'''


import nltk
from nltk.corpus import stopwords
import re

# Download nltk resources if not already present
#nltk.download('punkt')
#nltk.download('stopwords')

corpus = "Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.[5] Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President,[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, Indias highest civilian honour While delivering a lecture at the Indian Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was buried with full state honours"

# Define stopwords list
stop_words = stopwords.words('english')

#for i in corpus:
cleaned = re.sub(r"[^a-zA-Z]"," ","corpus")
print(cleaned)
print(type(cleaned))

# Remove punctuation and special characters using regular expression
pattern = r'[^\w\s]'  # Matches any character that's not a word character or whitespace

para = nltk.sent_tokenize(cleaned)
print(para[1])

#words = [[word for word in nltk.word_tokenize(sentence) if word.lower() not in stop_words] for sentence in sentences]



#words = [nltk.word_tokenize(i) for i in para]
words = [nltk.word_tokenize(sentence) for sentence in para]


print(words)

filtered_words = [[word for word in sentence if word.lower() not in stop_words] for sentence in words]



'''
for i in words:
    words.lower()
[corpus for i in corpus]


# Process the corpus
para = nltk.tokenize.sent_tokenize(corpus)

processed_para = []
for sentence in para:
    words = nltk.tokenize.word_tokenize(sentence)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and re.sub(pattern, '', word)]  # Lowercase, remove stop words, and remove unwanted characters
    processed_para.append(filtered_words)

# Print the processed sentences
for sentence in processed_para:
    print(sentence)
    print(type(sentence))  # Output: <class 'list'>
'''
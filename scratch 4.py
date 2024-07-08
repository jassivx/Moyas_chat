import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Uncomment the following lines if you need to download nltk resources
# nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

corpus = ("Avul Pakir Jainulabdeen Abdul Kalam BR (/ˈɑːbdəl kəˈlɑːm/ ⓘ; 15 October 1931 – 27 July 2015) was an Indian "
          "aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007. Born and "
          "raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering. He spent "
          "the next four decades as a scientist and science administrator, mainly at the Defence Research and Development "
          "Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian "
          "space programme and military missile development efforts.[1] He thus came to be known as the Missile Man of India "
          "for his work on the development of ballistic missile and launch vehicle technology.[2][3][4] He also played a pivotal "
          "organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original "
          "nuclear test by India in 1974.[5] Kalam was elected as the 11th president of India in 2002 with the support of both the "
          "ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the People's President,[6] "
          "he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several "
          "prestigious awards, including the Bharat Ratna, India's highest civilian honour. While delivering a lecture at the Indian "
          "Institute of Management Shillong, Kalam collapsed and died from an apparent cardiac arrest on 27 July 2015, aged 83.[7] "
          "Thousands, including national-level dignitaries, attended the funeral ceremony held in his hometown of Rameswaram, where he was "
          "buried with full state honours.")

# Define stopwords list
stop_words = stopwords.words('english')

# Remove punctuation and special characters using regular expression
cleaned = re.sub(r"[^a-zA-Z\s]", " ", corpus)

# Ensure cleaned is a string
print(f"Cleaned type: {type(cleaned)}")

# Sentence tokenization
sentences = nltk.sent_tokenize(cleaned)

# Ensure sentences is a list of strings
print(f"Sentences type: {type(sentences)}")
print(f"First sentence: {sentences[0]}")

# Word tokenization and removal of stopwords
words = []
for sentence in sentences:
    word_list = nltk.word_tokenize(sentence)
    filtered_words = []
    for word in word_list:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    words.append(filtered_words)

print(words)

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize words
lemmatized_words = []
for sentence in words:
    lemmatized_sentence = []
    for word in sentence:
        lemmatized_sentence.append(lemmatizer.lemmatize(word))
    lemmatized_words.append(lemmatized_sentence)

print(lemmatized_words)

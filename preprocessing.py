from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os, nltk, unicodedata, string, re
'''
    Normalizing the text...
    1. Removed non ascii characters...
    2. Removed punctuations...
    3. Poter stemmer...
    4. Removed stop words...
    5. Coverted every character into lower case...
    
    Normalization can be improved by adding these functionality...
    1. Convert numbers into words.
    2. Add meaning to punctuations.
'''

def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def remove_punctuations(file):
    new_words = []
    for word in file:
        word = word.translate(str.maketrans('','',string.punctuation))
        if word != '':
            new_words.append(word)
            
    return new_words

def stemming(file):
    ps = PorterStemmer()
    new_words = []
    for word in file:
        new_words.append(ps.stem(word))
    return new_words

def lemmitization(file):
    lemmatizer = WordNetLemmatizer()
    new_words = []
    for word in file:
        new_words.append(lemmatizer.lemmatize(word))
    return new_words

def convert_number_to_words(file):
    print(file)
    new_words = []
    for word in file:
        if word.isnumeric():
            new_words.append(num2words(word))
        else:
            new_words.append(word)
    
    return new_words

def normalize(file):
    file = nltk.word_tokenize(file)
    
    #remove non ascii characters
    file = remove_non_ascii(file)
    
    #remove stopwords
    stopword = nltk.corpus.stopwords.words('english')
    file = [word for word in file if not word in stopword]
    
    #convert characters into lower case
    file = [word.lower() for word in file]
    
    #remove punctuation from file
    file = remove_punctuations(file)
    
    #apply lemmatization
    file = lemmitization(file)

    file = convert_number_to_words(file)
    return file
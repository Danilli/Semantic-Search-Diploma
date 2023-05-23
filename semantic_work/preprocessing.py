import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from textblob import TextBlob


def tokenization(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens]
    return tokens


def lemmatisation(tokens):
    lemma = WordNetLemmatizer()
    tokens = [lemma.lemmatize(token) for token in tokens]
    return tokens


def stop_words_filter(tokens):
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens


def stemming(tokens):
    ps = PorterStemmer()
    tokens = [ps.stem(token) for token in tokens]
    return tokens


def spell_correction(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return corrected_text


def prepare_text(pure_text):
    correct_text = spell_correction(pure_text)
    tokens = tokenization(str(correct_text))
    tokens = stop_words_filter(tokens)
    tokens = lemmatisation(tokens)
    tokens = stemming(tokens)
    return tokens


from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
import preprocessing


def word2vec(corpus) -> Word2Vec:
    processed_corpus = [preprocessing.prepare_text(text) for text in corpus]
    model = Word2Vec(processed_corpus, window=5, min_count=1, workers=4)

    # Get the most similar words to a given word
    return model


def tf_idf(corpus) -> TfidfVectorizer:
    # Create a TF-IDF vectorizer object
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
    # Fit the vectorizer on the corpus and transform the corpus
    vectorizer.fit(corpus)

    # transform the documents into a matrix of TF-IDF features
    tfidf_matrix = vectorizer.transform(corpus)
    # get the vocabulary (a set of unique terms)
    features = vectorizer.get_feature_names_out()

    return vectorizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import gensim
from gensim import corpora, models
import preprocessing
import scipy.sparse.sparsetools as sc

# # corpuse for a bit experiments with code
# documents = ['Human machine interface for lab abc computer applications',
#                  'A survey of user opinion of computer system response time',
#                  'The EPS user interface management system',
#                  'System and human system engineering testing of EPS',
#                  'Relation of user perceived response time to error measurement',
#                  'The generation of random binary unordered trees',
#                  'The intersection graph of paths in trees',
#                  'Graph minors A survey']


def nmf_document(doc, n_components=5):
    # Vectorize the document using tf-idf
    vectorizer = TfidfVectorizer(stop_words='english')
    doc_vec = vectorizer.fit_transform([doc])

    # Perform NMF on the document-term matrix
    nmf_model = NMF(n_components=n_components)
    W = nmf_model.fit_transform(doc_vec)
    H = nmf_model.components_

    # Get the top n_components topics and their associated words
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_topics = []
    for topic_idx, topic in enumerate(H):
        top_words_idx = topic.argsort()[:-n_components - 1:-1]
        top_words = feature_names[top_words_idx]
        top_topics.append({'topic': topic_idx, 'words': top_words})

    # Return the topics and their associated coefficients
    topic_coef = list(W[0])
    main_coef = topic_coef.index(max(topic_coef)) + 1
    for topics in top_topics:
        if topics["topic"] == main_coef:
            return topics["words"]

    return top_topics[0]["words"]


def lsa_doc(document:str) -> list:
    # Infer topics for new document
    lsa_model = models.LsiModel.load("helpers_files\\lsa_model")
    dictionary = corpora.Dictionary.load("helpers_files\\lsa_dict")
    new_vec = dictionary.doc2bow(preprocessing.prepare_text(document))
    new_topic_distribution = np.array(lsa_model[new_vec])  # Extract topic distribution, ignoring document ID
    # Multiply by the LSI model's projection matrix to get the final topic distribution
    projection = lsa_model.projection.u
    final_distribution = sc.csc_matvec(projection, new_topic_distribution.T)
    return final_distribution


def train_lsa_model(corpus):

    # Tokenization and preprocessing of documents
    tokenized_docs = [preprocessing.prepare_text(doc) for doc in corpus]

    # Create a dictionary and corpus
    dictionary = corpora.Dictionary(tokenized_docs)
    dictionary.save("helpers_files\\lsa_dict")
    corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

    # Build the LSA model
    lsa_model = models.LsiModel(corpus, id2word=dictionary)
    lsa_model.save("helpers_files\\lsa_model")

    return lsa_model


def train_lda_model(train_corpus) -> gensim.models.ldamodel.LdaModel:

    # preprocessing
    texts = [preprocessing.prepare_text(document) for document in train_corpus]
    # dictionary and corpus
    dictionary = corpora.Dictionary(texts)
    dictionary.save('helpers_files\\lda_dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    # apply lda model
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=len(corpus))
    lda_model.save("helpers_files\\lda_model")
    return lda_model


def lda_to_doc(document: str) -> list:
    # Convert document to list of tokens
    tokens = preprocessing.prepare_text(document)
    lda_model = gensim.models.ldamodel.LdaModel.load("helpers_files\\lda_model")
    # Create empty lists to store the word topic distributions and the assigned topics
    word_distribs = []
    assigned_topics = []

    # Replace NaN values with zeroes
    for word, dist in word_distribs:
        if len(set(dist)) > lda_model.num_topics:
            raise ValueError("Topic distribution has more than {} entries".format(lda_model.num_topics))
        else:
            assert len(set(dist)) == lda_model.num_topics, "Length of topic distribution must match num_topics"
            for key in sorted(dist):
                dist[key] = abs(dist[key]) if dist[key] != 0 else 0

    # Return a list of tuples consisting of words and their assigned topics
    for word, distrib in word_distribs:
        assigned_topics.append((word, distrib))

    return assigned_topics


def init_topic_modeling(corpuse: []):
    train_lda_model(corpuse)
    train_lsa_model(corpuse)


# the topic modeling of other algorithms are working, but I can't take from them a structured answer for current doc
def get_topics_of_doc(document: str):
    # lsa_top = lsa_doc(document)
    # lda_top = lda_to_doc(document)
    nmf_top = list(nmf_document(document))
    # topics = set(lsa_top + lda_top + nmf_top)
    # return topics
    return nmf_top

import nltk
import math
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TextSimilarity:
    def __init__(self, statements):
        self.statements = statements

    def TF(self, sentence):
        words = nltk.word_tokenize(sentence.lower())
        freq = nltk.FreqDist(words)
        dictionary = {}
        for key in freq.keys():
            norm = freq[key] / float(len(words))
            dictionary[key] = norm
        return dictionary

    def IDF(self):
        def idf(TotalNumberOfDocuments, NumberofDocumentsWithThisWord):
            return 1.0 + math.log(TotalNumberOfDocuments/NumberOfDocumentsWithThisWord)

        numDocuments = len(self.statements)
        uniqueWords = {}
        idfValues = {}
        for sentence in self.statements:
            for word in nltk.word_tokenize(sentence.lower()):
                if word not in uniqueWords:
                    uniqueWords[word] = 1
                else:
                    uniqueWords[word] += 1
        for word in uniqueWords:
            idfValues[word] = idf(numDocuments, uniqueWords[word])
        return idfValues

    def TF_IDF(self, query):
        words = nltk.word_tokenize(query.lower())
        idf = self.IDF()
        vectors = {}
        for sentence in self.statements:
            tf = self.TF(sentence)
            for word in words:
                tfv = tf[words] if word in tf else 0.0
                idfv = idf[word] if word in idf else 0.0
                mul = tfv * idfv
                if word not in vectors:
                    vectors[word] = []
                vectors[word].append(mul)
        return vectors

    def displayVectors(self, vectors):
        print(self.statemetns, '\n')
        for word in vectors:
            print("{} -> {}".format(word, np.round(vectors[word],3)))

statements = [
            'ruled india',
            'Chalukyas ruled Badami',
            'So many kingdoms ruled India',
            'Lalbagh is a botanical garden in India'
        ]

TextSimilarity.displayVectors(statements)
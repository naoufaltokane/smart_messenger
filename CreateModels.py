from gensim import corpora, models, similarities
from EAR import Processing as process
import csv



class GenSimModel:

    def __init__(self, path):
        ''' This function creates a GenSim corpus and dictionary based on the
        texts kept in the keyword-texts file. '''
        # Get documents out of mycorpus.txt file
        #with open(path, mode='r') as myfile:
         #   self.documents = myfile.read()
        self.documents = []
        with open(path, 'r') as csvfile:
            emails = csv.reader(csvfile)
            next(emails)
            for row in emails:
                email = row[0]
                parsed = process.getTokens(email)
                self.documents.append(parsed)

        print("documents are :")
        print(self.documents)


        self.dictionary = corpora.Dictionary(self.documents)
        print(self.dictionary)
        print("-----------------------------")
        for i in range(len(self.dictionary)):
            print(i, self.dictionary[i])


        #create bag of words: frequence of each terms
        self.corpus = [self.dictionary.doc2bow(doc) for doc in self.documents]
        print("corpus is")
        print(self.corpus)

        self.dictionary.compactify()

        # Create TF-IDF
        print ("Creating GenSim TF-IDF Model and Index")
        self.tfidfModel = models.TfidfModel(self.corpus)
        tempCorpus = self.tfidfModel[self.corpus]
        # Create Index
        self.tfidfIndex = similarities.MatrixSimilarity(tempCorpus)
        print("Done creating tfidf model--------------------------------" )


        # Create LDA
        print ("Creating GenSim LDA Model and Index")
        self.ldaModel = models.LdaModel(
            self.corpus, id2word=self.dictionary, num_topics=300, update_every=1, chunksize=2000, passes=5)
        tempCorpus = self.ldaModel[self.corpus]
        # Create Index
        self.ldaIndex = similarities.MatrixSimilarity(tempCorpus)
        print("Done creating lda model ----------------------------------")


    def getCorpus(self):
        return self.corpus

    def getDictionary(self):
        return self.dictionary

    def getTfidf(self):
        return self.tfidfModel

    def getLda(self):
        return self.ldaModel

    def getTfidfIndex(self):
        return self.tfidfIndex

    def getLdaIndex(self):
        return self.ldaIndex

import string
import nltk
import csv
from nltk.tokenize import word_tokenize
from EAR.CreateModels import GenSimModel
import nltk
import contractions
from nltk.stem import WordNetLemmatizer

def getTokens(msg_content):

    ''' Uses the Natural Language Toolkit to turn words into tokens '''

    msg_content = contractions.fix(msg_content)

    stopwords = nltk.corpus.stopwords.words('english')
    addedStopWords = [u'http', 'http', u'https', 'https', u're', 're',
                      u'sent', 'sent', u'to', 'to', u'from', 'from',
                      u'subject', 'subject', 'original',
                      u'original', u'message', 'message', 'i', u'i',
                      '-from', '--from', u'-from', u'--from', '-original',
                      '--original', u'-origina', u'--original']

    punctuations = list(string.punctuation)

    tempTokens = nltk.word_tokenize(msg_content)
    #tempTokens = lemmatize(tempTokens)
    tempTokens = [w.lower() for w in tempTokens if (
            w not in punctuations and len(w) < 50)]
    tempTokens = [w.lower() for w in tempTokens if w not in addedStopWords]
    # print tempTokens
    tokens = [w.lower() for w in tempTokens if w not in stopwords]
    return tokens


def lemmatize(words):
    """Lemmatize words in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word)
        lemmas.append(lemma)
    return lemmas


def corpus():
    with open('emails.csv', 'r+', newline='') as csvfile:
        try:
            emails = csv.reader(csvfile)
            filewriter = csv.writer(csvfile)
            next(emails)

            for row in emails:
                email = row[0]
                parsed = getTokens(email)
                row[2] = parsed
                filewriter.writerow(row)

        except StopIteration:
            print("No rows")
            pass




def getMailsAsList(corpusName):

    dic = []
    with open(corpusName, 'r') as csvfile:
        emails = csv.reader(csvfile)
        next(emails)
        for row in emails:
            mail = row[0].split()
            dic.append(mail)


    saveCorpus = open(corpusName + ".txt", 'w')

    for f in dic:
            tokens = ''.join(map(str, f))
            saveCorpus.write(tokens + '\n')
    return dic



def compare_simil_tfidf(query, corpus):
    gs = GenSimModel(corpus)

    quer = [w.lower() for w in word_tokenize(query)]
    print("query tokens are --------------------------------------------------------")
    print(quer)
    print(type(quer))

    print("--------------------------------------------------------------------------")
    dictionary = gs.getDictionary()
    print("dictionary is")
    print(dictionary)

    for i in range(len(dictionary)):
        print(i, dictionary[i])


    corp = dictionary.doc2bow(quer, allow_update=True, return_missing=False)
    print("query corp is ----------------------")
    print(corp)

    print("tfidf model is -------------")
    tf_idf = gs.getTfidf()
    print(tf_idf)

    query_model = tf_idf[corp]


    index = gs.getTfidfIndex()
    print('query model is ------')
    print(query_model)
    print("the similarities with tfidf are")
    simils = index[query_model]
    print(index[query_model])

    # Format result ------------------------------------------

    sims = sorted(enumerate(simils), key=lambda item: -item[1])
    print('scores in order')
    print(sims)
    print(type(sims))

    x = sims[0]
    y = sims[1]
    score1 = [x[1]]
    score2 = [y[1]]

    print('score1')
    print([x[1]])
    print('score2')
    print([y[1]])

    line_number1 = 1 + x[0]
    line_number2 = 1 + y[0]
    with open(corpus, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        text1 = mycsv[line_number1][1]
        text2 = mycsv[line_number2][1]

    L=[]
    L.append(text1)
    L.append(score1)
    L.append(text2)
    L.append(score2)
    print("most similar in corpus is: " + text1)
    return L



def compare_simil_lda(query, corpus):
    gs = GenSimModel(corpus)
    quer = getTokens(query)
    #quer = [w.lower() for w in word_tokenize(query)]
    print("query tokens are --------------------------------------------------------")
    print(quer)
    print(type(quer))

    print("--------------------------------------------------------------------------")
    dictionary = gs.getDictionary()
    print("dictionary is")
    print(dictionary)

    for i in range(len(dictionary)):
        print(i, dictionary[i])


    corp = dictionary.doc2bow(quer)
    print("query corp is ----------------------")
    print(corp)

    print("lda model is -------------")
    lda = gs.getLda()
    print(lda)

    query_model = lda[corp]


    index = gs.getLdaIndex()
    print('query model is ------')
    print(query_model)
    print("the similarities with lda are")
    print(index[query_model])

import gensim
from gensim import corpora
from gensim.corpora.dictionary import Dictionary
from gensim.models import LsiModel

#подготовка текста
common_texts = df["column"]
dictionary = corpora.Dictionary(common_texts)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in common_texts]
#Количество тем и слов в темах задал заранее
number_of_topics=7
words=10

#создание и обучение модели
lsamodel = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)
#Вывод тем и слов из полученных тем
for index, topic in lsamodel.show_topics(formatted=False, num_words= 30):
    print('Topic: {} \nWords: {}'.format(index, [w[0] for w in topic]))

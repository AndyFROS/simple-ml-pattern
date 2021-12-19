#Latent Dirichlet Allocation (LDA) — популярный алгоритм моделирования тем, реализованный, в том числе, в пакете Gensim.
#Основная задача алгоритмов ТМ состоит в том, чтобы получившиеся #темы были качественными, понятными, самостоятельными и разделенными.

import gensim
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim import corpora

#Подготовка текста
common_texts = df["column_sentences"]
dictionary = gensim.corpora.Dictionary(common_texts)
bow_corpus = [dictionary.doc2bow(doc) for doc in common_texts]


#Создание и обучение модели
lda_model = LdaModel(
    bow_corpus, 
    num_topics = 5, 
    id2word = dictionary,                                    
    passes = 10,)

#Вывел полученные темы со значениями
for index, topic in lda_model.show_topics(formatted=False, num_words= 30):
    print('Topic: {} \nWords: {}'.format(index, [w[0] for w in topic]))

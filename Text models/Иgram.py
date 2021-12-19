#Ниже представленны методы, которые формируют атрибуты с unigram, bigram и trigram. 
#Также есть возможность получения лучшей ngramm в поле с помощью метрики tf-idf в словаре поля, если это необходимо
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=15, max_df=0.95, ngram_range=(1,1))
X = vectorizer.fit_transform(df['clean_sentence'])
vect_unigram = pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names())
vect_unigram.head()

#Биграмм
vectorizer = TfidfVectorizer(min_df=15, max_df=0.95, ngram_range=(1,2))
X = vectorizer.fit_transform(df['clean_sentence'])
vect_begram = pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names())
vect_begram.head()

#Триграмм
vectorizer = TfidfVectorizer(min_df=15, max_df=0.95, ngram_range=(1,3))
X = vectorizer.fit_transform(df['clean_sentence'])
vect_trigram = pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names())
vect_trigram.head()

#Сохранение нграм в виде ноых признаков для датафрейма
df2 = pd.concat([df, vect_unigram, vect_begram, vect_trigram], axis=1)

from sklearn.decomposition import NMF
vectorizer = TfidfVectorizer(max_features=1500, min_df=10)
X = vectorizer.fit_transform(df["column"])
#Получение списка векторизованных слов
words = np.array(vectorizer.get_feature_names())


#Создание и обучение модели
nmf = NMF(n_components=10, solver="mu", init="nndsvda")
W = nmf.fit_transform(X)
H = nmf.components_
#Вывел полученные темы со значениями
for i, topic in enumerate(H):
     print("Topic {}: {}".format(i + 1, ",".join([str(x) for x in words[topic.argsort()[-10:]]])))

from sklearn.feature_extraction.text import TfidfVectorizer
#Объявление векторизатора
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['column'])
tfidf.get_feature_names()[:10]

#С использованием PCA
from sklearn.decomposition import PCA
#Объявление PCA
pca = PCA(n_components=2, svd_solver='full', random_state=0)
#Присваиваю трансформированный список в переменную XP (x pca)
XP = pca.fit_transofrm(X.toarray())

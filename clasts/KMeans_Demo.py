from sklearn.feature_extraction.text import TfidfVectorizer
#Объявление векторизатора
tfidf = TfidfVectorizer()
X2 = tfidf.fit_transform(df['name'])

import numpy as np
from sklearn.decomposition import PCA
#Объявление анализа главных компонентов
pca = PCA(n_components=2, random_state=0)
X = pca.fit_transform(X2.toarray())

#функция визуализации
def viz(X, prediction):
    plt.figure(figsize=(12, 12))
    plt.subplot(224)
    plt.scatter(X[:, 0], X[:, 1], c=prediction)
    plt.title("Unevenly Sized Blobs")
    
    plt.show()
    
    
from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters = 7, max_iter=200,init='k-means++', random_state=69)
kmodel.fit(X)

klabels = kmodel.labels_

from sklearn import metrics
#Метрика Silhouette_score
silhouette_score = metrics.silhouette_score(X, klabels, metric='euclidean')
silhouette_score


#Предоставление меток/назначение кластера каждой точке/тексту
df['KMeans Clus Label'] = klabels2 #Последний столбец вы это номера меток

#Вызвал функцию визуализации
viz(X, klabels)

#Краткий вывод основых слов для каждого клсатера
print("Top terms per cluster:")
order_centroids = kmodel.cluster_centers_.argsort()[:, ::-1]
terms = tfidf.get_feature_names()[3:]
#При помощи цмкла выведу по 10 слов для 7 кластеров
for i in range(7):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
        print()

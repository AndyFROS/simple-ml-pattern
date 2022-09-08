X1 = df[["attrib1", "attrib1", "attrib1"]]

"""
MinMaxScaler
Преобразование характеристик путем масштабирования каждой характеристики в заданном диапазоне. Этот оценщик масштабирует и переводит каждый признак в отдельности таким образом,чтобы он находился в заданном диапазоне на обучающем множестве,например,между нулем и единицей.
"""
from sklearn.preprocessing import MinMaxScaler
#обьявление MinMaxScaler
scaler = MinMaxScaler()
#Преобразование данных
return scaler.fit_transform(X)

"""
PCA
Метод главных компонент — один из основных способов уменьшить размерность данных, потеряв наименьшее количество информации.
"""
from sklearn.decomposition import PCA
#Обьявление метода главных компонент
pca = PCA(n_components=2)
#Применение на данных
return pca.fit_transform(X)

#Функция для визуализации распределения 
def viz(prediction):
    #Размер фигуры
    plt.figure(figsize=(12, 12))
    plt.subplot(224)
    #Вывод изобрадения при помощи scatter
    plt.scatter(X[:, 0], X[:, 1], c=prediction)
    plt.title("Unevenly Sized Blobs")
    #Вывод изображения
    plt.show()


from sklearn.cluster import KMeans
#Настройка параметров
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
#Предсказание
kmpreds = kmeans.predict(X)
#Новый атрибут содержащий кластеризированные метки в набор данных
df1["KMCLUSTS"] = kmpreds


#Применение функции описанной выше
viz(df1["KMCLUSTS"])


"""
Метрики calinski_harabasz_score и davies_bouldin_score, потому что они работают очень быстро и хорошо интерпритируются
calinski_harabasz_score - Оценка определяется как отношение между внутрикластерной дисперсией и межкластерной дисперсией.
davies_bouldin_score - Минимальная оценка равна нулю, а более низкие значения указывают на худшую кластеризацию.
"""
import sklearn
#Использование метрики calinski_harabasz_score
sklearn.metrics.calinski_harabasz_score(X, df1["KMCLUSTS"])
#Использование метрикуи davies_bouldin_score
sklearn.metrics.davies_bouldin_score(X, df1["KMCLUSTS"])

#Вывод среднего количества данных на кластер
df1.groupby(["KMCLUSTS"])["passenger_count"].mean()

#Полулярность кластеров
df1["KMCLUSTS"].value_counts()

"""
Можно посмотреть распределение кластеров по отношению к атрибутам
"""
#Поворот названий, чтобы удобно читалось
plt.xticks(rotation=45)
#Вывод столбчато1 диаграммы, что бы посмотреть распределение
sns.barplot(x=df1["CLUSTERNAME"], y=df1["total_sum"])


"""
Так же можно узнать популярность кластеров
"""
#Поворот названий, чтобы удобно читалось
plt.xticks(rotation=45)
#Вывод столбчато1 диаграммы, что бы посмотреть распределение
sns.barplot(x=df1["CLUSTERNAME"], y=df1["total_sum"].value_counts())
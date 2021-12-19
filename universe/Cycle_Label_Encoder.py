#Кодировщик который перекодирует несколько столбцев в цикле
from sklearn import preprocessing
#Создание кодировщика
le = preprocessing.LabelEncoder()
#Создание списка столбцев, которые будут перекодированы
encoder = ['columns']
for i in encoder:
    #Перекодирование в цикле
    df[i] = le.fit_transform(df[i])

#Перед использованием заменяем все nan на []
df['name'] = df['name'].fillna({i: [] for i in df.index})

#Список элементов по которым будет проходить цикл
elements = ['your elements']

#Функция которая будет вызываться в цикле для преобразования признаков в одномерный список
def to_1D(series):
    return pd.Series([x for _list in series for x in _list])

#Цикл для построение распределени плотности списковых признаков
for i in elements:
    fig, ax = plt.subplots(figsize = (18,4))
    #Использовние вышеупомянутой функции
    ax.bar(to_1D(df[i]).value_counts().index,
        to_1D(df[i]).value_counts().values)
    #Метка частоты распределения
    ax.set_ylabel("Frequency", size = 12)
    ax.set_title(i, size = 14)
    #Для более корректного отображения певерну метки на 90 градусов
    plt.xticks(rotation=90)
    plt.show()

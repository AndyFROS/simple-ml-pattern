#Не категориальные признаки
for i in df.columns:
    if type(df[i].iloc[2]) == np.int64 or type(df[i].iloc[2]) == np.float64:
        sns.displot(df, x=i, kind="kde", fill=True)
#Еще можно исключать какие то типы данных при помощи 
df.select_dtypes(exclude=['object', 'datetime64'])

        
#Категориальные признаки
#Лист с признаками которые не будут учитываться при визуализации
skip = ['skip elements']
for i in df.columns:
    if type(df[i].iloc[2]) == str and i not in skip:
        sns.catplot(x=i, kind='count', palette='ch:25', height=20, aspect=5, data=df)
        plt.xticks(rotation=90)
        plt.show()

        
        
#У не категориальных призноков анализ плотности происходит немного сложнее
#Из за большого количества данных для быстроты выведения графиков можно сократить сгруппированые значения до 50 самых популярных
csr = [[df['name1'].value_counts()[:50].index, df['name1'].value_counts()[:50]],
      [df['name2'].value_counts()[:50].index, df['name2'].value_counts()[:50]]]
#Вывод значений при помощи цикла
for i in csr:
    #Размер фигуры
    plt.figure(figsize=(15,8))
    #Повернул все значения боком, что бы все красиво располагалось
    plt.xticks(rotation=90)
    #Построение и вывод графиков
    sns.barplot(i[0], i[1])

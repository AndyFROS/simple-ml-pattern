#Получение атрибутов, в которых 1 признак занимет более 95% данных
#Количество строк
num_rows = len(df.index)
#Список для атрибутов
low_information_cols = []
#Цикл, который будет проходить по всем атрибутам
for col in df.columns:
    #Получение количества значений
    cnts = df[col].value_counts(dropna=False)
    #Получение процента вхождений самого популярного атрибута
    top_pct = (cnts/num_rows).iloc[0]
    
    if top_pct > 0.95:
        #Добавление информации в список
        low_information_cols.append(col)
        #Вывод информации
        print('{0}: {1:.5f}%'.format(col, top_pct*100))
        print(cnts)
        print()

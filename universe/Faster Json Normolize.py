df = pd.DataFrame()
#Пасринг значений из json в DataFrame (df)
for filename in glob.glob("data/*.json"): #Цикл, который перебирает все файлы
    with open(filename, encoding='utf-8-sig') as json_data:  #Открытие каждого файла по очереди
        data = json.load(json_data)#Загрузка файла и помещение его в переменную data
    #Будет 2 маленьких фрейма данных с разными данными из одного json документа
    df1 = pd.json_normalize(data['mainFeat'], errors='ignore')
    df2 = pd.json_normalize(data['mainFfeat'], record_path=['one', 'two'], meta=[['path',  'id']], errors='ignore')
    #В конце обьединяю все эти файлы в 1 большой DataFrame
    dft = df1.merge(df2, on = ('path.id'))
    df = pd.concat([df, dft.merge(dft, on = ('path.id'), how='left', suffixes=('_first', '_second'))])

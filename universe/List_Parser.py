#Перед использованием заменил nan на []
df['name'] = df['name'].fillna({i: [] for i in df.index})

#Функция которая принимает на вход DataFrame, название колонки и суффикс (То что будет добавлено к названию новых атрибутов), а возвращает DataFrame с новыми атрибутами из списка
def listParse(df, column, suf=''):
    #Значение из колонки
    v = df[column].values
    #Длмнна списков
    l = [len(x) for x in v.tolist()]
    f, u = pd.factorize(np.concatenate(v))
    n, m = len(v), u.size
    i = np.arange(n).repeat(l)
    #Объединение в DataFrame
    dummies = pd.DataFrame(
        np.bincount(i * m + f, minlength=n * m).reshape(n, m),
        df.index, u
    )
    #Возвращает DataFrame без колонки, которая была распаршена
    return df.drop(column, 1).join(dummies, rsuffix=suf)

#Использование
df = listParse(df, 'name', '_postfix')

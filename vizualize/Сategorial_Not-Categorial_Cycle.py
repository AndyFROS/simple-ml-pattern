#Не категориальные признаци
for i in df.columns:
    if type(df[i].iloc[2]) == np.int64 or type(df[i].iloc[2]) == np.float64:
        sns.displot(df, x=i, kind="kde", fill=True)


#Категориальные признаки
#Лист с признаками которые не будут учитываться при визуализации
skip = ['skip elements']
for i in df.columns:
    if type(df[i].iloc[2]) == str and i not in skip:
        sns.catplot(x=i, kind='count', palette='ch:25', height=20, aspect=5, data=df)
        plt.xticks(rotation=90)
        plt.show()

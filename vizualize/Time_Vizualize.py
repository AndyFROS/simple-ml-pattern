import seaborn as sns
import matplotlib.pyplot as plt

#Преобразование колонки datetimeCol в тип datetime (если до этого он был иной)
df['datetimeCol'] = pd.to_datetime(df['datetimeCol'])

#Получение дня недели и часа дня из атрибута datetimeCol
df['dayofweek'] = df['datetimeCol'].map(lambda x: x.weekday())
df['hourofday'] = df['datetimeCol'].map(lambda x: x.hour)plt.figure(figsize=(30, 18))

#Построение диаграммы рассеивания по временным точкам, в данном случае по часу дня 
plt.figure(figsize=(30, 18))
sns.scatterplot(data=df, x="datetimeCol", y="hourofday", hue='targetcol',alpha=0.5, s=10)


#Реиндексация перед использованием pivot_table
df.reset_index(drop=True, inplace=True)


#Визуализация усреднённого количества обращений по дням недели при помощи сводной таблицы
pt = pd.pivot_table(df,index='dayofweek', columns ='targetcol', aggfunc='size')
#получение процентного соотношения
plt.figure(figsize=(12, 8), dpi=72)
ax = sns.heatmap(pt, annot=True, linewidths=0.1, cmap="copper", fmt='g'); #Можно еще использовать YlOrRd в параметре cmap
#Наименование меток
ax.set_title('Effect of on the target variable', fontsize = 15, y=1.05)

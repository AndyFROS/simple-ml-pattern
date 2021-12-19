import matplotlib.pyplot as plt
import seaborn as sns

#ВИзуализация по дням недели
df['dayofweek'] = df["datetime_column"].dt.day_name()

pt = pd.pivot_table(df, index='name', columns='dayofweek', values='datetime_column', aggfunc='count')
#получение процентного соотношения
pt = pt.apply(lambda x: round(x / x.sum() * 100,1), axis=1)
#замена всех нанов на 0
pt = pt.fillna(0)
#Размер графика
plt.figure(figsize=(7, 6))
#Отображение
sns.heatmap(pt, annot=True, linewidths=0.4, cmap="YlOrRd");

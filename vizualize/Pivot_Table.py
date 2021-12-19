df.reset_index(drop=True, inplace=True)
#Данные визуализации сводной таблицы
pt = pd.pivot_table(df, index='Index', columns='columns', aggfunc='size', fill_value=0)
#Преобразование данных в процент
pt = pt.apply(lambda x: round(x / x.sum() * 100,1), axis=1)
#Рендеринг воспроизведения
plt.figure(figsize=(12, 8), dpi=72)
ax = sns.heatmap(pt, annot=True, linewidths=0.1, cmap="copper", fmt='g');
#Названия меток и наименования визуализации
ax.set_title('Effect of on the target variable', fontsize = 15, y=1.05)
ax.set_xlabel('X title', fontsize = 23)
ax.set_ylabel('Y title', fontsize = 23)

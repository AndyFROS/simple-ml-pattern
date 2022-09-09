#ref https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
#Author Selva Prabhakaran

df=df.sort_values(by='date1')
df.reset_index(inplace=True)

#to_datetime метод, который автоматически преобразует дату в првавильный формат
df[["date1", "date2"]] = pd.to_datetime(df[["date1", "date2"]].stack(), format='%Y-%m-%d %H:%M:%S').unstack()
#Создание столбца с уникальными датами, это необходимо для работы модели строящей времянные ряды
df["date1"] = df["date1"].map(lambda x: x.date())
#Удаление дубликатов при помощи drop_duplicates
df = df.drop_duplicates(subset=['date1'])
#Сброс индексов
df.reset_index(drop=True, inplace=True)


df['datecopy']=df['date1']
df.set_index('datecopy', inplace=True)
df.index = pd.to_datetime(df.index)
chi = df[df['cluster']==0]
chi = chi[['predictable_attrib']]
chi=chi.rename(columns={"predictable_attrib": "co2"})

y = chi.asfreq('D')
y.fillna(0, inplace=True)

# 'MS' группирует месячные данные
y = y['co2']

# bfill значит, что нужно использовать значение до заполнения пропущенных значений
y = y.fillna(y.bfill())

y.plot(figsize=(15, 6))
plt.show()

mod = sm.tsa.ARIMA(y,
order=(1, 2, 1),
seasonal_order=(1, 2, 1, 10),
enforce_stationarity=False,
enforce_invertibility=False)
results = mod.fit()
print(results.summary().tables[1])

pred_dynamic = results.get_prediction(start=pd.to_datetime(y.index[0]), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()

# Извлечь прогнозируемые и истинные значения временного ряда
y_forecasted = pred_dynamic.predicted_mean
y_truth = y[y.index[0]:] # Вычислить среднеквадратичную ошибку
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

pred_dynamic = results.get_prediction(start=pd.to_datetime("2023-01-01"), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()
y_forecasted = pred_dynamic.predicted_mean

# Получить прогноз на 1000 шагов вперёд
pred_uc = results.get_forecast(steps=1000)
# Получить интервал прогноза
pred_ci = pred_uc.conf_int()

ax = y.plot(label='observed', figsize=(20, 15))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
pred_ci.iloc[:, 0],
pred_ci.iloc[:, 1], color='y', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Количество заражённых')
ax.set_title('Предсказание заражённых для United States')
plt.legend()
plt.show()

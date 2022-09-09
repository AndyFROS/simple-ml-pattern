import streamlit as st
import pickle
import pandas as pd
import datetime
import itertools
import statsmodels.api as sm
import matplotlib.pyplot as plt

plt.style.use('dark_background')

html_temp = """
<div style="background-color:tomato;padding:15px">
<h1 style="color:white;text-align:center;">Предсказание признаков</h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)
import pickle
# load the model from disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

df = pd.read_csv("need_data.csv", engine="pyarrow")
steps=st.slider("Количество дней для предсказания", 10, 1000, step=5)
selected_cluster=st.selectbox("Выберите 1 из кластеров", (df['class'].unique()))
selected_attribute=st.selectbox("Выберите 1 из атрибутов", ("marks", "time"))



#Создание столбца с уникальными датами, это необходимо для работы модели строящей времянные ряды
df["unqDate"] = df["date"].map(lambda x: x.date())
#Удаление дубликатов при помощи drop_duplicates
df = df.drop_duplicates(subset=['unqDate'])
#Сброс индексов
df.reset_index(drop=True, inplace=True)


# Получить прогноз на 500 шагов вперёд
pred_uc = loaded_model.get_forecast(steps=steps)
# Получить интервал прогноза
pred_ci = pred_uc.conf_int()
#Копия столбца столбца с датой, это нужно для того что бы на осноые этого столбца прописать индексы
df['datecopy']=df['unqDate']
#Установка datecopy в качестве индексов для столбца
df.set_index('datecopy', inplace=True)
#Форматирование индексов в datetime формат
df.index = pd.to_datetime(df.index)
chi = df[df['class']==selected_cluster]
chi = chi[[selected_attribute]]
chi=chi.rename(columns={"marks": "co2"})
y = chi
y = y.asfreq('D')
# 'MS' группирует месячные данные
y = y['co2']
# bfill значит, что нужно использовать значение до заполнения пропущенных значений
y = y.fillna(y.bfill())






fig, ax = plt.subplots()
ax = y.plot(label='observed', figsize=(20, 15))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
pred_ci.iloc[:, 0],
pred_ci.iloc[:, 1], color='y', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Количество заражённых')
ax.set_title('Предсказание заражённых для United States')
plt.legend()
st.pyplot(plt)

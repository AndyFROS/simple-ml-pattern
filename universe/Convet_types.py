#Конвернтация object в list
df["column"] = df["column"].apply(lambda x: x.replace("'", "").strip('][').split(', '))

#Конвернтация object в datetime
df['column']=pd.to_datetime(df['column'])

#Конвернтация object в int
df['column']=df['column'].astype(int, errors='ignore')
#Конвернтация object в int с заменой nan на 0 и при условии ошибки (например если в столбеце будет "ДВА" вместо "2") будет стоять nan, который сразу будет заменен на 0
df['column']=pd.to_numeric(df['column'], errors='coerce').fillna(0)

#np.where
import numpy as np
#Основная идея состоит в том, чтобы использовать функцию np.where() для преобразования всех значений «Y» в True, а все остальное — в False.
df["column"] = np.where(df["column"] == "Y", True, False)

#Изменение типов данных при конвертации из csv в DataFrame
df_2 = pd.read_csv("sales_data_types.csv",
                   dtype={'Customer Number': 'int'},
                   converters={'2016': convert_currency,
                               '2017': convert_currency,
                               'Percent Growth': convert_percent,
                               'Jan Units': lambda x: pd.to_numeric(x, errors='coerce'),
                               'Active': lambda x: np.where(x == "Y", True, False)
                              })

import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine

file = 'csvTest/Data8277.csv'
my_database = create_engine('sqlite:///my_database.db')
chunksize=10000

i = 0
j = 0


for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
    df = df.rename(columns={c: c.strip() for c in df.columns})
    df.index+=j
    df.to_sql('data_use', my_database, if_exists='append')
    j = df.index[-1]+1
    print('| index {}'.format(j))
    
df = pd.read_sql_query('SELECT 5 FROM data_use', my_database)

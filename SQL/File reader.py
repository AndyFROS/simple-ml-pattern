#Если sql файл слишком большой, то его можно выгрузить при помощи консоли (Ниже пример работы MySQL shell)
#\sql
#\connect root@localhost
#create database DataBaseName;
#use BRK
#source C:/Users/User/project/file.sql;



import MySQLdb as mdb  
import datetime, time 

import pandas as pd
import numpy as np

def run_sql_file(filename, connection): 
    start = time.time() 
    
    file = open(filename, 'r') 
    sql = s = " ".join(file.readlines()) 
    print("Start executing: " + filename + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + "\n" + sql) 
    cursor = connection.cursor() 
    cursor.execute(sql)
    cursor.close() 
    connection.commit() 
    end = time.time() 
    print("Time elapsed to run the query:" )
    print(str((end - start)*1000) + ' ms')
    
    
connection = mdb.connect('127.0.0.1', 'root', 'password', 'DataBaseName') 
cursor = connection.cursor()
run_sql_file("file.sql", connection)


#Вывести список имеющихся таблиц в бд (Вместо show tables можно указать show databases и будет показан список баз данных)
connection = mdb.connect('127.0.0.1', 'root', 'password', 'DataBaseName') 
cursor = connection.cursor()
databases = ("show tables")
cursor.execute(databases)
for (databases) in cursor:
     print(databases[0])
    
    
    
#Теперь импорт в pandas
query = "Select * from yourDataTable;"
result_dataFrame = pd.read_sql(query, connection)
connection.close() #Закрывает соединение

result_dataFrame

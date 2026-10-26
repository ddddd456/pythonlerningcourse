import mysql.connector
#1 создать подключение
connection = mysql.connectior.connect(host='localhost',user='root',password='admin',database='academy')
#2создать курсор
cursor = connection.cursor()
#3 объявить команду
cursor.execute('select * from teachers')
#4 достаем данные
rows = cursor.fetchall()
for row in cursor:
    print(row)
#закрываем соединение
cursor.close()

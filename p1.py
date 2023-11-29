import psycopg2
import socket
from threading import Thread

conn = psycopg2.connect(database="DB", user="myLogin", password="databasePass123", host="localhost", port=5432)

cur = conn.cursor()
sock1 = socket.socket()
sock1.bind(('127.0.0.1', 5432))
k=1
sock1.listen(1)
cursor = sock1.accept()
cursor.execute('SELECT num FROM table1')
database = cursor.fetchall()

def function():
    err = 0
    while True:
        a = int(conn.recv(1024))+1
        if a in database:
            msg="В БД обнаружено совпадение. Попробуйте еще раз".encode("utf-8")
            insert_q = """INSERT INTO table1 (log) VALUES 'ошибка 1'"""
            cursor.execute()
        else:
            if a == database[k-1]:
                msg="Число меньше предыдущего на 1".encode("utf-8")
                insert_q = """INSERT INTO table1 (log) VALUES 'ошибка 2'"""
                cursor.execute()
                conn.commit()
            else:
                database.append(a)
                msg = str(a).encode("utf-8")
                insert_q = """INSERT INTO table1 (num) VALUES (%s)"""
                rec = (a)
                cursor.execute(insert_q, rec)
            conn.commit()
            count = cursor.rowcount
        k=k+1
        conn.send(msg)
     
t = Thread(target=function)
t.start()
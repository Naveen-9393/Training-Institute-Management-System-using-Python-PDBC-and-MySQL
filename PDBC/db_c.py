import mysql.connector
def db_con_func():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    database ="_10kcoders_sms",
    password="My@14114141"
)
conn=db_con_func()
curObj=conn.cursor()
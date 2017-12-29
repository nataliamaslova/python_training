# import mysql.connector
import pymysql.cursors

connection = pymysql.connect(host="localhost", database="addressbook", user="root", password="")

try:
    pass
    # cursor = connection.cursor()
    # cursor.execute("select * from group_list")
    # for row in cursor.fetchall():
    #     print(row)
finally:
    connection.close()
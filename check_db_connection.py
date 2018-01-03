import mysql.connector
# import pymysql.cursors

connection = mysql.connector.connect(host="localhost", port="3306", database="addressbook", user="root", password="", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

# connection = pymysql.connect(host="localhost", port="3306", database="addressbook", user="root", password="", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

try:

    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
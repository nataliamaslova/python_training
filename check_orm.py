from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", port="3306", database="addressbook", user="root", password="",
               unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

try:

    l = db.get_contact_list()
    for item in l:
        print(item)

    print(len(l))
finally:
    pass
    # db.destroy()
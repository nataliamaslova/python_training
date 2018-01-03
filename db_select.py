from fixture.db import DbFixture

db = DbFixture(host="localhost", port="3306", database="addressbook", user="root", password="",
               unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

try:

    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)

    print(len(contacts))
finally:
    db.destroy()
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", port="3306", database="addressbook", user="root", password="",
               unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

try:
    group_id = Group(id="228")
    print(group_id)
    l = db.get_contacts_not_in_group(group_id)
    for item in l:
        print(item)

    print(len(l))
finally:
    pass
    # db.destroy()
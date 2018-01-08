import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture():

    def __init__(self, host, port, database, user, password, unix_socket):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.unix_socket = unix_socket

        self.connection = pymysql.connect(host=host, port=port, database=database,
                                          user=user, password=password, unix_socket=unix_socket)
        # clear cache after any query
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
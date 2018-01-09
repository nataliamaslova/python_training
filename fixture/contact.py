from model.contact import Contact
import re
import selenium

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("selected[]")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_group(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("select[name='group']>option[value='%s']" % id).click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("email", contact.email)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[17]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("select[name='to_group']>option[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # click on Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit deletion dialog
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # click on Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit deletion dialog
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def add_contact_to_group_by_ids(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        self.select_group_by_id(group_id)
        # click on "Add to" button
        wd.find_element_by_css_selector("input[value='Add to']").click()
        self.open_contact_page()
        self.contact_cache = None

    def remove_contact_from_group_by_ids(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.open_group(group_id)
        self.select_contact_by_id(contact_id)
        # click on "Add to" button
        wd.find_element_by_css_selector("input[name='remove']").click()
        self.open_contact_page()
        self.contact_cache = None

    def update_first_contact(self, new_contact_data):
        self.update_contact_by_index(0, new_contact_data)

    def update_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # click on Edit button
        xpath_data = "//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img"
        wd.find_element_by_xpath(xpath_data).click()
        # do some updates
        self.fill_contact_form(new_contact_data)
        # click on Update button
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def update_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # click on Edit button
        xpath_data = "//table[@id='maintable']/tbody/tr[" + str(id + 2) + "]/td[8]/a/img"
        wd.find_element_by_xpath(xpath_data).click()
        # do some updates
        self.fill_contact_form(new_contact_data)
        # click on Update button
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            rows = wd.find_elements_by_name("entry")
            for cell in rows:
                id = cell.find_element_by_name("selected[]").get_attribute("value")
                columns = cell.find_elements_by_css_selector("td")
                lastname = columns[1].text
                firstname = columns[2].text
                address = columns[3].text
                emails = columns[4].find_elements_by_css_selector("a")
                all_emails = ''
                if (emails.count != 0):
                    for email in emails:

                        all_emails = all_emails + email.text + '\n'
                all_emails = all_emails[0:-1]
                all_phones = columns[5].text
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, id = id,
                                                  address = address,
                                                  all_phones_from_home_page = all_phones,
                                                  all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
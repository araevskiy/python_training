from sys import maxsize


class Contact:

    def __init__(self, firstname=None, secondname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email=None, email2=None, email3=None, address=None, secondaddress=None, all_phones_from_home_page=None, all_emails_from_home_page=None, id=None):
        self.firstname = firstname
        self.secondname = secondname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.secondaddress = secondaddress

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.secondname, self.email, self.mobilephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

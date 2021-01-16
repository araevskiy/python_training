from model.contact import Contact


testdata = [
    Contact(firstname=random_string("firstname", 15), secondname=random_string("secondname", 15), lastname=random_string("lastname", 15),
            address=random_string("address", 15), secondaddress=random_string("secondaddress", 15),
            email=random_string("1@1.", 10), email2=random_string("2@2.", 15), email3=random_string("email", 20),
            homephone=random_string("+7", 10), mobilephone=random_string("7", 10), workphone=random_string("8", 10), secondaryphone=random_string("7000", 10))
]
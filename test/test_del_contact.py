from model.contact import Contact
from random import randrange





def test_delete_some_contact(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="Aleу", secondname="RY",lastname="gg"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts

#def test_delete_contact2(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Aleу", secondname="RY",lastname="gg"))
#    app.contact.delete_first_contact()
#    old_contacts = app.contact.get_contact_list()
#   app.contact.delete_first_contact()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[0:1] = []
 #   assert old_contacts == new_contacts

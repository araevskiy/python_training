from model.contact import Contact




def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Aleу", secondname="RY"))
    app.contact.delete_first_contact()

def test_delete_contact2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Aleу", secondname="RY"))
    app.contact.delete_first_contact()

from model.contact import Contact



def test_modify_contact(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(firstname="11", secondname="22"))
        app.contact.modify_contact(Contact(firstname="Aleуss56", secondname="RYsss"))

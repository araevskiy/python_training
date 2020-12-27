from model.contact import Contact



def test_modify_contact(app):
        app.contact.modify_contact(Contact(firstname="Aleуss56", secondname="RYsss"))





def test_delete_contact(app2):
    app2.session2.login(usermane="admin", password="secret")
    app2.contact.delete_first_contact()
    app2.session2.logout()
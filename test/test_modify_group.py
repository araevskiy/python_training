from model.group import Group




def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="212121", header="fdfd121212fdd", footer="fdfdd2121dff"))
    app.session.logout()
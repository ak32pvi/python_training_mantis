def test_create_project(app):
    app.session.login("administrator", "administrator")
    app.project.create()
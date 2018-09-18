from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "administrator")
    app.project.delete()
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "administrator")
    if app.project.count() == 0:
        app.project.create(Project(name="New_project_name_PRE"))
    app.project.delete()

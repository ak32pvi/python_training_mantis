from model.project import Project


def test_create_project(app):
    app.session.login("administrator", "administrator")
    app.project.create(Project(name="New_project_name_created"))

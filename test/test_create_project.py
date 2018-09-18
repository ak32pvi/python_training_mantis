from model.project import Project


def test_create_project(app):
    app.session.login("administrator", "administrator")
    old_projects = app.project.count()
    app.project.create(Project(name="New_project_name_created071"))
    new_projects = app.project.count()
    assert len(old_projects) + 1 == len(new_projects)

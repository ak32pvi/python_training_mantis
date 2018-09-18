from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "administrator")
    old_projects = app.project.count()
    if app.project.count() == 0:
        app.project.create(Project(name="New_project_name_PRE"))
    app.project.delete()
    new_projects = app.project.count()
    assert len(old_projects) - 1 == len(new_projects)

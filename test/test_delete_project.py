from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "administrator")
    if app.project.count() == 0:
        app.project.create(Project(name="test_delete"))
    old_projects = app.project.get_project_list()
    app.project.delete()
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects[0:1] = []
    assert old_projects == new_projects

    # old_projects = app.project.count()
    # app.project.delete()
    # new_projects = app.project.count()
    # assert len(old_projects) - 1 == len(new_projects)

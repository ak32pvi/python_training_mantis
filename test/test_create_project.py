from model.project import Project


def test_create_project(app):
    app.session.login("administrator", "administrator")
    old_projects = app.project.get_project_list()
    project = Project(name="name")
    app.project.create()
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects[0:1] = []
    assert old_projects == new_projects

    # old_projects = app.project.count()
    # app.project.create(Project(name="New_project_name_created071"))
    # new_projects = app.project.count()
    # assert len(old_projects) + 1 == len(new_projects)

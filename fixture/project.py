from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_create_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def open_project_create_mode(self):
        wd = self.app.wd
        wd.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td/form/input[2]').click()

    def create(self, project):
        wd = self.app.wd
        self.go_to_create_project()
        self.open_project_create_mode()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector('td.center input').click()

    def choose_first_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('tr.row-1 a').click()

    def submit_project_deletion_twice(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[4]/form/input[3]").click()
        wd.find_element_by_xpath("/html/body/div[2]/form/input[4]").click()

    def delete(self):
        wd = self.app.wd
        self.go_to_create_project()
        self.choose_first_project()
        self.submit_project_deletion_twice()

    def count(self):
        wd = self.app.wd
        self.go_to_create_project()
        return len(wd.find_elements_by_css_selector('tr.row-1 a,.row-2 a'))

    def get_project_list(self):
        wd = self.app.wd
        self.go_to_create_project()
        projects = []
        for element in wd.find_elements_by_css_selector('tr.row-1 a,.row-2 a'):
            text = element.text
            projects.append(Project(name=text))
        return projects











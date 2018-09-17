
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






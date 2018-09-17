#from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_create_project(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_create_page.php")

    def create(self):
        wd = self.app.wd
        self.go_to_create_project()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys("AT47")
        wd.find_element_by_css_selector('td.center input').click()




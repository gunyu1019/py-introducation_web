import json
from puepy import Component, t


@t.component()
class Project(Component):
    props = []

    def initial(self):
        f = open("project.json", mode="r", encoding='utf-8')
        project_info = json.load(f)
        f.close()
        return {
            "current_page": 0,
            "max_page": len(project_info),
            "data": project_info
        }

    def populate(self):
        with t.div(classes=["project"]):
            t.span("진행했던 여러 개인 프로젝트를 소개합니다!", classes=["project-title"])
from puepy import Component, t


@t.component()
class Project(Component):
    props = []

    def populate(self):
        with t.div(classes=["project"]):
            pass
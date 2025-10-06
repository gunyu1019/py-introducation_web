from puepy import Application, Page, Component, t

# noinspection PyUnresolvedReferences
import introduction

application = Application()


@application.page()
class MainPage(Page):
    def populate(self):
        with t.div(classes=["container"]):
            t.introduction()
        return


application.mount("#app")

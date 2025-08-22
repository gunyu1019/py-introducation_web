from puepy import Application, Page, Component, t

application = Application()


@application.page('/')
class MainPage(Page):
    def populate(self):
        return ""


application.mount("#app")

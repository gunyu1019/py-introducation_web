from puepy import Application, Page, Component, t

# noinspection PyUnresolvedReferences
import introduction
# noinspection PyUnresolvedReferences
import virtual_business_card
# noinspection PyUnresolvedReferences
import project

application = Application()


@application.page()
class MainPage(Page):
    def populate(self):
        with t.div():
            t.introduction()
            t.project()
            t.virtual_business_card()
        return


application.mount("#app")

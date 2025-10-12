from puepy import Application, Page, Component, t

# noinspection PyUnresolvedReferences
import introduction
# noinspection PyUnresolvedReferences
import virtual_business_card

application = Application()


@application.page()
class MainPage(Page):
    def populate(self):
        with t.div():
            t.introduction()
            t.virtual_business_card()
        return


application.mount("#app")

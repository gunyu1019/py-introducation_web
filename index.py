from puepy import Application, Page, t
from puepy.runtime import is_server_side
from puepy.util import jsobj

# noinspection PyUnresolvedReferences
import introduction
# noinspection PyUnresolvedReferences
import virtual_business_card
# noinspection PyUnresolvedReferences
import project

if not is_server_side:
    import js

application = Application()


@application.page()
class MainPage(Page):
    def populate(self):
        with t.div(id="container"):
            t.introduction(data_anchor="introduction")
            t.project(data_anchor="project")
            t.virtual_business_card(data_anchor="virtual_business_card")
        return

    def on_ready(self):
        if is_server_side:
            return
        pageable = js.Pageable.new("#container")
        pageable.on("scroll", self.on_scroll)

    def on_scroll(self, data):
        # TOO-HARD CODING!!
        if data["index"] != 0:
            self.document.querySelector("div.introduction > img").style.display = "none"
        else:
            self.document.querySelector("div.introduction > img").style.display = "block"


application.mount("#app")

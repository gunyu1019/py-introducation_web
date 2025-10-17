from puepy import Component, t


@t.component()
class VirtualBusinessCard(Component):
    props = []

    def populate(self):
        with t.div(classes=["virtual-business-card"]):
            with t.div(classes=["business-card"]):
                with t.div(classes=["business-card-header"]):
                    t.span("이용현", classes=["business-card-header-title"])
                    t.span("Lee Yong Hyun", classes=["business-card-header-subtitle"])
                    t.img(src="assets/image/qr.png", classes=["business-card-qrcode"])
                with t.div(classes=["business-card-footer"]):
                    t.span("Software Engineer", classes=["business-card-footer-title"])
                    t.div(classes=["divider"])
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-linkedin"])
                        t.a("in/gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-discord"])
                        t.a("@gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fab fa-github"])
                        t.a("gunyu1019", href="https://github.com/gunyu1019")
                    with t.div(classes=["business-card-item"]):
                        t.i(classes=["fas fa-envelope"])
                        t.a("gunyu1019@yhs.kr", href="mailto://gunyu1019@yhs.kr")
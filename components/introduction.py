from puepy import Component, t


@t.component()
class Introduction(Component):
    props = []

    def populate(self):
        with t.div(classes=["introduction"]):
            with t.div(classes=["about-components"]):
                t.h3("👋 안녕하세요?")
                t.span("저는 새로운 지식을 자유롭게 받아들이고, ")
                t.span("세상에 도움이 되는 프로그램을 만드려고 노력하는 ")
                t.span("소프트웨어 개발자 이용현 입니다!")
            t.img(src="./assets/image/background-1.png")  # 배경 이미지
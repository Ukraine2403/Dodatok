class Title():
    def__init__(self, title_text, x, y)
        self.title = title_text
        self.x = x
        self.y = y
self.appearence = True

    def hide(self):
        self.appearence = False
        print(self.title, "- приховано")

    def show(self):
        self.appearence = True
        print(self.title, "- відображається")

    def print_info(self):
        print("Кнопка:", self.title)
        print("Розташування:", "(" + str(self.x) + "," + str(self.y) + ")" )
        print("Видимість:", self.appearence)

main = ("Дізнатися переможця прямо зараз", 150, 50)
rules =("Переможець може бути тільки один", 150, -100)

main.print_info()
rules.print_info()
rules_text.hide()


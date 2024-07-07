class Button():
    def __init__(self, title_text, x, y):
       self.title = title_text
       self.x = x
       self.y = y
       self.appearence = True

    def hide(self):
        self.appearence = False

    def show(self):
        self.appearence = True

    def print_info(self):
        print("Дані про віджет:")
        print(self.title, self.x, self.y, self.appearence)

button_1 = Button("ok", 100, 100)
button_1.print_info()
button_1.hide()
button_1.print_info()

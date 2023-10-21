class Title():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.appearence = True
    def printInfo(self):
        print("Кнопка: ",self.text)
        print(f"Розташування: ({self.x},{self.y})")
        print("Видимість: ", self.appearence)
    def hide(self):
        self.appearence=False
        print(f"{self.text} - приховано")
    def show(self):
        self.appearence=True
        print(f"{self.text} - відображається")

b1 = Title("Дізнатися переможця прямо зараз!", 150, 50)
b2 = Title("Переможець може бути тільки один", 150, -100)
b1.printInfo()
b2.printInfo()
b2.hide()
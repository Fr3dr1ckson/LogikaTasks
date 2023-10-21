class Button():
    def __init__(self,x,y,color, text, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.width = width
        self.height = height
        self.appearence = True

    def hide(self):
        self.appearence = False

    def show(self):
        self.appearence = True
        
    def printInfo(self):
        print(self.text)
        print(self.x)
        print(self.y)
        print(self.appearence)

button1 = Button(100,100, 'red', 'Button', 100, 100)
button1.hide()
button1.printInfo()
button1.show()
button1.printInfo()
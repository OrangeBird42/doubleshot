from tkinter import *
import tkinter.messagebox
import random

readFruit = open('fruitList.txt', "r")
#readFruitContents = readFruit.read()
def random_line(fruitList):
    lines = open(fruitList).read().splitlines()
    return random.choice(lines)

class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        exitButton.place(x=0, y=0)

        helloButton = Button(self, text="click for fruit!", command=self.clickHelloButton)

        helloButton.place(x=42, y=57)


    def clickExitButton(self):
        exit()

    def clickHelloButton(self): 
        #tkinter.messagebox.showinfo("hello!", "nice to meet you!")
        #tkinter.messagebox.showinfo("Fruit List!!", readFruitContents)
        tkinter.messagebox.showinfo("Fruit List", random_line('fruitList.txt'))

readFruit.close()
root = Tk()
app = Window(root)
root.wm_title("Tkinter window") #names the window
root.geometry("320x200")
root.mainloop()






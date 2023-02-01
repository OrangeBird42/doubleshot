from tkinter import *
import tkinter.messagebox


readFruit = open('fruitList.txt', "r")
readFruitContents = readFruit.read()

class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        exitButton.place(x=0, y=0)

        helloButton = Button(self, text="click!", command=self.clickHelloButton)

        helloButton.place(x=42, y=57)


    def clickExitButton(self):
        exit()

    def clickHelloButton(self): 
        #tkinter.messagebox.showinfo("hello!", "nice to meet you!")
        print(readFruitContents)

readFruit.close()
root = Tk()
app = Window(root)
root.wm_title("Tkinter window") #names the window
root.geometry("320x200")
root.mainloop()






from tkinter import *
import tkinter.messagebox

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

    def clickHelloButton(self): #doesnt work rn
        tkinter.messagebox.showinfo("hello!", "nice to meet you!")

root = Tk()
app = Window(root)
root.wm_title("Tkinter window") #names the window
root.geometry("320x200")
root.mainloop()






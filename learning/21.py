from tkinter import *
import tkinter.messagebox as messagebox
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='hello',command=self.hello)
                                                #点击触发hello模块
        self.alertButton.pack()
        #把button加入到父容器中
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','hello,%s'% name)
app=App()
app.master.title('hello')
app.mainloop()
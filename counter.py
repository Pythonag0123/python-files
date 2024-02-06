import tkinter as tk
class counter:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow
        mainwindow.geometry('200x100')
        mainwindow.title('Counter App')
        mainwindow.minsize(100,50)
        mainwindow.maxsize(300,200)
        self.var=tk.IntVar(value=0)
        tk.Label(mainwindow,text='Welcome to the counter App').pack()
        lb=tk.Label(mainwindow,textvariable=self.var,font=('bold',24))
        lb.pack()
        bt1=tk.Button(mainwindow,text='Increment',command=self.action1)
        bt1.pack(side=tk.LEFT,ipadx=10,ipady=10)
        bt2=tk.Button(mainwindow,text='Decrement',command=self.action2)
        bt2.pack(side=tk.RIGHT,ipadx=10,ipady=10)
    def action1(self):
        self.var.set(self.var.get()+1)
    def action2(self):
        self.var.set(self.var.get()-1)
#main-code
root=tk.Tk()
exe=counter(root)
root.mainloop()
                

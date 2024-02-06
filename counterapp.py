#counter app
import tkinter as tk
root=tk.Tk()
root.geometry('200x100')
root.title('Counter App')
root.minsize(100,50)
root.maxsize(300,200)
def action1():
    data=lb.cget('text')+1
    lb.config(text=data)
    if data>10:
        lb.confi
def action2():
    data=lb.cget('text')-1
    if data<0:
         pass
    else:
        lb.config(text=data,fg='green')
       
tk.Label(root,text='Welcome to the Counter App')
lb=tk.Label(root,text=0)
lb.pack()
bt1=tk.Button(root,text='Increment',command=action1)
bt1.pack(side=tk.LEFT,padx=5,pady=5,ipadx=10,ipady=10)
bt2=tk.Button(root,text='Decrement',command=action2)
bt2.pack(side=tk.RIGHT,padx=5,pady=5,ipadx=10,ipady=10)
root.mainloop()

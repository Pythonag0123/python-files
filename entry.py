import tkinter as tk
root=tk.Tk()
def action():
    data=entry.get()
    disp.config(text='Hello,' +data)
    entry.delete(0,tk.END)

tk.Label(root,text='Enter Your Name').pack()
entry=tk.Entry(root)
entry.pack()
bt1=tk.Button(root,text='Enter',command=action)
bt1.pack()
disp=tk.Label(root,text='')
disp.pack()

root.mainloop()

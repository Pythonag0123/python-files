import tkinter as tk
from PIL import ImageTk, Image
import os
def action1():
    n=n-1
    Image1=ImageTk.PhotoImage(image[n])
    if n==0:
        n=len(image)-1


def action2():
    n=n+1
    Image1=ImageTk.PhotoImage(image[n])
    if n==len(n):
        n=0


dtr = r"C:\Users\lenovo\Downloads"

lst_dir = os.listdir(dtr)
image = [im for im in lst_dir if im.endswith('.png') or im.endswith('.jpg')]
n=0
if __name__ == "__main__":
    root = tk.Tk()

    Image1 = Image.open(rimport tkinter as tk
from PIL import ImageTk, Image
import os
def action1():
    n=n-1
    Image1=ImageTk.PhotoImage(image[n])
    if n==0:
        n=len(image)-1


def action2():
    n=n+1
    Image1=ImageTk.PhotoImage(image[n])
    if n==len(n):
        n=0


dtr = r"C:\Users\lenovo\Downloads"

lst_dir = os.listdir(dtr)
image = [im for im in lst_dir if im.endswith('.png') or im.endswith('.jpg')]
n=0
if __name__ == "__main__":
    root = tk.Tk()

    
    Image1 = ImageTk.PhotoImage(Image1)
    Label1 = tk.Label(root, image=Image1)
    Label1.grid(row=0, column=0, columnspan=2)

    bt1 = tk.Button(root, text="previous", command=action1)
    bt1.grid(row=1, column=0)

    bt2 = tk.Button(root, text="next", command=action2)
    bt2.grid(row=1, column=1)

    root.mainloop()

import tkinter as tk
from PIL import ImageTk, Image
import os

n = 0

def action1():
    global n
    n = (n - 1) % len(image)
    load_image()

def action2():
    global n
    n = (n + 1) % len(image)
    load_image()

def action3(root):
    root.destroy()

def load_image():
    global Image1
    img = Image.open(os.path.join(dtr, image[n]))
    img = img.resize((1200, 600), Image.LANCZOS)  # Resize the image
    Image1 = ImageTk.PhotoImage(img)
    Label1.configure(image=Image1)
    Label1.image = Image1

dtr = r"C:\Users\lenovo\Downloads"
lst_dir = os.listdir(dtr)
image = [im for im in lst_dir if im.endswith('.png') or im.endswith('.jpg')]

if __name__ == "__main__":
    root = tk.Tk()

    Label1 = tk.Label(root)
    Label1.grid(row=0, column=0, columnspan=3)

    load_image()

    Label1.configure(image=Image1)

    bt1 = tk.Button(root, text="previous", command=action1)
    bt1.grid(row=1, column=0)

    bt2 = tk.Button(root, text="next", command=action2)
    bt2.grid(row=1, column=1)
    
    bt3=tk.Button(root,text="exit",command= lambda:action3(root))
    bt3.grid(row=1, column=2)

    root.mainloop()

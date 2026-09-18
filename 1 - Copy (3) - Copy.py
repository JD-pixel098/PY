

# import tkinter as tk
#
# from PIL import Image
# import os
#
# kd = Image.open(r"C:/Users/SIC/Desktop/neww/photo.png")
# kd_root = tk.Tk()
#
#
# import label
#
# kd_root = tk.Tk()                                    #2
#
# kd_root.geometry("300x500")
#
# kd = ImageTk.PhotoImage(kd)
#
# label = Label(root,image = kd)
# label.pack
#
#
#
#
# kd_root.minsize(100, 100)
#
# kd_root.maxsize(800, 700)
#
# label = tk.Label( text="Opening with 250 discount")
# label.pack()
#
# kd_root.mainloop()                                      #3


# import tkinter as tk



# import tkinter as tk
# import label
# prasad_root = tk.Tk()
# prasad_root.title("welcome to pycharm")   #prasad _root.title("welcome to the party")
# prasad_root.geometry("733x434")            # prasad_root.minsiz
# prasad_root.minsize(733,434)
# prasad_root.maxsize(933,634)
# label= tk.Label(text="welcome to pycharm")
# label.pack()
# prasad_root.mainloop()

# import tkinter as tk
# from socket import SocketIO
#
# from PIL import Image, ImageTk
# root = tk.Tk()
# root.title("jai kisan image")
# img = Image.open(r"C:\Users\SIC\Documents\GitHub\PY\JAGADEESH\MY_PROJECRS\image.png")
# photo = ImageTk.PhotoImage(img)
#
# # Show image in a label
# label = tk.Label(root, image=photo)
# label.pack()
#
# root.mainloop()


# import tkinler as tk
# from PIL import Image, ImageTk
#
# root = tk.Tk()
# root.geometry("300x300")
# root.resizable(width = False,height= False)
#
# main_frame = tk.Frame(root,bg = "white")
#
# image.obj = ImageTk.PhotoImage(Image.open("image.png"))



# import tkinter as tk
# windows = tk()
# window.title("dragon booster")
# canvas = Canvas(window,width = 300,height = 300)
# canvas.pack()
# self_image =photoImage(file = "C:\\Users\\SIC\\Documents\\GitHub\\PY\\JAGADEESH\\25265.png")
# canvas.create_image(0,0,image=self_image, anchor="nw")
#

# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
# root.title("cheat codes for CGI🚁🚁")
# root.geometry("300x250")

# label = tk.Label(root,text = "nutter tools")
# label.pack(padx=0,pady=20)
#
# type_entry = tk.Entry(root,font = ("thug tools",7))
# type_entry.pack(pady=5)
# usage_entry = tk.Entry(root,font = ("infinity weapons",10))
# usage_entry.pack(pady=5)





# name_entry = tk.Entry(root, font=("Comic Sans MS", 12))
# name_entry.pack(pady=5)
#
# age_entry = tk.Entry(root, font=("Comic Sans MS", 12))
# age_entry.pack(pady=5)



# root.mainloop()

# Language: Python
import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        canvas.config(bg=color)

root = tk.Tk()
root.title("Kids Coloring App")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

color_button = tk.Button(root, text="Pick a Color", command=choose_color)
color_button.pack(pady=10)

root.mainloop()






# import tkinter as tk
#
# from PIL import Image
# import os
#
# kd = Image.open(r"C:/Users/SIC/Desktop/neww/photo.png")
# kd_root = tk.Tk()
#
#
# import label
#
# kd_root = tk.Tk()                                    #2
#
# kd_root.geometry("300x500")
#
# kd = ImageTk.PhotoImage(kd)
#
# label = Label(root,image = kd)
# label.pack
#
#
#
#
# kd_root.minsize(100, 100)
#
# kd_root.maxsize(800, 700)
#
# label = tk.Label( text="Opening with 250 discount")
# label.pack()
#
# kd_root.mainloop()                                      #3


# import tkinter as tk



# import tkinter as tk
# import label
# prasad_root = tk.Tk()
# prasad_root.title("welcome to pycharm")   #prasad _root.title("welcome to the party")
# prasad_root.geometry("733x434")            # prasad_root.minsiz
# prasad_root.minsize(733,434)
# prasad_root.maxsize(933,634)
# label= tk.Label(text="welcome to pycharm")
# label.pack()
# prasad_root.mainloop()

# import tkinter as tk
# from socket import SocketIO
#
# from PIL import Image, ImageTk
# root = tk.Tk()
# root.title("jai kisan image")
# img = Image.open(r"C:\Users\SIC\Documents\GitHub\PY\JAGADEESH\MY_PROJECRS\image.png")
# photo = ImageTk.PhotoImage(img)
#
# # Show image in a label
# label = tk.Label(root, image=photo)
# label.pack()
#
# root.mainloop()


# import tkinler as tk
# from PIL import Image, ImageTk
#
# root = tk.Tk()
# root.geometry("300x300")
# root.resizable(width = False,height= False)
#
# main_frame = tk.Frame(root,bg = "white")
#
# image.obj = ImageTk.PhotoImage(Image.open("image.png"))



# import tkinter as tk
# windows = tk()
# window.title("dragon booster")
# canvas = Canvas(window,width = 300,height = 300)
# canvas.pack()
# self_image =photoImage(file = "C:\\Users\\SIC\\Documents\\GitHub\\PY\\JAGADEESH\\25265.png")
# canvas.create_image(0,0,image=self_image, anchor="nw")
#

# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
# root.title("cheat codes for CGI🚁🚁")
# root.geometry("300x250")

# label = tk.Label(root,text = "nutter tools")
# label.pack(padx=0,pady=20)
#
# type_entry = tk.Entry(root,font = ("thug tools",7))
# type_entry.pack(pady=5)
# usage_entry = tk.Entry(root,font = ("infinity weapons",10))
# usage_entry.pack(pady=5)





# name_entry = tk.Entry(root, font=("Comic Sans MS", 12))
# name_entry.pack(pady=5)
#
# age_entry = tk.Entry(root, font=("Comic Sans MS", 12))
# age_entry.pack(pady=5)



# root.mainloop()

# Language: Python
import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        canvas.config(bg=color)

root = tk.Tk()
root.title("Kids Coloring App")

canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

color_button = tk.Button(root, text="Pick a Color", command=choose_color)
color_button.pack(pady=10)

root.mainloop()





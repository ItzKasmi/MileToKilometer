from tkinter import *

# Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.pack()

def change_text():
    my_label["text"] = choice.get()


button = Button(text="Click Me", command=change_text)
button.pack()

choice = Entry(width=10)
choice.pack()

window.mainloop()

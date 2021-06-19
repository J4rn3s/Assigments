from tkinter import *
import tkinter.messagebox
def save_data():
    try:
        fileD = open("deliveries.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.set(None)
        description.delete(0, END)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)
        app.title("Cannot write to the File %s" % ex)

app = Tk()
app.title('Snowboard 4Life - Mountain Tips')
Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)
OptionMenu(app,depot, "Mammoth-CA - USA", "BigBear-CA - USA", "SnowSummit-CA - USA", "Whistler-BC - CA").pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()
app.mainloop()
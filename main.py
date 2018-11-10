import tkinter as tk

window = tk.Tk()
window.title('title')
window.geometry('400x200')

var1 = tk.StringVar()
lable = tk.Label(window, textvariable=var1, bg='red', width=100, height=3)
lable.pack()


def click_func():
    listbox_value = listbox.get(listbox.curselection())
    var1.set(listbox_value)


button = tk.Button(window, text='click me', command=click_func, width=100, height=1)
button.pack()


var2 = tk.StringVar()
var2.set(('11', '22', '33', '44'))

listbox = tk.Listbox(window, listvariable=var2)

a = [1,2,3,4]
for x in a:
    listbox.insert('end', x)
listbox.pack()


window.mainloop()

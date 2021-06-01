import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


def month_changed(event):
    msg = f'You selected {month_cb.get()}!'
    showinfo(title='Result', message=msg)


# month of year
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

label = ttk.Label(text="Please select a month:")
label.pack(fill='x', padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(root, textvariable=selected_month)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.pack(fill='x', padx=5, pady=5)

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()
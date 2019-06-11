from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as m_box
from schwifty import IBAN

root = tk.Tk()
root.title("iBan Generator")
root.geometry("500x400")
root.minsize(500, 400)
root.maxsize(500, 400)
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=70, pady=55)
label = ttk.Label(frame, text="Enter Your Country Code :").grid(row=0, column=0, padx=0, pady=2, sticky=tk.W)
country_code = tk.StringVar()
country_entry = ttk.Entry(frame, width=55, textvariable=country_code)
country_entry.grid(row=1, columnspan=4, padx=0, pady=2, ipady=3)
country_entry.focus()

label2 = ttk.Label(frame, text="Enter Your Bank Code :").grid(row=2, column=0, padx=0, pady=2, sticky=tk.W)
bank_code = tk.StringVar()
bank_entry = ttk.Entry(frame, width=55, textvariable=bank_code)
bank_entry.grid(row=3, columnspan=4, padx=0, pady=2, ipady=3)

label3 = ttk.Label(frame, text="Enter Your Account Code :").grid(row=4, column=0, padx=0, pady=2, sticky=tk.W)
account_code = tk.StringVar()
account_entry = ttk.Entry(frame, width=55, textvariable=account_code)
account_entry.grid(row=5, columnspan=4, padx=0, pady=2, ipady=3)

def onGen():
    def onCopy():
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(iban_get)
        clip.destroy()
        m_box.showinfo('Success','iBAN Copied Successfully')
    get_country = country_code.get()
    get_bank = bank_code.get()
    get_account = account_code.get()
    if get_country != '' and get_account != '' and get_bank != '':
        iban_get = IBAN.generate(get_country, bank_code=get_bank, account_code=get_account)
        got_iBan = ttk.Label(root, text=f"Your iBAN is {iban_get}", font="arial 12 bold")
        got_iBan.grid(row=1, column=0, padx=50, pady=2)
        btncopy = ttk.Button(root, text="Copy iBAN", command=onCopy)
        btncopy.grid(row=2, columnspan=3, padx=50, pady=2, ipady=5)
        m_box.showinfo('Success', 'iBAN Generated Successfully')
    else:
        m_box.showerror('Error', 'Please Fill Every Boxes Carefully !')
btn1 = ttk.Button(frame, text="Generate iBAN", command=onGen)
btn1.grid(row=6, columnspan=5, padx=70, pady=10, ipady=5)
root.mainloop()
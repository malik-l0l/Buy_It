"""
specially designed for those who cant do mental calculation in a real world scenario,
for example going to the local market.

This program will take two parameter and calculates the third one.

This program has three variables:
    1)Price per kilogram      -> 10$ for 1 Kg of Apple.
    2)Kg wanted               -> you need  750 grams
    so, 3)Money given will be -> 7.5 rs.

we can calculate this because these three values are interconnected.
"""
from tkinter import *


# ------------ METHODS ---------------------------------------------------------------------------------
def calculate():
    """
    takes input given in the textfield and shows the output in the label
    :return: None
    """
    display_label.config(text="")
    price = price_entry.get()
    kilos = kg_entry.get()
    money = money_entry.get()

    #  happens : if 1_(every column is empty) or 2_(any one column in filled) or 3_(every column is filled)
    #  do      : tell user to fill any two columns
    if (len(price) == 0 and len(kilos) == 0 and len(money) == 0) or (  # 1
            len(price) != 0 and len(kilos) == 0 and len(money) == 0) or (  # 2
            len(price) == 0 and len(kilos) != 0 and len(money) == 0) or (  # 2
            len(price) == 0 and len(kilos) == 0 and len(money) != 0) or (  # 2
            len(price) != 0 and len(kilos) != 0) and len(money) != 0:  # 3
        display_label.config(text="Please enter\nany 2 columns!")

    #  happens : if price/kg column is empty
    #  do      : calculate the price/kg
    elif len(price_entry.get()) == 0 and kilos.isdigit() and money.isdigit():
        display_label.config(text=f"Price/kg = {(float(money) / float(kilos)):.1f} rs")

    #  happens : if kg column is empty
    #  do      : calculate the grams
    elif len(kg_entry.get()) == 0 and price.isdigit() and money.isdigit():

        display_label.config(text=f"grams shown : {(((1 / float(price)) * float(money)) * 1000):.1f} g")

    #  happens : if money column is empty
    #  do      : calculate the money given
    elif len(money_entry.get()) == 0 and price.isdigit() and kilos.isdigit():
        display_label.config(text=f"Money given : {(float(price) * float(kilos)):.1f} rs")

    #  happens : if user enters number
    #  do      : calculate the money given
    else:
        display_label.config(text="Please enter Integers!")


# ------------ END METHODS ----------------------------------------------------------------------------


# ==================== MAIN WINDOW ===============================================================================
window = Tk()
window.title("Buy Helper")
window.config(bg="Black")
window.resizable(False, False)

BigFrame = Frame(window, bd=2, relief=SUNKEN)
BigFrame.pack()

frame = Frame(BigFrame)
frame.pack()
frame2 = Frame(BigFrame)
frame2.pack()

price_label = Label(frame, text="Price/kg *      : ", font=("Arial", 15, "bold"))
price_label.grid(row=0, column=0)
price_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
price_entry.grid(row=0, column=1)

kg_label = Label(frame, text="Kg wanted     : ", font=("Arial", 15, "bold"))
kg_label.grid(row=1, column=0)
kg_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
kg_entry.grid(row=1, column=1)

money_label = Label(frame, text="Money given  : ", font=("Arial", 15, "bold"))
money_label.grid(row=2, column=0)
money_entry = Entry(frame, font=('Consoles', 20, "bold"), width=10)
money_entry.grid(row=2, column=1)

Button(frame2, text="Enter", font=("Consoles", 10, "bold italic"),
       command=calculate, width=38).pack(pady=2)

display_label = Label(frame2, font=("Arial", 13, "bold"), bg="black",
                      fg="#00FF00", width=30, height=2, bd=5, relief=RAISED)
display_label.pack()

window.mainloop()

# ================ END MAIN WINDOW ===============================================================================

#tkinter: create panels
#partial: allows the usage of functions with parameters on the buttons
from tkinter import *
from tkinter import ttk
from functools import partial

#Part 1: Get the presente cash (which is registered in the text file)

#Quantities
with open('cash.txt', 'r') as file:
    quantities = file.read().splitlines()

#Values
values = [
    '0.05',
    '0.10',
    '0.25',
    '0.50',
    '1',
    '2',
    '5',
    '10',
    '20',
    '50',
    '100',
    '200'
]

#Dictionary that contains the values with the corresponded quantity
cash={}
for value, quantity in zip(values, quantities):
    cash[value] = int(quantity)


#Part 2: main panel. Contains the 3 options that can be used to manipulate and see the cash
    #Register cash: user can change any quantity in the cash.
    #See cash: user can see the present cash
    #Register exchange: user can register the sale of a product, updating automatically the cash and also receiving the correct change
def main_panel():
    #Creating the panel
    mainframe = ttk.Frame(root, padding='3 3 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Title
    ttk.Label(mainframe, text='What do you want to do?').grid(column=2, row=1)

    #Options
    ttk.Button(mainframe, text='Register Cash', command=first_option).grid(column=1, row=2)
    ttk.Button(mainframe, text='See Cash', command = see_cash).grid(column=2, row=2)
    ttk.Button(mainframe, text='Register Exchange', command = register_exchange).grid(column=3, row=2)

    #Just some margins to the elements of the panel
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)


#Part 3: each of the 3 options, with the corresponded panels and necessary functions
#3.1: Register Cash

#initial_cash: shows the panel that allows to register the present cash. By default, shows the cash that was previous saved, but allows changes
def first_option():
    #Creating the panel
    register_cash_panel = ttk.Frame(root, padding='3 3 12 12')
    register_cash_panel.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Panel title
    ttk.Label(register_cash_panel, text='Register Present Cash').grid(column=2, row=1)

    #Columns titles
    ttk.Label(register_cash_panel, text='Value').grid(column=1, row=2)
    ttk.Label(register_cash_panel, text='Quantity').grid(column=3, row=2)

    #Columns values (label for values and entry for quantities)
    temporary_cash={}
    i=3
    for value, quantity in cash.items():
        ttk.Label(register_cash_panel, text=value).grid(column=1, row=i)

        temporary_cash[value] = StringVar()
        entry = Entry(register_cash_panel, width=3, textvariable=temporary_cash[value])
        entry.grid(column=3, row=i)
        entry.insert(0,str(quantity))

        i+=1

    #Buttons: register for saving the cash and return to return to main panel
    ttk.Button(register_cash_panel, text='Register', command=partial(save_cash, temporary_cash)).grid(column=4, row=i)
    ttk.Button(register_cash_panel, text='Return', command=main_panel).grid(column=4, row=i + 1)

    root.mainloop()

#save_cash: used on the register cash panel to save the cash both in script and in the txt
def save_cash(temporary_cash):
    with open('cash.txt','w') as file:
        for value, quantity in temporary_cash.items():
            cash[value] = int(quantity.get())
            file.write(str(quantity.get())+'\n')

#3.2: See Cash

#see_panel: panel that allows to see the present cash
def see_cash():
    #Creating the panel
    see_cash_panel = ttk.Frame(root, padding='3 3 12 12')
    see_cash_panel.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Panel title
    ttk.Label(see_cash_panel, text='Cash').grid(column=2, row=1)

    #Columns titles
    ttk.Label(see_cash_panel, text='Value').grid(column=1, row=2)
    ttk.Label(see_cash_panel, text='Quantity').grid(column=3, row=2)

    #Columns values
    i=3
    for value, quantity in cash.items():
        ttk.Label(see_cash_panel, text=value).grid(column=1, row=i)
        ttk.Label(see_cash_panel, text=quantity).grid(column=3, row=i)
        i+=1

    #Button: return to return to main panel
    ttk.Button(see_cash_panel, text='Return', command=main_panel).grid(column=4, row=i)

    #Just some margins for the elements of the panel
    for child in see_cash_panel.winfo_children():
        child.grid_configure(padx=0, pady=3)

#3.3: Register Exchange

#register_exchange: creates the panel that allows to register the price of the product and the payment
def register_exchange():
    #Creates the panel
    register_exchange_panel = ttk.Frame(root, padding='3 3 12 12')
    register_exchange_panel.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Panel title
    ttk.Label(register_exchange_panel, text='Exchange', font='Bold').grid(column=4, row=1)

    #Price of the product
    ttk.Label(register_exchange_panel, text='Price').grid(column=1, row=2)
    price = StringVar()
    entry = Entry(register_exchange_panel, width=5, textvariable=price)
    entry.grid(column=2,row=2)

    #Payment title
    ttk.Label(register_exchange_panel, text='Payment').grid(column=4, row=2)

    #Column titles
    ttk.Label(register_exchange_panel, text='Value').grid(column=3, row=3)
    ttk.Label(register_exchange_panel, text='Quantity').grid(column=5, row=3)

    #Payment (by default, each value has a quantity of zero)
    paid={}
    i=4
    for value in cash.keys():
        paid[value] = IntVar()
        ttk.Label(register_exchange_panel, text=value).grid(column=3, row=i)
        entry = Entry(register_exchange_panel, width=3, textvariable=paid[value])
        entry.grid(column=5, row=i)
        i+=1
        entry.insert(0, '0')

    #Buttons: register to register the exchange and show the change, and return to return to the main panel
    ttk.Button(register_exchange_panel, text='Register', command=partial(change, price, paid)).grid(column=6, row=i)
    ttk.Button(register_exchange_panel, text='Return', command=main_panel).grid(column=6, row=i + 1)

    root.bind("<Return>", change)
    root.mainloop()

#change: calculates the change and shows it on a panel
def change(product_value, payment):
    #Creating the panel that shows the change to return to the client
    forthpanel = ttk.Frame(root, paddin='3 3 12 12 ')
    forthpanel.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Panel title
    ttk.Label(forthpanel, text='Change').grid(column=2, row=1)

    #Column titles
    ttk.Label(forthpanel, text='Value').grid(column=1, row=2)
    ttk.Label(forthpanel, text='Quantity').grid(column=3, row=2)

    #Putting the value of the price into a variable
    price = float(product_value.get())

    #Calculating the total payment given by the customer
    #Simultaneously, takes the coins and notes given by the customer and adds then to the cash
    payment_total = 0
    for value, quantity in payment.items():
        payment_total += float(value)*quantity.get()
        cash[value] += quantity.get()

    #Calculates the total change (sum of all coins and notes)
    change_total = payment_total - price

    #Calculates the change in terms of coins and notes
    #Simultaneously, takes the coins and notes of the changr and subtract then from the cash
    #Also builds the values of the columns (values and quantities)
    #The algorithm prioritizes using the highest value avaliable
    change = {}
    values = list(payment.keys())[::-1] #from highest to lowest
    for value in values:
        quantity = change_total//float(value)
        if quantity > 0 and cash[value] >= quantity:
            change[value] = int(quantity)
            cash[value] -= int(quantity)
        change_total -= quantity*float(value)

        i=3
        for value, quantity in change.items():
            ttk.Label(forthpanel, text=value).grid(column=1, row=i)
            ttk.Label(forthpanel, text=quantity).grid(column=3, row=i)
            i+=1

    #Writing the new cash in the txt file
    with open('cash.txt', 'w') as file:
        for quantity in cash.values():
            file.write(str(quantity)+'\n')

    #Button return to return to the main panel
    ttk.Button(forthpanel, text='Return', command=main_panel).grid(column=4, row=i+1)

    root.mainloop()


#Part 4: running the script
def main():
    #Creates the family of panels
    global root
    root = Tk()
    root.title('Managing the Cash')

    #Runs the main panel function
    main_panel()
    root.mainloop()


if __name__ == "__main__":
    main()

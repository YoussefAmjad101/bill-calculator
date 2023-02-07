from tkinter import *
import random
from datetime import datetime

root = Tk()
root.geometry("1200x650+100+20")
root.title("Restaurant Management system")

f = Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
f1.pack(side=LEFT, fill="both", expand=1)

f2 = Frame(root, bd=5, height=400, width=300, relief=RAISED)


now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand = StringVar()
Coffee = StringVar()
Bread = StringVar()
Water = StringVar()
Milk = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tea = StringVar()
Tax = StringVar()
cost = StringVar()
date = StringVar()
Juice = StringVar()
Choclate = StringVar()


lbl_Tea = Label(f1, font=('arial', 20, 'bold'), text="Tea 2DH",
                 width=12, bd=3, anchor='w')
lbl_Tea.grid(row=1, column=0)
txt_Tea = Entry(f1, font=('arial', 20, 'bold'), textvariable=Tea,
                 bd=3, width=8, bg="grey", justify='right')
txt_Tea.grid(row=1, column=1)

lbl_coffee = Label(f1, font=('arial', 20, 'bold'), text="coffee 7DH",
                 width=12, bd=3, anchor='w')
lbl_coffee.grid(row=2, column=0)
txt_coffee = Entry(f1, font=('arial', 20, 'bold'), textvariable=Coffee,
                 bd=3, width=8, bg="grey", justify='right')
txt_coffee.grid(row=2, column=1)

lbl_Bread = Label(f1, font=('arial', 20, 'bold'),
                   text=" Bread 2.50DH", width=12, bd=3, anchor='w')
lbl_Bread.grid(row=3, column=0)
txt_Bread = Entry(f1, font=('arial', 20, 'bold'), textvariable=Bread,
                   bd=3, width=8, bg="grey", justify='right')
txt_Bread.grid(row=3, column=1)

lbl_water = Label(f1, font=('arial', 20, 'bold'),
                  text="Water 5DH ", width=12, bd=3, anchor='w')
lbl_water.grid(row=4, column=0)
txt_water = Entry(f1, font=('arial', 20, 'bold'), textvariable=Water,
                  bd=3, width=8, bg="grey", justify='right')
txt_water.grid(row=4, column=1)

lbl_Milk = Label(f1, font=('arial', 20, 'bold'),
                  text="Milk 6DH", width=12, bd=3, anchor='w')
lbl_Milk.grid(row=5, column=0)
txt_Milk = Entry(f1, font=('arial', 20, 'bold'), textvariable=Milk,
                  bd=3, width=8, bg="grey", justify='right')
txt_Milk.grid(row=5, column=1)

lbl_Choclate = Label(f1, font=('arial', 20, 'bold'), text="Choclate 8DH",
                width=12, bd=3, anchor='w')
lbl_Choclate.grid(row=6, column=0)
txt_Choclate = Entry(f1, font=('arial', 20, 'bold'), textvariable=Choclate,
                bd=3, width=8, bg="grey", justify='right')
txt_Choclate.grid(row=6, column=1)

lbl_Juice = Label(f1, font=('arial', 20, 'bold'),
                   text="Juice 10 DH", width=12, bd=3, anchor='w')
lbl_Juice.grid(row=7, column=0)
txt_Juice = Entry(f1, font=('arial', 20, 'bold'), textvariable=Juice,
                   bd=3, width=8, bg="grey", justify='right')
txt_Juice.grid(row=7, column=1)


def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)
    try:
        qt = int(Tea.get())
    except:
        qt = 0
    try:
        qm = int(Milk.get())
    except:
        qm = 0
    try:
        qw = int(Water.get())
    except:
        qw = 0
    try:
        qj = int(Juice.get())
    except:
        qj = 0
    try:
        qc = int(Coffee.get())
    except:
        qc = 0
    try:
        qb = int(Bread.get())
    except:
        qb = 0
    try:
        qch = int(Choclate.get())
    except:
        qch = 0

    costofcoffee = qc * 7
    costoftea = qt * 2
    costofwater = qw * 5
    costofJuice = qj * 10
    costofmilk = qm * 6
    costofchoclate = qch * 8
    costofbread = qb * 2.50

    f2.pack(side=RIGHT, fill="both", expand=1)
    f2.configure(background="light yellow")

    lbl_bill = Label(f2, font=('arial', 18, 'bold'), text="Bill No.",
                     bg="light yellow", width=12, bd=20, anchor='w')
    lbl_bill.grid(row=1, column=0)
    txt_bill = Entry(f2, font=('arial', 18, 'bold'), textvariable=rand,
                     bd=6, width=17, bg="brown", fg='white', justify='right')
    txt_bill.grid(row=1, column=1)

    lbl_date = Label(f2, font=('arial', 18, 'bold'), text="Date",
                     bg="light yellow", width=12, bd=10, anchor='w')
    lbl_date.grid(row=2, column=0)
    txt_date = Entry(f2, font=('arial', 18, 'bold'), textvariable=date,
                     bd=6, width=17, bg="Pale Green1", justify='right')
    txt_date.grid(row=2, column=1)

    lbl_cost = Label(f2, font=('arial', 18, 'bold'), text="Cost",
                     bg="light yellow", width=12, bd=10, anchor='w')
    lbl_cost.grid(row=3, column=0)
    txt_cost = Entry(f2, font=('arial', 18, 'bold'), textvariable=cost,
                     bd=6, width=17, bg="Pale Green1", justify='right')
    txt_cost.grid(row=3, column=1)

    lbl_service = Label(f2, font=('arial', 18, 'bold'), text="Service Charge",
                        bg="light yellow", width=12, bd=10, anchor='w')
    lbl_service.grid(row=4, column=0)
    txt_service = Entry(f2, font=('arial', 18, 'bold'), textvariable=Service_Charge,
                        bd=6, width=17, bg="Pale Green1", justify='right')
    txt_service.grid(row=4, column=1)

    lbl_total = Label(f2, font=('arial', 18, 'bold'), text="Total",
                      bg="light yellow", width=12, bd=10, anchor='w')
    lbl_total.grid(row=6, column=0)
    txt_total = Entry(f2, font=('arial', 18, 'bold'), textvariable=Total,
                      bd=6, width=17, bg="brown", fg='white', justify='right')
    txt_total.grid(row=6, column=1)

    Totalcost = costoftea + costofchoclate + costofcoffee + \
        costofJuice + costofmilk + costofwater + costofbread
    costofmeal =  str('%.2f' % Totalcost),"DH."
    ser_charge = (Totalcost * 0.01)
    service = str('%.2f' % ser_charge),"DH."
    overall = Totalcost + ser_charge
    total = str('%.2f' % overall), "DH."

    Service_Charge.set(service)
    cost.set(costofmeal)
    Total.set(total)


def qexit():
    root.destroy()


def reset():
    Choclate.set('')
    Coffee.set('')
    Tea.set('')
    Bread.set('')
    Juice.set('')
    date.set('')
    Water.set('')
    Milk.set('')
    f2.pack_forget()


btn_Total = Button(f1, bd=5, fg="white", font=('arial', 16, 'bold'),
                   width=14, text="CALCULATE BILL", bg="dodgerblue", command=generate_bill)
btn_Total.grid(row=9, column=0, padx=10, pady=10)

btn_reset = Button(f1, bd=5, fg="white", font=(
    'arial', 16, 'bold'), width=10, text="RESET", bg="dodgerblue", command=reset)
btn_reset.grid(row=9, column=1, padx=10, pady=10)

btn_exit = Button(f1, bd=5, fg="white", font=('arial', 16, 'bold'),
                  width=10, text="EXIT", bg="dodgerblue", command=qexit)
btn_exit.grid(row=9, column=2, padx=10, pady=10)

root.mainloop()
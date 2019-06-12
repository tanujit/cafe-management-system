from tkinter import*
import random
import time;
import datetime


root= Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background='blue')

Tops = Frame(root, width=1350,height=100,bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900,height=650,bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440,height=650,bd=8, relief="raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width=440,height=450,bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width=440,height=250,bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width=900,height=330,bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900,height=320,bd=6, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height=330,bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height=330,bd=16, relief="raise")
f1ab.pack(side=RIGHT)


f2aa = Frame(f2a, width = 450, height=330,bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width = 450, height=330,bd=14, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='blue')
f1.configure(background='blue')
f2.configure(background='blue')

#==================================================================HEADING==========================================================================

lblInfo = Label(Tops, font=('arial',60,'bold'), text= " Cafe Management System ", bd=10)
lblInfo.grid(row=0,column=0)

#===================================================================COST OF ITEMS=============================================================

def CostofItems():
    Item1=float(E_Latte.get())
    Item2=float(E_Coke.get())
    Item3=float(E_Iced_Latte.get())
    Item4=float(E_Coffee.get())
    Item5=float(E_Cappuccin.get())
    Item6=float(E_Tea.get()) 
    Item7=float(E_Cold_coffee.get())
    Item8=float(E_Filter_coffee.get())
    
    Item9=float(E_Coffee_cake.get()) 
    Item10=float(E_Black_forest.get())
    Item11=float(E_Cream_cake.get())
    Item12=float(E_Lagoos_cake.get())
    Item13=float(E_Fruit_cake.get())
    Item14=float(E_Chocolate_cake.get())
    Item15=float(E_Chocolava.get())
    Item16=float(E_Bread_cake.get())

    PriceofDrinks = (Item1 * 12) + (Item2 * 25.5) + (Item3 * 24.99) + (Item4 * 10.29) + (Item5 * 20.20) + (Item6 * 5.9) + (Item7 * 12.99) + (Item8 * 55.45)

    PriceofCakes = (Item9 * 12.2) + (Item10 * 15.99) + (Item11 * 40.99) + (Item12 * 22.29) + (Item13 * 25.20) + (Item14 * 30.9) + (Item15 * 35.99) + (Item16 * 40.45)

    DrinksPrice ="Rs", str ('%.2f'%(PriceofDrinks))

    CakesPrice ="Rs", str ('%.2f'%(PriceofCakes))

    CostofCakes.set(CakesPrice)

    CostofDrinks.set(DrinksPrice)

    SC= "Rs" , str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax= "Rs" , str('%.2f'%((PriceofDrinks + PriceofCakes + 1.59)* 0.15))
    PaidTax.set(Tax)

    TT = ((PriceofDrinks + PriceofCakes + 1.59)*0.15)
    TC = "Rs" , str('%.2f'%(PriceofDrinks + PriceofCakes + 1.59 + TT))
    TotalCost.set(TC)

#=======================================================METHODS=======================================================================
def qExit():
    qExit=messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Latte.set("0")
    E_Coke.set("0")
    E_Iced_Latte.set("0")
    E_Coffee.set("0")
    E_Cappuccin.set("0")
    E_Tea.set("0")
    E_Cold_coffee.set("0")
    E_Filter_coffee.set("0")

    E_Coffee_cake.set("0")
    E_Black_forest.set("0")
    E_Cream_cake.set("0")
    E_Lagoos_cake.set("0")
    E_Fruit_cake.set("0")
    E_Chocolate_cake.set("0")
    E_Chocolava.set("0")
    E_Bread_cake.set("0")

             
    var1.set(0)    
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCappuccin.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCold_coffee.configure(state=DISABLED)
    txtFilter_coffee.configure(state=DISABLED)
    txtCoffee_cake.configure(state=DISABLED)
    txtBlack_forest.configure(state=DISABLED)
    txtCream_cake.configure(state=DISABLED)
    txtLagoos_cake.configure(state=DISABLED)
    txtFruit_cake.configure(state=DISABLED)
    txtChocolate_cake.configure(state=DISABLED)
    txtChocolava.configure(state=DISABLED)
    txtBread_cake.configure(state=DISABLED)
#======================================================================RECEIPT============================================================================

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+ randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t\t'+ DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t'+"Count of Items \n")
    txtReceipt.insert(END,'Latte:\t\t\t\t'+ E_Latte.get()+"\n")
    txtReceipt.insert(END,'Coke:\t\t\t\t'+ E_Coke.get()+"\n")
    txtReceipt.insert(END,'Iced_Latte:\t\t\t\t'+ E_Iced_Latte.get()+"\n")
    txtReceipt.insert(END,'Coffee:\t\t\t\t'+ E_Coffee.get()+"\n")
    txtReceipt.insert(END,'Cappuccin:\t\t\t\t'+ E_Cappuccin.get()+"\n")
    txtReceipt.insert(END,'Tea:\t\t\t\t'+ E_Tea.get()+"\n")
    txtReceipt.insert(END,'Cold_coffee:\t\t\t\t'+ E_Cold_coffee.get()+"\n")
    txtReceipt.insert(END,'Filter_coffee:\t\t\t\t'+ E_Filter_coffee.get()+"\n")
    txtReceipt.insert(END,'Coffee_cake:\t\t\t\t'+ E_Coffee_cake.get()+"\n")
    txtReceipt.insert(END,'Black_forest:\t\t\t\t'+ E_Black_forest.get()+"\n")
    txtReceipt.insert(END,'Cream_cake:\t\t\t\t'+ E_Cream_cake.get()+"\n")
    txtReceipt.insert(END,'Lagoos_cake:\t\t\t\t'+E_Lagoos_cake.get()+"\n")
    txtReceipt.insert(END,'Fruit_cake:\t\t\t\t'+ E_Fruit_cake.get()+"\n")
    txtReceipt.insert(END,'Chocolate_cake:\t\t\t\t'+ E_Chocolate_cake.get()+"\n")
    txtReceipt.insert(END,'Chocolava:\t\t\t\t'+ E_Chocolava.get()+"\n")
    txtReceipt.insert(END,'Bread_cake:\t\t\t\t'+ E_Bread_cake.get()+"\n")
    txtReceipt.insert(END,'Cost of Drinks:\t\t'+ CostofDrinks.get()+ '\t\tTax Paid:\t' + PaidTax.get() +"\n")
    txtReceipt.insert(END,'Cost of Cakes:\t\t'+ CostofCakes.get()+ '\t\tSubTotal:\t' +SubTotal.get() +"\n")
    txtReceipt.insert(END,'Service Charge:\t\t'+ ServiceCharge.get()+ '\t\tTotal Cost:\t' + TotalCost.get() +"\n")
   
#=========================================================================CHECKBOX==========================================================================

def chkbutton_value():
    if (var1.get() == 1):
        txtLatte.configure(state= NORMAL)
    elif var1.get()== 0:
            txtLatte.configure(state= DISABLED)
            E_Latte.set("0")
    if (var2.get() == 1):
        txtCoke.configure(state=NORMAL)
    elif var2.get()== 0:
            txtCoke.configure(state=DISABLED)
            E_Coke.set("0")
    if (var3.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
    elif var3.get()== 0:
            txtIced_Latte.configure(state=DISABLED)
            E_Iced_Latte.set("0")
    if (var4.get() == 1):
        txtCoffee.configure(state=NORMAL)
    elif var4.get()== 0:
            txtCoffee.configure(state=DISABLED)
            E_Coffee.set("0")
    if (var5.get() == 1):
        txtCappuccin.configure(state=NORMAL)
    elif var5.get()== 0:
            txtCappuccin.configure(state=DISABLED)
            E_Cappuccin.set("0")
    if (var6.get() == 1):
        txtTea.configure(state=NORMAL)
    elif var6.get()== 0:
            txtTea.configure(state=DISABLED)
            E_Tea.set("0")
    if (var7.get() == 1):
        txtCold_coffee.configure(state=NORMAL)
    elif var7.get()== 0:
            txtCold_coffee.configure(state=DISABLED)
            E_Cold_coffee.set("0")
    if (var8.get() == 1):
        txtFilter_coffee.configure(state=NORMAL)
    elif var8.get()==0:
            txtFilter_coffee.configure(state=DISABLED)
            E_Filter_coffee.set("0")
    if (var9.get() == 1):
        txtCoffee_cake.configure(state=NORMAL)
    elif var9.get()== 0:
            txtCoffee_cake.configure(state=DISABLED)
            E_Coffee_cake.set("0")
    if (var10.get() == 1):
        txtBlack_forest.configure(state=NORMAL)
    elif var10.get()== 0:
            txtBlack_forest.configure(state=DISABLED)
            E_Black_forest.set("0")
    if (var11.get() == 1):
        txtCream_cake.configure(state=NORMAL)
    elif var11.get()== 0:
            txtCream_cake.configure(state=DISABLED)
            E_Cream_cake.set("0")
    if (var12.get() == 1):
        txtLagoos_cake.configure(state=NORMAL)
    elif var12.get()== 0:
            txtLagoos_cake.configure(state=DISABLED)
            E_Lagoos_cake.set("0")
    if (var13.get() == 1):
        txtFruit_cake.configure(state=NORMAL)
    elif var13.get()== 0:
            txtFruit_cake.configure(state=DISABLED)
            E_Fruit_cake.set("0")
    if (var14.get() == 1):
        txtChocolate_cake.configure(state=NORMAL)
    elif var14.get()== 0:
            txtChocolate_cake.configure(state=DISABLED)
            E_Chocolate_cake.set("0")
    if (var15.get() == 1):
        txtChocolava.configure(state=NORMAL)
    elif var15.get()== 0:
            txtChocolava.configure(state=DISABLED)
            E_Chocolava.set("0")
    if (var16.get() == 1):
        txtBread_cake.configure(state=NORMAL)
    elif var16.get()== 0:
            txtBread_cake.configure(state=DISABLED)
            E_Bread_cake.set("0")
  
	
#==========================================================VARIABLES===============================================================================
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()


E_Latte=StringVar()
E_Coke=StringVar()
E_Iced_Latte=StringVar()
E_Coffee=StringVar()
E_Cappuccin=StringVar()
E_Tea=StringVar()
E_Cold_coffee=StringVar()
E_Filter_coffee=StringVar()

E_Coffee_cake=StringVar()
E_Black_forest=StringVar()
E_Cream_cake=StringVar()
E_Lagoos_cake=StringVar()
E_Fruit_cake=StringVar()
E_Chocolate_cake=StringVar()
E_Chocolava=StringVar()
E_Bread_cake=StringVar()


E_Latte.set("0")
E_Coke.set("0")
E_Iced_Latte.set("0")
E_Coffee.set("0")
E_Cappuccin.set("0")
E_Tea.set("0")
E_Cold_coffee.set("0")
E_Filter_coffee.set("0")

E_Coffee_cake.set("0")
E_Black_forest.set("0")
E_Cream_cake.set("0")
E_Lagoos_cake.set("0")
E_Fruit_cake.set("0")
E_Chocolate_cake.set("0")
E_Chocolava.set("0")
E_Bread_cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

#=================================================DRINKS===================================================================================================================

Latte = Checkbutton(f1aa, text="  Latte \t\t", variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Coke = Checkbutton(f1aa, text="  Coke \t\t", variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Iced_Latte = Checkbutton(f1aa, text="  Iced_Latte \t\t", variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Coffee = Checkbutton(f1aa, text="  Coffee \t\t", variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Cappuccino = Checkbutton(f1aa, text="  Cappuccino \t\t", variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Tea = Checkbutton(f1aa, text="  Tea \t\t", variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Cold_coffee = Checkbutton(f1aa, text="  Cold_coffee \t\t", variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Filter_coffee = Checkbutton(f1aa, text="  Filter_coffee \t\t", variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#====================================================CAKES======================================================================================================================

Coffee_cake = Checkbutton(f1ab, text=" Coffee_cake \t\t\t", variable=var9, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Black_forest = Checkbutton(f1ab, text=" Black_forest \t\t\t", variable=var10, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Cream_cake = Checkbutton(f1ab, text=" Cream_cake \t\t\t", variable=var11, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Lagoos_cake = Checkbutton(f1ab, text=" Lagoos_cake \t\t\t", variable=var12, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

Fruit_cake = Checkbutton(f1ab, text=" Fruit_cake \t\t\t", variable=var13, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Chocolate_cake = Checkbutton(f1ab, text=" Chocolate_cake \t\t\t", variable=var14, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Chocolava = Checkbutton(f1ab, text=" Chocolava \t\t\t", variable=var15, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Bread_cake = Checkbutton(f1ab, text=" Bread_cake \t\t\t", variable=var16, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)


#=====================================================ENTER WIDGE DRINKS================================================================================================================

txtLatte = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Latte, state=DISABLED)
txtLatte.grid(row=0,column=1)

txtCoke = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coke, state=DISABLED)
txtCoke.grid(row=1,column=1)

txtIced_Latte = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Latte,state=DISABLED)
txtIced_Latte.grid(row=2,column=1)

txtCoffee = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee,state=DISABLED)
txtCoffee.grid(row=3,column=1)

txtCappuccin = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cappuccin,state=DISABLED)
txtCappuccin.grid(row=4,column=1)

txtTea = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Tea,state=DISABLED)
txtTea.grid(row=5,column=1)

txtCold_coffee = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cold_coffee,state=DISABLED)
txtCold_coffee.grid(row=6,column=1)

txtFilter_coffee = Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Filter_coffee,state=DISABLED)
txtFilter_coffee.grid(row=7,column=1)



#=====================================================ENTER WIDGE CAKES========================================================================================

txtCoffee_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee_cake,state=DISABLED)
txtCoffee_cake.grid(row=0,column=1)

txtBlack_forest = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Black_forest,state=DISABLED)
txtBlack_forest.grid(row=1,column=1)

txtCream_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cream_cake,state=DISABLED)
txtCream_cake.grid(row=2,column=1)

txtLagoos_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lagoos_cake,state=DISABLED)
txtLagoos_cake.grid(row=3,column=1)

txtFruit_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Fruit_cake,state=DISABLED)
txtFruit_cake.grid(row=4,column=1)

txtChocolate_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolate_cake,state=DISABLED)
txtChocolate_cake.grid(row=5,column=1)

txtChocolava = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Chocolava,state=DISABLED)
txtChocolava.grid(row=6,column=1)

txtBread_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify='left',textvariable=E_Bread_cake,state=DISABLED)
txtBread_cake.grid(row=7,column=1)

#===========================================================INFORMATION==========================================================================================

lblReceipt = Label(ft2,font=('arial',16,'bold'),text="Get Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt = Text(ft2,font=('arial',11,'bold'),bd=8,width=59,height=22,bg="white")
txtReceipt.grid(row=1,column=0)


#=========================================================ITEM COST INFORMATION=============================================================================

lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="Cost of Drinks",bd=8)
lblCostofDrinks.grid(row=2,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=CostofDrinks)
txtCostofDrinks.grid(row=2,column=1)

lblCostofCakes=Label(f2aa,font=('arial',16,'bold'),text="Cost of Cakes",bd=8)
lblCostofCakes.grid(row=3,column=0,sticky=W)
txtCostofCakes=Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=CostofCakes)
txtCostofCakes.grid(row=3,column=1)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge",bd=8)
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
txtServiceCharge.grid(row=4,column=1)


#=========================================================PAYMENT INFORMATION===============================================================================

lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="Tax paid",bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=PaidTax)
txtPaidTax.grid(row=2,column=1,sticky=W)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total",bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1,sticky=W)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text="Total Cost",bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1,sticky=W)

#============================================================BUTTONS=============================================================================================

btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",command=CostofItems).grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Receipt",command=Receipt).grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Reset",command=Reset).grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=qExit).grid(row=0,column=3)



root.mainloop()

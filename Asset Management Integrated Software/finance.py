from tkinter import *

import os
path = os.path.dirname(os.path.realpath(__file__))

total = 40

q = [

"How would your best friend describe you as a risk taker?",
"You are on a TV game show and can choose one of the following. Which would you take?",
"You have just finished saving for a “once-in-a-lifetime” vacation. Three weeks before you plan to leave,you lose your job. You would:",
"How would you respond to the following statement? “It’s hard for me to pass up a bargain”",
"If you unexpectedly received $20,000 to invest, what would you do?",
"In terms of experience, how comfortable are you investing in stocks or stock mutual funds?",
"Which situation would make you the happiest?",
"When you think of the word “risk” which of the following words comes to mind first?",
"You inherit a mortgage-free house worth $80,000. The house is in a nice neighborhood, and you believe that it\n should increase in value faster than inflation. Unfortunately, the house needs repairs.\nIf rented today, the house would bring in $600 monthly, but if updates and repairs were made,\n the house would rent for $800 per month. To finance the repairs you’ll need to take out a mortgage on the property.\n You would:",
"In your opinion, is it more important to be protected from rising consumer prices (inflation) or \n to maintain the safety of your money from loss or theft?",
"After your first year at a small fast growing company, you are offered the following bonus choices. Which one would you choose?",
"Some experts are predicting prices of assets such as gold, jewels, collectibles, and real estate (hard assets) to increase in value;\nbond prices may fall, however, experts tend to agree that government bonds are relatively safe.\nMost of your investment assets are now in high interest government bonds.\nWhat would you do?",
"Assume you are going to buy a home in the next few weeks. Your strategy would probably be:",
"Given the best and worst case returns of the four investment choices below, which would you prefer?",
"Assume that you are applying for a mortgage. Interest rates have been coming down over the past few months. There’s the possibility\nthat this trend will continue. But some economists are predicting rates to increase. You have the option of locking in your\nmortgage interest rate or letting it float. If you lock in you will get the current rate, even if interest rates go up. If the rates go down,\nyou’ll have to settle for the higher locked in rate. You plan to live in the house for at least three years. What would you do?",
"In addition to whatever you own, you have been given $1,000. You are now asked to choose between:",
"In addition to whatever you own, you have been given $2,000. You are now asked to choose between:",
"Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL the\nmoney in ONE of the following choices. Which one would you select?",
"If you had to invest $20,000, which of the following investment choices would you find most appealing?",
"Your best friend, an experienced geologist, is putting together a group of investors to\nfund an exploratory gold mining venture. The venture could pay back 50 to 100 times the investment if\nsuccessful. If the mine is a bust, the entire investment is worthless. Your friend estimates the chance of\nsuccess is only 20%. If you had the money, how much would you invest?"
]


a0 = ["A real gambler","Willing to take risks after completing adequate research"," Cautious","A real risk avoider"]
a1 = ["$1,000 in cash","A 50% chance at winning $5,000"," A 25% chance at winning $10,000","A 5% chance at winning $100,000"]
a2 = [" Cancel the vacation","Take a much more modest vacation","Go as scheduled, reasoning that you need the time to prepare for a job search","Extend your vacation, because this might be your last chance to go first-class"]
a3 = ["Very true"," Sometimes true","Not at all true"]
a4 = ["Deposit it in a bank account, money market account, or an insured CD", "Invest it in safe high quality bonds or bond mutual funds", "Invest it in stocks or stock mutual funds"]
a5 = ["Not at all comfortable", "Somewhat comfortable", "Very comfortable"]
a6 = ["You win $50,000 in a publisher’s contest","You inherit $50,000 from a rich relative", "You earn $50,000 by risking $1,000 in the options market", "Any of the above—after all, you’re happy with the $50,000"]
a7 = ["Loss", "Uncertainty", "Opportunity", "Thrill"]
a8 = [" Sell the house", "Rent the house as is", "Remodel and update the house, and then rent it"]
a9 = ["Much more important to secure the safety of my money" , "Much more important to be protected from rising prices (inflation)"]
a10 = ["A five year employment contract" , "A $25,000 bonus", "Stock in the company currently worth $25,000 with the hope of selling out later at a large profit"]
a11 = ["Hold the bonds", "Sell the bonds, put half the proceeds into money market accounts, and the other half into hard assets", "Sell the bonds and put the total proceeds into hard assets", "Sell the bonds, put all the money into hard assets, and borrow additional money to buy more"]
a12 = ["To buy an affordable house where you can make monthly payments comfortably", "To stretch a bit financially to buy the house you really want", "To buy the most expensive house you can qualify for", "To borrow money from friends and relatives so you can qualify for a bigger mortgage"]
a13 = [" $200 gain best case; $0 gain/loss worst case", "$800 gain best case; $200 loss worst case", "$2,600 gain best case; $800 loss worst case", "$4,800 gain best case; $2,400 loss worst case"]
a14 = ["Definitely lock in the interest rate", "Probably lock in the interest rate", "Probably let the interest rate float", "Definitely let the interest rate float"]
a15 = ["A sure gain of $500", "A 50% chance to gain $1,000 and a 50% chance to gain nothing"]
a16 = [" A sure loss of $500", "A 50% chance to lose $1,000 and a 50% chance to lose nothing"]
a17 = [" A savings account or money market mutual fund", "A mutual fund that owns stocks and bonds", "A portfolio of 15 common stocks", "Commodities like gold, silver, and oil"]
a18 = ["60% in low-risk investments 30% in medium-risk investments 10% in high-risk investments", "30% in low-risk investments 40% in medium-risk investments 30% in high-risk investments", "10% in low-risk investments 40% in medium-risk investments 50% in high-risk investments"]
a19 = ["Nothing", "One month’s salary" , "Three month’s salary", "Six month’s salary"]

import csv

def Max(File, Amount):
    with open(File, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    X = [row[1] for row in data]

    X.pop(0)

    Y = [float(i) for i in X]
    
    Profit = []
    ProfitPercentage = []
    
    def stockBuySell(price, n):
        if (n == 1): 
            return
    
        i = 0
        sum = 0
        total = 0
        
        while (i < (n - 1)):
            
            while ((i < (n - 1)) and (price[i + 1] <= price[i])):
                i += 1
                
            if (i == n - 1): 
                break
            
            buy = i 
            i += 1
            
            while ((i < n) and (price[i] >= price[i - 1])): 
                i += 1
                
            sell = i - 1
            sum = (price[sell] - price[buy])
            total = total + sum
            
            #print("Buy on day: ",buy,"\t", 
                #"Sell on day: ",sell)
            Profit.append(total)
            #print(price[buy])
            temp =1 + (sum/price[buy])
            ProfitPercentage.append(temp)
            
    price = Y
    n = len(price)

    stockBuySell(price, n)
    #print(Profit)
    #print(ProfitPercentage)
    

    Final = Amount
    for i in range(0, len(ProfitPercentage)):
        Final = Final * (ProfitPercentage[i])
    
    return(Final)

import csv

Tn = '7 days to 14 days'

def fd(A, B, T):
    
    with open(path + r'\output.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        banks = []
        tenures = []
        interests = []
        for row in readCSV:
            bank = row[0]
            tenure = row[1]
            interest = row[2]
            banks.append(bank)
            tenures.append(tenure)
            interests.append(interest)
    global fdamt       
    amount_request = fdamt
    PERCENTAGE = 100
    
    for i in range(1, len(banks)):
        bnk = [i for i in banks if B in i]
        tnr = [j for j in tenures if T in j]
        if banks[i] in bnk and tenures[i] in tnr:
            b_n = banks[i]
            t_n = tenures[i]
            perc_val = float(interests[i].rstrip("%"))
            cal = round((perc_val*amount_request)/ PERCENTAGE, 2)
            total = amount_request + cal
            
    return(total)

def bnext():

   global windows
   windows = Toplevel(root)
   windows.title("Question 1")
   windows.geometry("900x200")
   root.withdraw()

   lbl1 = Label(windows,text = q[0],font = ('arial',10,'bold')).pack(side = TOP)
   cb1 = Radiobutton(windows, text=a0[0], value=4,variable = v0).pack(side=BOTTOM)
   cb2 = Radiobutton(windows, text=a0[1], value=3,variable = v0).pack(side=BOTTOM)
   cb3 = Radiobutton(windows, text=a0[2], value=2,variable = v0).pack(side=BOTTOM)
   cb4 = Radiobutton(windows, text=a0[3], value=1,variable = v0).pack(side=BOTTOM)
   btn1 = Button(windows,text = "next",font = ('arial',12,'bold'),fg = 'blue', command = bnext2).pack(side = RIGHT)
   btn2 = Button(windows,text = "back",font = ('arial',12,'bold'),fg = 'blue', command = bback).pack(side = LEFT)
   windows.mainloop()

def bnext2():

   global windows3
   windows3 = Toplevel(windows)
   windows3.title("Question 2")
   windows3.geometry("900x200")
   windows.withdraw()

   lbl2 = Label(windows3, text=q[1], font=('arial', 10, 'bold')).pack(side=TOP)
   cb5 = Radiobutton(windows3, text=a1[0], value=1,variable = v1).pack(side=BOTTOM)
   cb6 = Radiobutton(windows3, text=a1[1], value=2,variable = v1).pack(side=BOTTOM)
   cb7 = Radiobutton(windows3, text=a1[2], value=3,variable = v1).pack(side=BOTTOM)
   cb8 = Radiobutton(windows3, text=a1[3], value=4,variable = v1).pack(side=BOTTOM)

   btn3 = Button(windows3,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext3).pack(side=RIGHT)
   btn4 = Button(windows3,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback2).pack(side=LEFT)
   windows3.mainloop()

def bnext3():

   global windows4
   windows4 = Toplevel(windows3)
   windows4.title("Question 3")
   windows4.geometry("900x200")
   windows3.withdraw()

   lbl2 = Label(windows4, text=q[2], font=('arial', 10, 'bold')).pack(side=TOP)
   cb9 = Radiobutton(windows4, text=a2[0], value=1,variable = v2).pack(side=BOTTOM)
   cb10 = Radiobutton(windows4, text=a2[1], value=2,variable = v2).pack(side=BOTTOM)
   cb11 = Radiobutton(windows4, text=a2[2], value=3,variable = v2).pack(side=BOTTOM)
   cb12 = Radiobutton(windows4, text=a2[3], value=4,variable = v2).pack(side=BOTTOM)

   btn5 = Button(windows4,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext4).pack(side=RIGHT)
   btn6 = Button(windows4,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback3).pack(side=LEFT)
   windows4.mainloop()

def bnext4():

   global windows5
   windows5 = Toplevel(windows4)
   windows5.title("Question 4")
   windows5.geometry("900x200")
   windows4.withdraw()

   lbl2 = Label(windows5, text=q[3], font=('arial', 10, 'bold')).pack(side=TOP)
   cb13 = Radiobutton(windows5, text=a3[0], value=1,variable = v3).pack(side=BOTTOM)
   cb14 = Radiobutton(windows5, text=a3[1], value=2,variable = v3).pack(side=BOTTOM)
   cb15 = Radiobutton(windows5, text=a3[2], value=3,variable = v3).pack(side=BOTTOM)

   btn7 = Button(windows5,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext5).pack(side=RIGHT)
   btn8 = Button(windows5,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback4).pack(side=LEFT)

   windows5.mainloop()

def bnext5():

   global windows6
   windows6 = Toplevel(windows5)
   windows6.title("Question 5")
   windows6.geometry("900x200")
   windows5.withdraw()

   lbl2 = Label(windows6, text=q[4], font=('arial', 10, 'bold')).pack(side=TOP)
   cb16 = Radiobutton(windows6, text=a4[0], value=1,variable = v4).pack(side=BOTTOM)
   cb17 = Radiobutton(windows6, text=a4[1], value=2,variable = v4).pack(side=BOTTOM)
   cb18 = Radiobutton(windows6, text=a4[2], value=3,variable = v4).pack(side=BOTTOM)

   btn9 = Button(windows6,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext6).pack(side=RIGHT)
   btn10 = Button(windows6,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback5).pack(side=LEFT)

   windows6.mainloop()

def bnext6():

   global windows7
   windows7 = Toplevel(windows6)
   windows7.title("Question 6")
   windows7.geometry("900x200")
   windows6.withdraw()

   lbl2 = Label(windows7, text=q[5], font=('arial', 10, 'bold')).pack(side=TOP)
   cb19 = Radiobutton(windows7, text=a5[0], value=1,variable = v5).pack(side=BOTTOM)
   cb20 = Radiobutton(windows7, text=a5[1], value=2,variable = v5).pack(side=BOTTOM)
   cb21 = Radiobutton(windows7, text=a5[2], value=3,variable = v5).pack(side=BOTTOM)

   btn11 = Button(windows7,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext7).pack(side=RIGHT)
   btn12 = Button(windows7,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback6).pack(side=LEFT)

   windows7.mainloop()

def bnext7():

   global windows8
   windows8 = Toplevel(windows7)
   windows8.title("Question 7")
   windows8.geometry("900x200")
   windows7.withdraw()

   lbl2 = Label(windows8, text=q[6], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows8, text=a6[0], value=2,variable = v6).pack(side=BOTTOM)
   cb23 = Radiobutton(windows8, text=a6[1], value=1,variable = v6).pack(side=BOTTOM)
   cb24 = Radiobutton(windows8, text=a6[2], value=3,variable = v6).pack(side=BOTTOM)
   cb25 = Radiobutton(windows8, text=a6[3], value=1,variable = v6).pack(side=BOTTOM) 

   btn13 = Button(windows8,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext8).pack(side=RIGHT)
   btn14 = Button(windows8,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback7).pack(side=LEFT)

   windows8.mainloop()

def bnext8():

   global windows9
   windows9 = Toplevel(windows8)
   windows9.title("Question 8")
   windows9.geometry("900x200")
   windows8.withdraw()

   lbl2 = Label(windows9, text=q[7], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows9, text=a7[0], value=1,variable = v7).pack(side=BOTTOM)
   cb23 = Radiobutton(windows9, text=a7[1], value=2,variable = v7).pack(side=BOTTOM)
   cb24 = Radiobutton(windows9, text=a7[2], value=3,variable = v7).pack(side=BOTTOM)
   cb25 = Radiobutton(windows9, text=a7[3], value=4,variable = v7).pack(side=BOTTOM) 

   btn13 = Button(windows9,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext9).pack(side=RIGHT)
   btn14 = Button(windows9,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback8).pack(side=LEFT)

   windows9.mainloop()

def bnext9():

   global windows10
   windows10 = Toplevel(windows9)
   windows10.title("Question 9")
   windows10.geometry("900x200")
   windows9.withdraw()

   lbl2 = Label(windows10, text=q[8], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows10, text=a8[0], value=1,variable = v8).pack(side=BOTTOM)
   cb23 = Radiobutton(windows10, text=a8[1], value=2,variable = v8).pack(side=BOTTOM)
   cb24 = Radiobutton(windows10, text=a8[2], value=3,variable = v8).pack(side=BOTTOM)

   btn13 = Button(windows10,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext10).pack(side=RIGHT)
   btn14 = Button(windows10,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback9).pack(side=LEFT)

   windows10.mainloop()

def bnext10():

   global windows11
   windows11 = Toplevel(windows10)
   windows11.title("Question 10/20")
   windows11.geometry("900x200")
   windows10.withdraw()

   lbl2 = Label(windows11, text=q[9], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows11, text=a9[0], value=1,variable = v9).pack(side=BOTTOM)
   cb23 = Radiobutton(windows11, text=a9[1], value=3,variable = v9).pack(side=BOTTOM)

   btn13 = Button(windows11,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext11).pack(side=RIGHT)
   btn14 = Button(windows11,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback10).pack(side=LEFT)

   windows11.mainloop()

def bnext11():

   global windows12
   windows12 = Toplevel(windows11)
   windows12.title("Question 11/20")
   windows12.geometry("900x200")
   windows11.withdraw()

   lbl2 = Label(windows12, text=q[10], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows12, text=a10[0], value=1,variable = v10).pack(side=BOTTOM)
   cb23 = Radiobutton(windows12, text=a10[1], value=2,variable = v10).pack(side=BOTTOM)
   cb24 = Radiobutton(windows12, text=a10[2], value=3,variable = v10).pack(side=BOTTOM)

   btn13 = Button(windows12,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext12).pack(side=RIGHT)
   btn14 = Button(windows12,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback11).pack(side=LEFT)

   windows12.mainloop()

def bnext12():

   global windows13
   windows13 = Toplevel(windows12)
   windows13.title("Question 12/20")
   windows13.geometry("900x200")
   windows12.withdraw()

   lbl2 = Label(windows13, text=q[11], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows13, text=a11[0], value=1,variable = v11).pack(side=BOTTOM)
   cb23 = Radiobutton(windows13, text=a11[1], value=2,variable = v11).pack(side=BOTTOM)
   cb24 = Radiobutton(windows13, text=a11[2], value=3,variable = v11).pack(side=BOTTOM)
   cb25 = Radiobutton(windows13, text=a11[3], value=4,variable = v11).pack(side=BOTTOM) 

   btn13 = Button(windows13,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext13).pack(side=RIGHT)
   btn14 = Button(windows13,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback12).pack(side=LEFT)

   windows13.mainloop()

def bnext13():

   global windows14
   windows14 = Toplevel(windows13)
   windows14.title("Question 13/20")
   windows14.geometry("900x200")
   windows13.withdraw()

   lbl2 = Label(windows14, text=q[12], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows14, text=a12[0], value=1,variable = v12).pack(side=BOTTOM)
   cb23 = Radiobutton(windows14, text=a12[1], value=2,variable = v12).pack(side=BOTTOM)
   cb24 = Radiobutton(windows14, text=a12[2], value=3,variable = v12).pack(side=BOTTOM)
   cb25 = Radiobutton(windows14, text=a12[3], value=4,variable = v12).pack(side=BOTTOM) 
 

   btn13 = Button(windows14,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext14).pack(side=RIGHT)
   btn14 = Button(windows14,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback13).pack(side=LEFT)

   windows14.mainloop()

def bnext14():

   global windows15
   windows15 = Toplevel(windows14)
   windows15.title("Question 14/20")
   windows15.geometry("900x200")
   windows14.withdraw()

   lbl2 = Label(windows15, text=q[13], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows15, text=a13[0], value=1,variable = v13).pack(side=BOTTOM)
   cb23 = Radiobutton(windows15, text=a13[1], value=2,variable = v13).pack(side=BOTTOM)
   cb24 = Radiobutton(windows15, text=a13[2], value=3,variable = v13).pack(side=BOTTOM)
   cb25 = Radiobutton(windows15, text=a13[3], value=4,variable = v13).pack(side=BOTTOM) 
 
   btn13 = Button(windows15,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext15).pack(side=RIGHT)
   btn14 = Button(windows15,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback14).pack(side=LEFT)

   windows15.mainloop()

def bnext15():

   global windows16
   windows16 = Toplevel(windows15)
   windows16.title("Question 15/20")
   windows16.geometry("900x200")
   windows15.withdraw()

   lbl2 = Label(windows16, text=q[14], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows16, text=a14[0], value=1,variable = v14).pack(side=BOTTOM)
   cb23 = Radiobutton(windows16, text=a14[1], value=2,variable = v14).pack(side=BOTTOM)
   cb24 = Radiobutton(windows16, text=a14[2], value=2,variable = v14).pack(side=BOTTOM)
   cb25 = Radiobutton(windows16, text=a14[3], value=3,variable = v14).pack(side=BOTTOM) 
 
   btn13 = Button(windows16,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext16).pack(side=RIGHT)
   btn14 = Button(windows16,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback15).pack(side=LEFT)

   windows16.mainloop()

def bnext16():

   global windows17
   windows17 = Toplevel(windows16)
   windows17.title("Question 16/20")
   windows17.geometry("900x200")
   windows16.withdraw()

   lbl2 = Label(windows17, text=q[15], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows17, text=a15[0], value=1,variable = v15).pack(side=BOTTOM)
   cb23 = Radiobutton(windows17, text=a15[1], value=3,variable = v15).pack(side=BOTTOM)
   
   btn13 = Button(windows17,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext17).pack(side=RIGHT)
   btn14 = Button(windows17,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback16).pack(side=LEFT)

   windows17.mainloop()
   
def bnext17():

   global windows18
   windows18 = Toplevel(windows17)
   windows18.title("Question 17/20")
   windows18.geometry("900x200")
   windows17.withdraw()

   lbl2 = Label(windows18, text=q[16], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows18, text=a16[0], value=1,variable = v16).pack(side=BOTTOM)
   cb23 = Radiobutton(windows18, text=a16[1], value=3,variable = v16).pack(side=BOTTOM)
   
   btn13 = Button(windows18,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext18).pack(side=RIGHT)
   btn14 = Button(windows18,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback17).pack(side=LEFT)

   windows18.mainloop()

def bnext18():

   global windows19
   windows19 = Toplevel(windows18)
   windows19.title("Question 18/20")
   windows19.geometry("900x200")
   windows18.withdraw()

   lbl2 = Label(windows19, text=q[17], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows19, text=a17[0], value=1,variable = v17).pack(side=BOTTOM)
   cb23 = Radiobutton(windows19, text=a17[1], value=2,variable = v17).pack(side=BOTTOM)
   cb24 = Radiobutton(windows19, text=a17[2], value=3,variable = v17).pack(side=BOTTOM)
   cb25 = Radiobutton(windows19, text=a17[3], value=4,variable = v17).pack(side=BOTTOM) 
 
   btn13 = Button(windows19,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext19).pack(side=RIGHT)
   btn14 = Button(windows19,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback18).pack(side=LEFT)

   windows19.mainloop()

def bnext19():

   global windows20
   windows20 = Toplevel(windows19)
   windows20.title("Question 19/20")
   windows20.geometry("900x200")
   windows19.withdraw()

   lbl2 = Label(windows20, text=q[18], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows20, text=a18[0], value=1,variable = v18).pack(side=BOTTOM)
   cb23 = Radiobutton(windows20, text=a18[1], value=2,variable = v18).pack(side=BOTTOM)
   cb24 = Radiobutton(windows20, text=a18[2], value=3,variable = v18).pack(side=BOTTOM)
   
   btn13 = Button(windows20,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext20).pack(side=RIGHT)
   btn14 = Button(windows20,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback19).pack(side=LEFT)

   windows20.mainloop()

def bnext20():

   global windows21
   windows21 = Toplevel(windows20)
   windows21.title("Question 20/20")
   windows21.geometry("900x200")
   windows20.withdraw()

   lbl2 = Label(windows21, text=q[19], font=('arial', 10, 'bold')).pack(side=TOP)
   cb22 = Radiobutton(windows21, text=a19[0], value=1,variable = v19,command = checked).pack(side=BOTTOM)
   cb23 = Radiobutton(windows21, text=a19[1], value=2,variable = v19,command = checked).pack(side=BOTTOM)
   cb24 = Radiobutton(windows21, text=a19[2], value=3,variable = v19,command = checked).pack(side=BOTTOM)
   cb25 = Radiobutton(windows21, text=a19[3], value=4,variable = v19,command = checked).pack(side=BOTTOM) 
 
   btn13 = Button(windows21,text = "next",font = ('arial',12,'bold'),fg = 'blue',command = bnext21).pack(side=RIGHT)
   btn14 = Button(windows21,text = "back",font = ('arial',12,'bold'),fg = 'blue',command = bback20).pack(side=LEFT)

   windows21.mainloop()

def bnext21():

   global windows22
   windows22 = Toplevel(root)
   windows22.title("Final Result")
   windows22.geometry("900x200")
   windows21.withdraw()
   btn11 = Button(windows22, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback21).pack(side=LEFT)
   bnext = Button(windows22, text="Next", font=('arial', 12, 'bold'), fg='blue', command=bnext22).pack(side=BOTTOM)
   bf = Label(windows22,text = "Your risk analysis score is " + str(total),font = ("arial",16,"bold"),fg = "red")
   bf.pack(side = TOP)

   windows22.mainloop()

def bnext22():

   global windows23
   windows23 = Toplevel(windows22)
   windows23.title("Details")
   windows23.geometry("900x200")
   windows22.withdraw()
   btn11 = Button(windows23, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback22).pack(side=BOTTOM)
   bnext = Button(windows23, text="Next", font=('arial', 12, 'bold'), fg='blue', command=bnext23).pack(side=BOTTOM)
   bf = Label(windows23,text = "Please enter your age:",font = ("arial",14),fg = "blue").place(x = 5, y = 10)
   bf1 = Label(windows23,text = "Please enter time to maturity:",font = ("arial",14),fg = "blue").place(x = 5, y = 50)
   bf2 = Label(windows23,text = "Enter your savings amount(in Rs):",font = ("arial",14),fg = "blue").place(x = 5, y = 100)
   e1 = Entry(windows23, bd = 2, textvariable = Age)
   e2 = Entry(windows23, bd = 2, textvariable = Mat)
   e3 = Entry(windows23, bd = 7, textvariable = Sav)
   e1.place(x = 300, y = 20)
   e2.place(x = 300, y = 60) 
   e3.place(x = 300, y = 110)

   windows23.mainloop()

def bnext23():

   global windows24
   windows24 = Toplevel(windows23)
   windows24.title("Details")
   windows24.geometry("900x600")
   windows23.withdraw()
   btn11 = Button(windows24, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback23).pack(side=BOTTOM)
   global riskclass
   riskclass = ""
   
   if total > 55:
       riskclass = 'Aggressive'
       myimage = PhotoImage(file="D:\Study\Btech proj\gga.png")
       mylabel = Label(windows24, image=myimage).place(x = 30, y = 40)
   elif total > 30 and total < 56:
       riskclass = 'Moderately Aggressive'
       myimage = PhotoImage(file='D:\Study\Btech proj\mod agg.png')
       mylabel = Label(windows24, image=myimage).place(x = 30, y = 40)
   else:
       riskclass = 'Conservative'
       myimage = PhotoImage(file='D:\Study\Btech proj\conservative.png')
       mylabel = Label(windows24, image=myimage).place(x = 30, y = 40)
   bf = Label(windows24,text = "Your risk class is: " + riskclass,font = ("arial",16),fg = "blue").place(x = 5, y = 10) 
   bnext = Button(windows24, text="Next", font=('arial', 12, 'bold'), fg='blue', command=bnext24).pack(side=BOTTOM)    
   windows24.mainloop()

def bnext24():

   global windows25
   windows25 = Toplevel(windows24)
   windows25.title("Details")
   windows25.geometry("900x550")
   windows24.withdraw()
   btn11 = Button(windows25, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback24).pack(side=BOTTOM)
   if riskclass == 'Aggressive':
        stockperc = 0.69
        fdperc = 0.23
        cashperc = 0.03
        commperc = 0.05
   if riskclass == 'Moderately Aggressive':
        stockperc = 0.52
        fdperc = 0.40
        cashperc = 0.06
        commperc = 0.02
   if riskclass == 'Conservative':
        stockperc = 0.2
        fdperc = 0.7
        cashperc = 0.09
        commperc = 0.01     
   s = Sav.get() #savings
   global stockamt
   global fdamt
   global cash
   global commamt
   stockamt = s * stockperc
   fdamt = s * fdperc 
   cash = s * cashperc
   commamt = s * commperc
   bf = Label(windows25,text = "Money into stocks: Rs " + str(stockamt),font = ("arial",16),fg = "blue").place(x = 5, y = 10)
   bf1 = Label(windows25,text = "Money into FDs: Rs " + str(fdamt),font = ("arial",16),fg = "blue").place(x = 5, y = 50)
   bf2 = Label(windows25,text = "Money as cash: Rs " + str(cash),font = ("arial",16),fg = "blue").place(x = 5, y = 100)
   bf3 = Label(windows25,text = "Money into commodities: Rs " + str(commamt),font = ("arial",16),fg = "blue").place(x = 5, y = 150)
   bf4 = Label(windows25,text = "Do you wish to change the breakup?" ,font = ("arial",16),fg = "blue").place(x = 5, y = 200)
   bnext = Button(windows25, text="Yes", font=('arial', 12, 'bold'), fg='green', command=bnextyes).pack(side=LEFT)
   bnext = Button(windows25, text="No", font=('arial', 12, 'bold'), fg='red', command=bnext25).pack(side=RIGHT)    
   windows25.mainloop()

def bnextyes():

   global windows100
   windows100 = Toplevel(windows25)
   windows100.title("Details")
   windows100.geometry("900x550")
   windows25.withdraw()
   global changemade
   changemade = 1

   bf = Label(windows100,text = "Money into stocks: Rs ",font = ("arial",14),fg = "blue").place(x = 5, y = 10)
   bf1 = Label(windows100,text = "Money into FDs: Rs ",font = ("arial",14),fg = "blue").place(x = 5, y = 50)
   bf2 = Label(windows100,text = "Money into commodities: Rs ",font = ("arial",14),fg = "blue").place(x = 5, y = 100)
   bf3 = Label(windows100,text = "Money into cash: Rs ",font = ("arial",14),fg = "blue").place(x = 5, y = 150)

   e1 = Entry(windows100, bd = 2, textvariable = stockch)
   e2 = Entry(windows100, bd = 2, textvariable = fdch)
   e3 = Entry(windows100, bd = 7, textvariable = commch)
   e4 = Entry(windows100, bd = 7, textvariable = cashch)
   

   e1.place(x = 300, y = 20)
   e2.place(x = 300, y = 60) 
   e3.place(x = 300, y = 110)
   e4.place(x = 300, y = 155)

   bnext = Button(windows100, text="Next", font=('arial', 12, 'bold'), fg='red', command=bnext25).pack(side=BOTTOM)    
   windows100.mainloop()

def bnext25():

   global windows26
   windows26 = Toplevel(windows24)
   windows26.title("Stocks and Commodities Prediction")
   windows26.geometry("800x450")
   windows25.withdraw()
   global stockamt
   global fdamt 
   global cash
   global commamt
   global changemade
   if changemade == 1:
       windows100.withdraw()
       stockamt = stockch.get()
       fdamt = fdch.get()
       commamt = commch.get()
       cash = cashch.get()
   btn11 = Button(windows26, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback25).pack(side=BOTTOM)

   HDFC =  Max(path + r"\HDFCNIFETF.NS.csv", stockamt)
   m50 = Max(path + r"\M50.BO.csv", stockamt)
   m100 =  Max(path + r"\M100.BO.csv", stockamt)
   fbse = Max(path + r"\SETFBSE100.BO.csv", stockamt)
   nifbk = Max(path + r"\SETFNIFBK.NS.csv", stockamt)
   global stockmax
   stockmax = max(HDFC, m50, m100, fbse, nifbk)
   
   bf1 = Label(windows26,text = "Amount invested in Stocks = " + str(stockamt),font = ("arial",16),fg = "blue").place(x = 5, y = 10)
   
   if HDFC > stockamt:       
        bf = Label(windows26,text = "HDFC returns: " + str(HDFC),font = ("arial",16),fg = "green").place(x = 5, y = 40)
   else:
       bf = Label(windows26,text = "HDFC returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 40)
   if m50 > stockamt:
        bf1 = Label(windows26,text = "M50 returns:   " + str(m50),font = ("arial",16),fg = "green").place(x = 5, y = 70)
   else:
        bf1 = Label(windows26,text = "M50 returns:   Not profitable",font = ("arial",16),fg = "red").place(x = 5, y = 70)
   if m100 > stockamt:
       bf2 = Label(windows26,text = "M100 returns: " + str(m100),font = ("arial",16),fg = "green").place(x = 5, y = 100)
   else:
        bf2 = Label(windows26,text = "M100 returns: Not profitable",font = ("arial",16),fg = "red").place(x = 5, y = 100)
   if fbse > stockamt:
       bf3 = Label(windows26,text = "SETFBSE returns: " + str(fbse),font = ("arial",16),fg = "green").place(x = 5, y = 130)
   else:
       bf3 = Label(windows26,text = "SETFBSE returns: " + str(fbse),font = ("arial",16),fg = "red").place(x = 5, y = 130)
   if nifbk > stockamt:
       bf4 = Label(windows26,text = "NIFBK returns: " + str(nifbk),font = ("arial",16),fg = "green").place(x = 5, y = 160)
   else:
       bf4 = Label(windows26,text = "NIFBK returns: Not profitable",font = ("arial",16),fg = "red").place(x = 5, y = 160)

   ambuja =  Max(path + r"\AMBUJACEM.NS.csv", commamt)
   hindpetro =  Max(path + r"\HINDPETRO.NS.csv", commamt)
   grasim =  Max(path + r"\GRASIM.NS.csv", commamt)
   tata =  Max(path + r"\TATACHEM.NS.csv", commamt)
   nmdc =  Max(path + r"\NMDC.NS.csv", commamt)
   global commax
   commax  = max(ambuja, grasim, hindpetro, tata, nmdc)

   bf5 = Label(windows26,text = "Amount invested in Commodities = " + str(commamt),font = ("arial",16),fg = "blue").place(x = 5, y = 200)
   if ambuja > commamt:       
        bf6 = Label(windows26,text = "Ambuja returns: " + str(ambuja),font = ("arial",16),fg = "green").place(x = 5, y = 230)
   else:
       bf6 = Label(windows26,text = "Ambuja returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 230)
   if hindpetro > commamt:       
        bf7 = Label(windows26,text = "HindPetro returns: " + str(hindpetro),font = ("arial",16),fg = "green").place(x = 5, y = 260)
   else:
       bf7 = Label(windows26,text = "HindPetro returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 260)
   if grasim > commamt:       
        bf8 = Label(windows26,text = "Grasim returns: " + str(grasim),font = ("arial",16),fg = "green").place(x = 5, y = 290)
   else:
       bf8 = Label(windows26,text = "Grasim returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 290)
   if tata > commamt:       
        bf9 = Label(windows26,text = "TataChem returns: " + str(tata),font = ("arial",16),fg = "green").place(x = 5, y = 320)
   else:
       bf9 = Label(windows26,text = "TataChem returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 320)
   if nmdc > commamt:       
        bf10 = Label(windows26,text = "NMDC returns: " + str(nmdc),font = ("arial",16),fg = "green").place(x = 5, y = 350)
   else:
       bf10 = Label(windows26,text = "NMDC returns: Not profitable ",font = ("arial",16),fg = "red").place(x = 5, y = 350)

   bnext = Button(windows26, text="Next", font=('arial', 12, 'bold'), fg='blue', command=bnext26).pack(side=BOTTOM)    
   windows26.mainloop()

def bnext26():

   global windows27
   windows27 = Toplevel(windows26)
   windows27.title("Fixed Deposits Prediction")
   windows27.geometry("800x450")
   windows26.withdraw()
   btn11 = Button(windows27, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback26).pack(side=BOTTOM)
   global fdamt
   bf1 = Label(windows27,text = "Amount invested in FDs = " + str(fdamt),font = ("arial",16),fg = "blue").place(x = 5, y = 10)

   sbi = fd(fdamt,'SBI Fixed Deposit', '7 days to 45 days')
   bf = Label(windows27,text = "SBI returns: " + str(sbi),font = ("arial",16),fg = "green").place(x = 5, y = 40)
   hdfc = fd(fdamt,'HDFC Bank Fixed Deposit', '7 days')
   bf = Label(windows27,text = "HDFC returns: " + str(hdfc),font = ("arial",16),fg = "green").place(x = 5, y = 70)
   icici = fd(fdamt,'ICICI Bank Fixed Deposit', '7 days')
   bf = Label(windows27,text = "ICICI returns: " + str(icici),font = ("arial",16),fg = "green").place(x = 5, y = 100)
   axis = fd(fdamt,'Axis Bank', '7 days')
   bf = Label(windows27,text = "Axis Bank returns: " + str(axis),font = ("arial",16),fg = "green").place(x = 5, y = 130)
   kotak = fd(fdamt,'Kotak Bank', '7 days')
   bf = Label(windows27,text = "kotak returns: " + str(kotak),font = ("arial",16),fg = "green").place(x = 5, y = 160)
   bob = fd(fdamt,'Bank of Baroda', '7 days')
   bf = Label(windows27,text = "Bank of Baroda returns: " + str(bob),font = ("arial",16),fg = "green").place(x = 5, y = 190)
   citi = fd(fdamt,'Citibank', '7 days')
   bf = Label(windows27,text = "Citibank returns: " + str(citi),font = ("arial",16),fg = "green").place(x = 5, y = 220)
   idfc = fd(fdamt,'IDFC First Bank', '7 days')
   bf = Label(windows27,text = "IDFC returns: " + str(idfc),font = ("arial",16),fg = "green").place(x = 5, y = 250)
   global stockmax
   global commax
   global fdmax
   global cash
   fdmax = max(sbi, hdfc,icici,axis,kotak,bob,citi,idfc)
   #bf = Label(windows27,text = "TOTAL returns: Rs" + str(stockmax+commax+fdmax+cash),font = ("arial",16),fg = "green").place(x = 5, y = 280)
   bnext = Button(windows27, text="Next", font=('arial', 12, 'bold'), fg='blue', command=bnext27).pack(side=BOTTOM)    
   windows27.mainloop()

def bnext27():

   global windows28
   windows28 = Toplevel(windows27)
   windows28.title("Final result")
   windows28.geometry("800x450")
   windows27.withdraw()
   btn11 = Button(windows28, text="back", font=('arial', 12, 'bold'), fg='blue', command=bback27).pack(side=BOTTOM)
   global stockmax
   global commax
   global fdmax
   global cash
   treturn = stockmax+commax+fdmax+cash
   global stockamt
   global fdamt 
   global commamt
   s = stockamt + fdamt + cash + commamt
   gainperc = ((treturn - s)/s) * 100
   bf = Label(windows28,text = "Total returns:  Rs",font = ("arial",32),fg = "blue").place(x = 5, y = 10)
   bf = Label(windows28,text = str(treturn),font = ("arial",32),fg = "green").place(x = 320, y = 10)
   bf = Label(windows28,text = "Return Percent: ",font = ("arial",32),fg = "blue").place(x = 5, y = 100)
   bf = Label(windows28,text =  str(gainperc) + "%",font = ("arial",32),fg = "green").place(x = 320, y = 100)
   bnext = Button(windows28, text="Quit", font=('arial', 12, 'bold'), fg='blue', command=quit).pack(side=BOTTOM)    
   windows28.mainloop()

def bback():

    windows.withdraw()
    root.deiconify()
    root.mainloop()
def bback2():

    windows3.withdraw()
    windows.deiconify()
    windows.mainloop()
def bback3():

    windows4.withdraw()
    windows3.deiconify()
    windows3.mainloop()
def bback4():

    windows5.withdraw()
    windows4.deiconify()
    windows4.mainloop()
def bback5():

    windows6.withdraw()
    windows5.deiconify()
    windows5.mainloop()
def bback6():

    windows7.withdraw()
    windows6.deiconify()
    windows6.mainloop()
def bback7():

    windows8.withdraw()
    windows7.deiconify()
    windows7.mainloop()
def bback8():

    windows9.withdraw()
    windows8.deiconify()
    windows8.mainloop()
def bback9():

    windows10.withdraw()
    windows9.deiconify()
    windows9.mainloop()
def bback10():

    windows11.withdraw()
    windows10.deiconify()
    windows10.mainloop()
def bback11():

    windows12.withdraw()
    windows11.deiconify()
    windows11.mainloop()
def bback12():

    windows13.withdraw()
    windows12.deiconify()
    windows12.mainloop()
def bback13():

    windows14.withdraw()
    windows13.deiconify()
    windows13.mainloop()
def bback14():

    windows15.withdraw()
    windows14.deiconify()
    windows14.mainloop()
def bback15():

    windows16.withdraw()
    windows15.deiconify()
    windows15.mainloop()
def bback16():

    windows17.withdraw()
    windows16.deiconify()
    windows16.mainloop()
def bback17():

    windows18.withdraw()
    windows17.deiconify()
    windows17.mainloop()
def bback18():

    windows19.withdraw()
    windows18.deiconify()
    windows18.mainloop()
def bback19():

    windows20.withdraw()
    windows19.deiconify()
    windows19.mainloop()
def bback20():

    windows21.withdraw()
    windows20.deiconify()
    windows20.mainloop()
def bback21():

    windows22.withdraw()
    windows21.deiconify()
    windows21.mainloop()
def bback22():

    windows23.withdraw()
    windows22.deiconify()
    windows22.mainloop()
def bback23():

    windows24.withdraw()
    windows23.deiconify()
    windows23.mainloop() 
def bback24():

    windows25.withdraw()
    windows24.deiconify()
    windows24.mainloop() 
def bback25():

    windows26.withdraw()

    windows25.deiconify()
    windows25.mainloop()    
def bback26():

    windows27.withdraw()
    windows26.deiconify()
    windows26.mainloop()  
def bback27():

    windows28.withdraw()
    windows27.deiconify()
    windows27.mainloop()    
def checked():

    c = 0
    c = v0.get() + v1.get() + v2.get() +  v3.get() + v4.get() + v5.get() + v6.get() + v7.get() + v8.get() + v9.get() + v10.get() + v11.get() + v12.get() + v13.get() + v14.get() + v15.get() + v16.get() + v17.get() + v18.get() + v19.get()
    global total
    total = c
    

root = Tk()

v0 = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()
v13 = IntVar()
v14 = IntVar()
v15 = IntVar()
v16 = IntVar()
v17 = IntVar()
v18 = IntVar()
v19 = IntVar()

Age = IntVar()
Mat = IntVar()
Sav = IntVar()

changemade = 0
stockch = IntVar()
commch = IntVar()
fdch = IntVar()
cashch = IntVar()

stockperc = 0
fdperc = 0
cashperc = 0
commperc = 0

stockamt = 0
fdamt = 0 
cash = 0
commamt = 0

stockmax = 0
commax = 0
fdmax = 0

root.title("Risk Analysis")
root.geometry("900x200")

lbl0 = Label(root,text = "Answer the following questions:",font = ("arial",42,"bold"),fg = 'blue').pack(side = TOP)
lbl00 = Label(root,text = "for assessing your risk appetite",font = ("arial",37,"bold"), fg = 'grey').pack(side = TOP)

btn1 = Button(root,text = "Proceed",font = ('arial',12,'bold'),fg = 'blue',command = bnext).pack(side = BOTTOM)

root.mainloop()
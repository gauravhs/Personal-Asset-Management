# Importing the libraries
import requests
from bs4 import BeautifulSoup
import csv
from tkinter import *
import pandas as pd
import itertools
import os
 
#Specify URL
url = "https://www.myloancare.in/fixed-deposit/fd-interest-rates/"

# Make Get request
response = requests.get(url)

# Parse the HTML content of main page
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find('table', attrs = {'class' : 'table table-curved doc-table'})

#Write to CSV File
csvfile = open('Banks.csv', 'w+', newline='')
writer = csv.writer(csvfile)
for row in table.find_all('tr'):
    csvRow = []
    for cell in row.find_all(['td', 'th']):
        cell_text = cell.get_text(strip = True)
        csvRow.append(cell_text)
    writer.writerow(csvRow)
csvfile.close()
#Keeping only the first 10 banks
#df = pd.read_csv('new.csv')
#df.drop(df.tail(40).index, inplace=True)
#df.to_csv('new.csv')

#Function for storing tables for each bank in a new file
def openbank(url1, bank):
    url2 = url1
    response = requests.get(url2)
    soup1 = BeautifulSoup(response.content, "lxml")
    table1 = soup1.find('table', attrs = {'class' : 'table table-curved'})
    df = pd.read_html(str(table1))[0]
    bankname = bank
    tenure = df["Tenure"].tolist()
    interest =  df["FD Rates"].tolist()
    dict = {'Name of Bank': bankname ,'Tenure' : tenure, 'Interest' : interest}
    df = pd.DataFrame(dict).head(n=5)
    df.to_csv(r'C:\Users\Admin\Desktop\new2.csv', mode = 'a', index=False)
        
#Retrieving the individual links for each bank to store the details
#And passing it to the function
rows = table.find_all('tr')
for tr in rows:
    cols = tr.find_all('td')
    if len(cols) >= 2 :
        link = cols[0].find('a').get('href')
        #print(link)
        openbank(link, cols[0].get_text(strip = True))
        
#Removing multiple rows from new2 file(Name, Tenure, Interest)
rows = csv.reader(open("new2.csv", "rt"))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("new2.csv", "wt"))
writer.writerows(newrows)
df = pd.read_csv('new2.csv')
df.to_csv('output.csv', index=False)
#Calculations
def home():

    PERCENTAGE = 100
    amount_request = int(e1.get())
    subs = str(choices[tkvar.get()])
    results = []

    with open('output.csv') as csvfile:
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
            #print(banks)
            #print(tenures)
            #print(interests)
    
    prd = [i for i in tenures if subs in i] 
    for i in range(1, len(banks)):
        if tenures[i] in prd:
            b_n = banks[i]
            t_n = tenures[i]
            perc_val = float(interests[i].rstrip("%"))
            cal = round((perc_val*amount_request)/ PERCENTAGE, 2)
            tot = amount_request + cal
            temp_text = str(b_n) + '(' + str(perc_val) + '% ) = '+ str(tot) + 'Rs (Interest Earned = '+ str(cal) + 'Rs) \n'
            results.append(str(temp_text))
    #Display the Results
    mylist = Listbox(master, yscrollcommand = scrollbar.set, width = 70, height = int(80/3) )
    for line in range(len(results)):
        mylist.insert(END, results[line])
    mylist.pack( side = LEFT, fill = BOTH )
    mylist.place(relx = 0.5, rely = 0.5, anchor="center")
    scrollbar.config( command = mylist.yview )

#Application
#Setup GUI
master = Tk(className = ' Dynamic Fixed Deposit Calculator' )
master.minsize(width=770, height=300)
scrollbar = Scrollbar(master)
scrollbar.pack( side = RIGHT, fill=Y )
Label(master, text = 'Deposit Amount').pack()
e1 = Entry(master)
e1.pack()

Label(master, text = 'No. of Days').pack() 
mainframe = Frame(master)
mainframe.pack()
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

tkvar = StringVar(master)
choices = {  '7-14 Days':'7 days to 14 days',
             '15-29 Days':'15 days to 29 days',
             '30-45 Days':'30 days to 45 days',
             '7-45 Days':'7 days to 45 days' ,
             '46-60 Days':'46 days to 60 days',
             '46-90 Days':'46 days to 90 days',
             '91-180 Days':'91 days to 180 days'}

popupMenu = OptionMenu(mainframe, tkvar, *choices)
popupMenu.pack()

# on change dropdown value
def change_dropdown(*args):
    print(choices[tkvar.get()])

# link function to change dropdown
tkvar.trace('w', change_dropdown)

line = '    '
Label(master, text = line).pack()
Button(master, text = "Calculate", command = home).pack()
mainloop()

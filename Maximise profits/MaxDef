
import csv

F = 'NMDC.NS.csv'

A = 1000

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
            
            print("Buy on day: ",buy,"\t", 
                "Sell on day: ",sell)
            Profit.append(total)
            #print(price[buy])
            temp =1 + (sum/price[buy])
            ProfitPercentage.append(temp)
            
    price = Y
    n = len(price)

    stockBuySell(price, n)
    print(Profit)
    print(ProfitPercentage)
    

    Final = Amount
    for i in range(0, len(ProfitPercentage)):
        Final = Final * (ProfitPercentage[i])
    
    return(Final)

Max(F, A)

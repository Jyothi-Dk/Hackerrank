stock_prices=[10,4,2,9]
max_no=max(stock_prices)#10
diff=[]
for i in range(stock_prices.index(max_no),len(stock_prices)):
    diff.append(abs(stock_prices[i]-max_no))
       
        
print(max(diff))
      
        
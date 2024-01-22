
cost_price = int(input("enetr the cost price: "))
sale_price = int(input("enetr the sale price: "))

# profit
if sale_price > cost_price:
    profit = sale_price - cost_price
    print( "we have made profit of ", profit)

#loss
elif sale_price < cost_price:
    loss =  cost_price - sale_price
    print( "we have made loss of ", loss)
    
# neither profit nor loss    
else:
    print(" we have made neither profit nor loss")



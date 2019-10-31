__author__ = 'Sachin Mistry'
__email__ = 'sachin_mistry@outlook.com'
__licence__ = 'Uni Licence'
__version__ = '2019 10-10'

sweets =('First' , 'Second' , 'Third' , 'Forth' , 'Fifth' ,)
prices = []
for sweet in sweets:
    sweets_shop=int(input('Enter price of ' +str(sweet + ' sweet: ')))
    prices.append(sweets_shop)



average_price = sum(prices) / len(sweets)
average_price =str(round(average_price, 2))
highest_price = max(prices)
lowest_price = min(prices)
total_price= sum(prices)
print('The average price for is: ' +str(average_price))
print('The highest price is: ' +str(highest_price))
print('The lowest price is: ' +str(lowest_price))
print('The total price is ' +str(total_price))
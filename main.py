# ORDER FROM A MENU!!!!!!!!!!!!!!

menu = {
    'Popcorn': 12.5,
    'Hot Dog': 2.35,
    'Giant Pretzel': 7.8,
    'Assorted Lollies': 4.35,
    'Soda': 2.6,
    'Bottled Water': 3,
    'Nachos': 6.5,
    'Chips': 4.8
    }

# You didn't see this....
secret_menu = {
    'Fart Juice': 69420
}

total = 0
cart = []

print('############## MENU ################')
for item, price in menu.items():
    print(f'{item:20}: A${price:.2f}')
print('####################################')

while True:
    buy = input("\nWhat would you like to buy? (Q to Quit): ").title()
    
    if not menu.get(buy) == None:
        amount = int(input("How many would you like to buy?: "))
        
        for i in range(amount):
            cart.append(buy)
    
    elif not secret_menu.get(buy) == None:
        print("You don't wanna do this...")
        cart.append(buy)
    
    elif buy[0] == 'Q':
        break
    
    else:
        print(f'{buy} is not on the menu.')
    
print('########### YOUR CART #############\n')

for buy in cart:
    
    if buy == 'Fart Juice':
        print('MURDE- I mean uhh Fart Juice')
    else:
        print(buy)
    
    total += menu.get(buy, secret_menu.get(buy))
    
print(f'\nYour total is A${total:,.2f}!')

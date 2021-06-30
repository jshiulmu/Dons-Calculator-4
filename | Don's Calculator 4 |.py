#UPGRADED CALCULATOR FOR DIVIDING LONG BILLS WITH MANY ITEMS, (GROCERY SHOPPING, RESTAURANTS)
#VERSION 4

#GO TO RUN>RUN MODULE AT TOP TO RUN PROGRAM

stop = False
#count = 0

print("Calculator 4 by Jordan Shiu (and Dylan Shiu a little bit).\n\n")
print("Create a seperate file with each items' price and who is paying for each item.")
print("Be sure to give every item a new line and seperate everything with spaces. You can put text, not numbers, before the item's price to label it. This is an example:\n\n")
print("100 PersonA PersonB PersonC\nLobster 6.99 PersonA\nEggs 6.99 PersonB PersonD\n")
print("Copy and paste the text into the program. Enter '000' on a new line and press Enter. Totals will be returned.\n\nCopy and paste text below this line:")


#CALCULATOR 4 improvement: INPUTS CAN ACCEPT WORDS BEFORE PRICE: "Eggs 9 A B C" OR NOT, "9 A B C" IS GOOD TOO



totals = {}
price = 0

def who_payin (item):
    global price
    i = 0
    start = 0
    calculate = []
    
    calc_input = item.split()
    
    for i in calc_input:
        try: 
            price = float(i)
            location = calc_input.index(i)
        except:
            pass
        
    for i in calc_input:
        if calc_input.index(i) <= location:
            pass
        elif calc_input.index(i) > location:
            calculate.append(i)
        
        
    for i in calculate:
        if i in totals.keys():
            totals[i] += price/len(calculate)

        elif i not in totals.keys():
            totals[i] = price/len(calculate)
           
while stop == False:
    item = input()

    who_payin(item)

    if item == "000":
        stop = True
        

print("\nGreat! The total today is")
print(sum(totals.values()))
print("Here's what everyone must pay:")
print(totals)





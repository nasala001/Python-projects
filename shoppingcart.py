#shopping cart program
#content covered: list,sets,tuples
foods=[] #we are not going to use tuples here i.e. () which are unchangeable since we are going to ask customers what are they going to buy
prices=[]
total=0
while True:
    food=input("enter a food to buy(q to quit):")
    if food.lower() == "q": #even though customers type Q it will make it lowercase
        break
    else:
        price=float(input(f"enter price of {food}:"))
        foods.append(food)
        prices.append(price)
print("-----YOUR CART------")
for food in foods:
    print(food,end=" ")
for price in prices:
    total=total+price
#pizza momo your total is: 10.1 if print() not added
print()

print(f"your total is: {total}")

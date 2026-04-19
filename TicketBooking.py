# TICKET BOOKING SYSTEM
print("=" * 35)
print("**** MELA OF THE SPRING ****")
print("-" * 35)
print("// TICKET PRICE - RS.200 //")
print("(type 'q' as username to quit)")

ticket_price = 200
username = []
ages2 = []
total_list = []
price_list = []

while True:
    print("\n--- New Booking ---")


    username3 = input("Enter your username (or 'q' to quit): ")
    if username3.lower() == "q":
        print("\n Quitting... showing summary!")
        break  # jumps out of while loop directly

    ages = int(input("Enter your age: "))
    num_tickets = int(input("Enter number of tickets: "))

    if 0 < ages <= 17:
        category = "Child"
        discount = 0.50
    elif 17 < ages <= 58:
        category = "Adult"
        discount = 0.0
    else:
        category = "Senior"
        discount = 0.35

    original_price = ticket_price * num_tickets
    discount_amount = original_price * discount
    final_price = original_price - discount_amount

    username.append(username3)
    ages2.append(ages)
    total_list.append(num_tickets)
    price_list.append(final_price)

    print(f"\n  Category       : {category}")
    print(f"  Discount       : {int(discount * 100)}%")
    print(f"  Original Price : Rs. {original_price}")
    print(f"  Final Price    : Rs. {final_price:.2f}")


print("\n" + "=" * 35)
print("------FINAL BOOKING SUMMARY------")
print("=" * 35)


if len(username) == 0:
    print("\n  No bookings were made!")
else:
    total_tickets = 0
    total_price = 0

    for i in range(len(username)):
        print(f"\n  Name    : {username[i]}")
        print(f"  Age     : {ages2[i]}")
        print(f"  Tickets : {total_list[i]}")
        print(f"  Price   : Rs. {price_list[i]:.2f}")
        total_tickets += total_list[i]
        total_price += price_list[i]

    print("\n" + "-" * 35)
    print(f"  TOTAL TICKETS : {total_tickets}")
    print(f"  TOTAL PRICE   : Rs. {total_price:.2f}")

print("=" * 35)
print("   Thank you for booking!")
print("=" * 35)
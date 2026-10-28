def calculate_change(paid, price):
    result = paid - price
    return result

snack_price = 40
print("===VENDING MACHINE===")
print("Snack price =", snack_price)
print("Accepted coins are: 1, 5, 10, 25")

total_inserted = 0
coin_inserted = 0
while True :
    coin = int(input("Which coin inserted: "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        continue
    total_inserted = total_inserted + coin
    coin_inserted = coin_inserted + 1
    print("Total money inserted: ",total_inserted)
    print("Number of coin inserted: ",coin_inserted)
    if total_inserted >= snack_price:
        print("Enough coin inserted.")
        break
cal_change = calculate_change(total_inserted, snack_price)
print("Dispensing your snack.")
if cal_change == 0:
    pass
else:
    print("Here is your change: ",cal_change)
print("==== PURCHASE SUMMARY ====")
print("Snack Price: ",snack_price)
print("Coins Inserted: ",coin_inserted)
print("Total Paid: ",total_inserted)
print("Change Given: ",cal_change)
print("==========================")
print("Thanks for purchase!")
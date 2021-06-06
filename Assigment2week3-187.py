def save_transaction(prices, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%s%07d%s\n" % (credit_card, prices * 100, description))
    file.close()

items = ['Donut','Latte','Filter','Muffin']
prices = [1.50,2.0,1.80,1.20]
running = int(1)

while running == int(1):
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("choose an option: "))
    running = int(2)
    if choice == option:
        running = int(2)
    else:
        credit_card = input("Credit card number: ")
        running = int(2)
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])

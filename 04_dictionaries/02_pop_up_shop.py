def fruit_purchase():
    fruits = {'apple': 10, 'oranges': 5, 'grapes': 15}
    total_sale = 0

    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many {fruit_name} do you want to buy? "))
                total_sale += (amount_bought * price)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    return total_sale

def main():
    purchase = fruit_purchase()
    print(f"Total Price: {purchase}")

if __name__ == '__main__':
    main()                           
   
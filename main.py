MENU = {'hamburger','pizza','sandwich','doner','cola','sprite','cookie','fries','chicken strips'}
print(" Welcome to Food Ordering Services")
print("<--------------------------------->")
def get_order():
    current_order = []
    while True:
        print("What Can I Get For You?\n")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I am sorry, we don't serve that.")
            continue
        if is_order_complete():
            return current_order

def is_order_complete():
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        print("Invalid Input")
        

def output_order(order_list):
    print("Okay so you want")
    for order in order_list:
        print(order)

def main():
    order= get_order()
    output_order(order)
    print("Please drive through to the second window.")

if __name__ == "__main__":
    main()

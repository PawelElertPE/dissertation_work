import sys
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    },
    "water": {
        "ingredients": {
            "water": 250,
        },
        "cost": 0.75
    },
    "milk": {
        "ingredients": {
            "milk": 250,
        },
        "cost": 1.50
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 550,
    "coffee": 100,
}



temperature = 20
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            print(f"Top up {item} immediately")
            is_hot = False


            #global current_temperature
            current_temperature = 100
            i = 1
            while current_temperature > 20:
                current_temperature -= 1
                time.sleep(0.4 * i)
                i *= 1.05 
                print(f"The current temperature is: {current_temperature}°C.")
                print(f"The temperature drops by 1Deg in {round(0.4 *i, 3)} seconds.")
                is_hot = False
                if current_temperature == 20:
                    print("You have safely switched the coffee-machine off")
                    print("Please replenish the resources and restart the coffe-machine.")
                    sys.exit() # It does the job. When you run out of ressources, the machine cools down and switches off!
                    # Restart the program, once you have replenished resources.
                    return False

            is_hot = False
            break
        elif order_ingredients[item] > 0.3 * resources[item]:
            print(f"You have only 30% or less of {item} left. Top up soon!")
            print(f"Water: {resources['water']}ml.")
            print(f"Milk: {resources['milk']}ml.")
            print(f"Coffee: {resources['coffee']}g.")
        else:
            return True
    return True

#TODO: udate the amount customer has inserted after qarters, dimes and so on....
#      If the amount is less than required, tell it the customer.
#      If the amount is more, tell him/her  as well
def process_coins_and_transaction(drink_cost):
    """Handles the coin processing and checks if the transaction is successful."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    #print(f"You have already inserted {total:.2f}.")
    if total <= drink_cost:
        print(f"There is ${(drink_cost - total):.2f} remaining.")
    else:
        print(f"You have already inserted $ {total:.2f}, it's more, than {choice} costs:$ {drink_cost:.2f}")
    
    total += int(input("How many dimes?: ")) * 0.1
    if total <= drink_cost:
        print(f"There is $ {(drink_cost - total):.2f} remaining.")
    else:
        print(f"You have already inserted $ {total:.2f}, it's more, than {choice} costs:$ {drink_cost:.2f}")
        
    total += int(input("How many nickles?: ")) * 0.05
    if total <= drink_cost:
        print(f"There is $ {(drink_cost - total):.2f} remaining.")
    else:
        print(f"You have already inserted $ {total:.2f}, it's more, than {choice} costs:$ {drink_cost}")
                
    total += int(input("How many pennies?: ")) * 0.01

    if total >= drink_cost:
        change = round(total - drink_cost, 2)
        print(f"Here is $ {change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

#TODO: create various wait times and various ICONS for each drink!!!
# do it, :))
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    # print(f"Your {drink_name} is being brewed.... Please wait")
    # time.sleep(3)
    # print(f"Here is your {drink_name} ☕️. Enjoy!")
    if choice == "espresso": # or "latte" or "cappuccino":
        print(f"Your {drink_name} is being brewed 🫖.... Please, please wait")
        time.sleep(3)
        print(f"Here is your {drink_name} ☕️. Enjoy!")
    elif choice == "latte":
        print(f"Your {drink_name} is being brewed 🫖.... Please, please wait")
        time.sleep(4.2)
        print(f"Here is your {drink_name} ☕️☕️. Enjoy!")
    elif choice == "cappuccino":
        print(f"Your {drink_name} is being brewed 🫖.... Please, please wait")
        time.sleep(4.8)
        print(f"Here is your {drink_name} ☕️🍰. Enjoy!")
        
    elif  choice == "water":
        print(f"Your {drink_name} is being served🫗.... Please wait")
        time.sleep(1.9)
        print(f"Here is your {drink_name} 🥛. Enjoy!")
    else: # choice == "milk":
        print(f"Your {drink_name} is being served 🐄.... Please wait")
        time.sleep(2.2)
        print(f"Here is your {drink_name} 🥛🍰. Enjoy your daily proteins intake!")



is_on = True



current_temperature = 20
is_warming_up = True

while current_temperature < 100:
    if is_warming_up:
        current_temperature += 1
        time.sleep(0.1)
        print(f"The current temperature is: {current_temperature}°C.")
        if current_temperature == 100:
            print("The coffee machine is ready.")
            is_warming_up = False
            is_hot = True

while is_hot:
    choice = input("What would you like? (espresso/latte/cappuccino/milk/water/report/off): ").lower()
    if choice == "off":
        print("Thank you, bye")
        i = 1
        while current_temperature > 20:
            current_temperature -= 1
            time.sleep(0.4 * i)
            i *= 1.05 #Im bardziej temp. maszyny i otoczenia sie zlizaja, tym spadek temp. jest wolniejszy.
            #napisac to samo tam, gdzie kawiarka wylacza sie z powodu braku zasobow!!!!!
            print(f"The current temperature is: {current_temperature}°C.")
            print(f"The temperature drops by 1Deg in {round(0.4 *i, 3)} seconds.")
            if current_temperature == 20:
                print("You have safely switched the coffee-machine off")
                print("Thank you, bye")
                #choice = "off"
        is_hot = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU.get(choice)
        if drink:
            print(f"The amount you have to pay is ${drink['cost']:.2f}")
            if is_resource_sufficient(drink["ingredients"]):
                if process_coins_and_transaction(drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please choose from espresso, latte, cappuccino, water or milk.")

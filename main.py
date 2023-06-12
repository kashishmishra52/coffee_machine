MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":00
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    '''checks whether the resources are enough or not'''
    for keys in order_ingredients:
        if order_ingredients[keys] >= resources[keys]:
            print(f"SORRY there is not enough {keys}")
            return False
    return True

def process_coins():
    '''calculate the sum of coins inserted into the machine '''
    print("please enter coins to get processed")
    total=int(input("how many quarters?"))*0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total
def transaction(money_received,drink_cost):
    '''calculate the whole transaction and returns change '''
    if money_received>=drink_cost:
        change=money_received-drink_cost
        print(f"here is your ${change}change")
        global profit
        profit+=drink_cost
        print("your payment is succesful")
        return True
    else:
        print("SORRY that's not enough money money refunded")
        return False
def make_coffee(drink_name,order_ingredients):
    '''produce th efinal coffe and deduct the resources '''
    for keys in order_ingredients:
        resources[keys]-=order_ingredients[keys]
    print(f"here is your {drink_name}")


is_on=True
while is_on:
    choice=input("what do you like to have today (ESPRESSO/LATTE/CAPPUCCINO/report)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(resources)
        print(profit)
    else:
        choicee = MENU[choice]
        if check_resources(choicee["ingredients"]):
            payment=process_coins()
            if transaction(payment,choicee["cost"]):
                make_coffee(choice,choicee["ingredients"])



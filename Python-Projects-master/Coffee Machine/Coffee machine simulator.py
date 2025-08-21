menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":100,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":150,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":200,
    }
}
resources={
    "water":500,
    "milk":200,
    "coffee":100,
}
def check(ingredients):
    for i in ingredients:
        if ingredients[i]>resources[i]:
            print(f"there is no enough resources.")
            return False
    return True

flag=True
profit=0
while flag:
    entry=input("what would you like to have?(latte/espresso/cappuccino):").lower()
    if entry=='off':
        exit()
    elif entry=='report':
        print(f"water={resources["water"]}\nmilk={resources["milk"]}\ncoffee={resources["coffee"]}\nmoney={profit}")
    else:
        coffee_type=menu[entry]
        print(coffee_type)
        if check(coffee_type['ingredients']):
            five = int(input("enter no.of Rs.5 coins:"))
            ten = int(input("enter no.of Rs.10 coins:"))
            twenty = int(input("enter no.of Rs.20 coins:"))
            money = five * 5 + ten * 10 + twenty * 20
            # if money>=menu[entry]['cost']:
            #     print("payment sucessful.")
            if money==menu[entry]['cost']:
                profit=profit+money
                resources['water']=resources['water']-coffee_type['ingredients']['water']
                resources['coffee'] = resources['water'] - coffee_type['ingredients']['coffee']
                resources['milk'] = resources['water'] - coffee_type['ingredients']['milk']
                print(f"Here is your {entry}")
            elif money>menu[entry]['cost']:
                refund=money-menu[entry]['cost']
                profit=profit+menu[entry]['cost']
                resources['water'] = resources['water'] - coffee_type['ingredients']['water']
                resources['coffee'] = resources['coffee'] - coffee_type['ingredients']['coffee']
                resources['milk'] = resources['milk'] - coffee_type['ingredients']['milk']
                print(f"Here is your {entry} and your change is Rs.{refund}")
            elif money<menu[entry]['cost']:
                print(f"sorry that's not enough money.your Rs.{money} refunded sucessfully.")
                

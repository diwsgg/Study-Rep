from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Creating the objects
menu = Menu()
newCoffe = CoffeeMaker()
money = MoneyMachine()

def main():
    #Keep the cicle
    anotherDrink = False
    print("Welcome to the coffe machine")
    while not anotherDrink:
        print("-"*50)
        print("What kind of drinks dou you like, we have: ")
        print("-"*50)
        print(menu.get_items())
        print("-"*50)
        option = input("\n Which one doy you like?: ").lower()
        if option == 'off':
            anotherDrink = True
        elif option == 'report':
            newCoffe.report()
            money.report()
            print("-"*50)
        elif option == "latte" or option == "espresso" or option == "cappuccino":
            #1. We are going to check if we have the enough ingredients
            #2. Then payment
            #3. And for last we make the coffe

            #We need a new object since we need all the atributes for this one, not just the "coffe type"
            typeDrink = menu.find_drink(option)

            #1. FIRST CHECK
            if(newCoffe.is_resource_sufficient(typeDrink)):
                #2. Second check
                if(money.make_payment(typeDrink.cost)):
                    #3. Make the coffe
                    newCoffe.make_coffee(typeDrink)
                    print("-"*50)
        else: 
            print("*"*50)
            print("That is not a correct option")
            print("*"*50+"\n")
    print("Have a nice day")

main()
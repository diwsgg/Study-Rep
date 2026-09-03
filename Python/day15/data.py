#Add the dictionaries

MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffe": 18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffe": 24,
        },
        "cost":2.5,
    },
    "capucchino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffe": 24,
        },
        "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffe": 100,
}

#Options to pay
options_to_pay={
    'penny' : 0.01,
    'dime' : 0.10,
    'nickel' : 0.05,
    'quarter' : 0.25,
}
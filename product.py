# project- shop Management System
# Feature cover 
#               : variables,conditions,
#                 loop,function,list and dictionary
#                 fuction,oops,file handling,error handling

import json 
import os
if os.path.exists("product.json"):
    with open("product.json", "r") as file:
        products=json.load(file)
else:
    products={}
    
def add_product():
    name=input("enter your product name")
    price=int(input("enter your product price"))
    quantity=int(input("enter your product Quantity"))
    total_price=quantity*price
    
    product={"Name":name,
             "Price":price,
             "Quantity":quantity,
             "Total Price":total_price
    }
    products[name]=product
    

    with open("product.json","w")as file:
        json.dump(products,file,indent=4)
    print("PRODUCT ADDED SUCCESSFULLY")

def search_product(name):
    with open("product.json","r")as file:
        products=json.load(file)
        if name in products:
            print(products[name])
        else:
            print("PRODUCT NOT AVAILABLE")
            
def sell_item(name,quantity):
    with open("product.json","r")as file:
        products=json.load(file)
        if "sell_item" in products[name]:
            products[name]["sell_item"]+=quantity
        else:
            products[name]["sell_item"]=quantity
            products[name]["sell_price"]=quantity*products[name]["Price"]
            products[name]["left quantity"]=products[name]["Quantity"]-quantity
    with open("product.json","w")as file:
        json.dump(products,file,indent=4)
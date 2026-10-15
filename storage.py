#this file use for storage fuction and errors

import os,json
def exist_file():
    try:
        if os.path.exists("product.json"):
            with open("product.json","r")as f:
                products=json.load(f)
                
        else:
            products={}
    except json.JSONDecodeError:
        products={}
        
    return products

def save(products):
    with open("product.json","w") as f:
        json.dump(products,f,indent=4)
    
        
def read():
    try:
        with open("product.json","r")as f:
            products=json.load(f)
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
            print("PRODUCT NOT AVAIABLE")

    return products

def valid_valid_int(message):
    while True:
        try:
            value= int(input(message))
            if value<=0:
             print("try again")
             continue
            return value
        except ValueError:
            print(" not supported string")

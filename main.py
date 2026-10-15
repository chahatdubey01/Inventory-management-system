# project- Inventory Management System
# Feature cover 
#               : variables,conditions,
#                 loop,function,list and dictionary
#                 fuction,oops,file handling,error handling
# This file contain main logics

import storage
products=storage.exist_file()


    
def add_product():
    name=input("enter your product name")
    price=storage.valid_valid_int("enter your product price")
    quantity=storage.valid_valid_int("enter your product Quantity")
    total_price=quantity*price
    
    product={"Name":name,
             "Price":price,
             "Quantity":quantity,
             "Total Price":total_price
    }
    products[name]=product
    
    storage.save(products)
    print("PRODUCT ADDED SUCCESSFULLY")

def search_product(name):
        products=storage.read()
        if name in products:
            print(products[name])
        else:
            print("PRODUCT NOT AVAILABLE")            
def sell_item():
    products=storage.read()
    name=input("enter product name")
    quantity=storage.valid_valid_int("ENTER YOUR QUANTITY")
   
    if name in products:
        if "sell_item"in products[name]:
            if quantity>products[name]["Quantity"]:
                print("not enough product")
            else:
                products[name]["sell_item"]+=quantity
                products[name]["sell_price"]+=products[name]["Price"]*quantity
                products[name]["left_item"]=products[name]["left_item"]-quantity
                            
        else:
            products[name]["sell_item"]=quantity
            products[name]["sell_price"]+=products[name]["Price"]*quantity
            products[name]["left_item"]=products[name]["Quantity"]-quantity
    else:
        print(" product not avalable")
        
   
    storage.save(products)
        
        
# add_product()
# search_product("dahi")
# sell_item()
            

            
    

    
    
        
        

    
    
    


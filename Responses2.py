from knowledge_base import knowledge

def get_user_input(): # getting the input from the user
    return input("How can I assist you with our products today? (Ask about price, specifications, or availability)\n 'help' for more info. \n 'exit' to end conversation. \n")
def simplify_string(input_string): # simplifying the user input for proccesing
    simplified  = input_string.lower()
    if simplified.endswith('s'): # incease the user types in plural, ex laptop/laptops
        simplified = simplified[:-1] # removes the s from plurals
    return simplified
#products = [product["name"] for product in knowledge]
products = []
for i in knowledge:
    products.append(i['name'].lower())
def product_in_query(query):
    items = query.split()
    for i in items:
        if i.lower() in products:
            return i.lower()
    return None
def find_name(name): # a helper function that catches the desired product from the user input
    name = simplify_string(name)
    for product in knowledge:
        if name.lower() in product["name"].lower():
            return product
    return None
def responses(user_input): # handling the user inputs
    if len(user_input.split()) == 1:
        product = ""
        found_product = product_in_query(user_input)
        if found_product:
            product = find_name(found_product)
            if product:
                view = ""
                for key, value in product.items():
                    view += f"{key}: {value}\n" 
                return f"here is an overview of the mentioned item {view}"    

                return f"here is a full overview of the mentioned product:\n {product}"
        
    if any(keyword in user_input for keyword in ["hello", "hi", "salam"]):
        return "hello please read the instructions below"
    if any(keyword in user_input for keyword in ["price", "how much", "cost"]): # code block for price 
        product = ""
        found_product = product_in_query(user_input)
        if found_product:
            product = find_name(found_product)
            if product:
                return f"the price of {product['name']} is ${product['price']}."
        else:
            product_name = input("Please specify the name of the product: ")
            product = find_name(product_name)
            if product:
                return f"The price of {product['name']} is {product['price']}."
            else:
                return "Product not found." 
    elif "is" in user_input and "available" in user_input or "is" in user_input and "stock" in user_input or "quantity" in user_input: # code block for availability
        product = ""
        input_list = user_input.split()    
        found_product = product_in_query(user_input)
        if found_product:
            product = find_name(found_product)
            if product:
                    return f"{product['name']} is available. Quantity: {product['quantity']}."
        else:
            product_name = input("Please specify the name of the product: ")
            product = find_name(product_name)
            if product:
                return f"{product['name']} is available. Quantity: {product['quantity']}."     
            else:   
                return "No matching product found in our inventory."      
    elif "attributes" in user_input or "charactristics" in user_input or "details" in user_input: # code block for specifications
        product = "" 
        found_product = product_in_query(user_input)
        if found_product:
            product = find_name(found_product)
            if product:
                attributes = product['attributes']
                at = ""
                for key, value in attributes.items():
                    at = at +  f"{key}: {value}\n"
                return f"The attributes of the {product['name']} are: \n{at}."
        else:
            product_name = input("Please specify the name of the product: ")
            product = find_name(product_name)
            if product:
                attributes = product['attributes']
                at = ""
                for key, value in attributes.items():
                    at = at +  f"{key}: {value}\n"
                return f"The attributes of the {product['name']} are: \n{at}."  
            else:
                return "product not found"    
    elif user_input.lower() == "help": # user help block
        return ("You can ask about product prices, availability, and specifications.\n"
                "Example queries:\n"
                "- 'What is the price of a laptop?'\n"
                "- 'Is the TV in stock?'\n"
                "- 'Show me details of the smartphone.'")                
    else: # exit / input not understood block
        if user_input == "exit":
            return "exit"  
        else:
            print("I'm sorry, I didn't understand that. Could you please rephrase your question?")
        return responses(get_user_input()) # recurive call to keep the chatbot running

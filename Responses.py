from knowledge_base import knowledge

def get_user_input(): # getting the input from the user
    return input("How can I assist you with our products today? (Ask about price, specifications, or availability)\n 'help' for more info. \n 'exit' to end conversation. \n")
def simplify_string(input_string): # simplifying the user input for proccesing
    simplified  = input_string.lower()
    if simplified.endswith('s'): # incease the user types in plural, ex laptop/laptops
        simplified = simplified[:-1] # removes the s from plurals
    return simplified
def find_name(name): # a helper function that catches the desired product from the user input
    name = simplify_string(name)
    for product in knowledge:
        if name.lower() in product["name"].lower():
            return product
    return None
products = []
for i in knowledge:
    products.append(i['name'])
print(products)    
def responses(user_input): # handling the user inputs
    if any(keyword in user_input for keyword in ["price", "how much", "cost"]): # code block for price 
        product_name  = input(" specify the name of the product ")
        product = find_name(product_name)
        if product:
            return f"the price of {product['name']} is ${product['price']}."
        else:
            return "could not find the response"
    elif "is" in user_input and "available" in user_input or "is" in user_input and "stock" in user_input: # code block for availability
        input_list = user_input.split()    
        for i in input_list:
            product = find_name(i)
            if product:
                return f"{product['name']} is available. Quantity: {product['quantity']}."
        return "No matching product found in our inventory."   
    elif "attributes" in user_input or "charactristics" in user_input or "details" in user_input: # code block for specifications
        input_list = user_input.split()    
        for i in input_list:
            product = find_name(i)
            if product:
                attributes = product['attributes']
                at = ""
                for key, value in attributes.items():
                    at = at +  f"{key}: {value}\n"
                return f"The attributes of the {product['name']} are: \n{at}."
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




























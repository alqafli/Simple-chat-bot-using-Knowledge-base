from Responses2 import get_user_input, responses
i = True
def main(): 
    while True:
        user_input = get_user_input()
        response = responses(user_input)
        if response == "exit":
            print("thank you for using our website !!")
            break
        print(response)
main()

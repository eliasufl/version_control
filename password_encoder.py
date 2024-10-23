#encode() by Elias Ortega
def encode(password):
    password = password.replace("0","a").replace("1","b").replace("2","c").replace("3","d").replace("4","e").replace("5","f").replace("6","g").replace("7","h").replace("8","i").replace("9","j").replace("a","3").replace("b","4").replace("c","5").replace("d","6").replace("e","7").replace("f","8").replace("g","9").replace("h","0").replace("i","1").replace("j","2")
    password = int(password) #by the way i am completely aware that this is probably the absolute stupidest way to do this but it works perfectly
    return password

# decode() by Kaden Jones
def decode(password):
    result = ""
    string_password = str(password)
    for char in string_password: # all of the encrypted characters are related by arithmetic operations so we can undo them based off of what number they are
        if int(char) > 3:
            result = str(result) + str((int(char) - 3))
        elif int(char) < 3:
            result = str(result) + str(int(char) + 7)
        else:
            result = str(result) + "0"


    return result

if __name__ == "__main__":
    while True:
        menu_input = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if menu_input == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_input == "2":
            password = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {password}.")
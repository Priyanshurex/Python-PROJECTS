import random
import string

def generate_password(length, complexity=3):
    if complexity == 1:
        char_set = string.ascii_lowercase 
    elif complexity == 2:
        char_set = string.ascii_letters  
    elif complexity == 3:
        char_set = string.ascii_letters + string.digits 
    elif complexity == 4:
        char_set = string.ascii_letters + string.digits + string.punctuation 
    else:
        print("Invalid complexity level.")
        return None
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6: 
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nSelect the complexity level:")
    print("1: Lowercase letters only")
    print("2: Uppercase + Lowercase letters")
    print("3: Uppercase + Lowercase letters + Digits")
    print("4: Uppercase + Lowercase letters + Digits + Special characters")
    
    while True:
        try:
            complexity = int(input("Enter complexity level (1/2/3/4): "))
            if complexity not in [1, 2, 3, 4]:
                print("Invalid selection. Please choose a valid complexity level.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length, complexity)
    
    print("\nYour generated password is:")
    print(password)

if __name__ == "__main__":
    main()

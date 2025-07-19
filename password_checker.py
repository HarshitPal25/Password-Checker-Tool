def password_strength(password):

    """
    Checks the strength of a password based on various criteria.

    Returns:
        A string indicating the password strength: "Very Weak", "Weak", "Medium", or "Strong".
    """
    length=len(password)
    lowercase = any(char.isupper() for char in password)
    uppercase= any(char.islower() for char in password)
    numerical= any(char.isalnum() for char in password)
    special= any(not char.isupper() for char in password)

    strength= "Very Weak"
    if length>=12 and lowercase and uppercase and numerical and special:
        strength = "Strong"
    elif length>=8 and (lowercase or uppercase) and (numerical or special):
        strength = "Medium"
    elif length>=6 and (lowercase or uppercase or numerical or special):
        strength = "weak"
    return strength
    

def main():
    """
    Gets user input and checks password strength.
    """
    password = input("Enter you password: ")
    strength = password_strength(password)
    if(strength == "Strong"):
        print(f"Password strength: {strength}")
    else:
        print("Enter strong password please \n")
        main()

#Ensures that the main() function is executed only when the script is run directly not imported as a module. 
if __name__ == "__main__":
    main()
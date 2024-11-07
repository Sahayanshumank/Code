number = int(input("Enter a Number: "))
org_var = number  # Stores the original number
rev = ""

while number != 0:
    rev += str(number % 10)  # Get the last digit and append it to `rev`
    number //= 10  # Remove the last digit from `number`

print("\nReversed:", rev)

# Check for Palindrome
if org_var == int(rev):  # Convert rev to int for proper comparison
    print(f"Given number ({org_var}) is a palindrome")
else:
    print(f"Given number ({org_var}) is not a palindrome")

    
    
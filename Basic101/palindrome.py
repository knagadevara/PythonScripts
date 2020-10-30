c12 = input("What is the string? ")

## not so conventional
lst12 = "".join(reversed(c12))
if c12 == lst12:
    print("Palindrome!")
else:
    print("Not a Palindrome!")

## conventional
if(c12==c12[::-1]):
    print("Palindrome!")
else:
    print("Not a Palindrome!")
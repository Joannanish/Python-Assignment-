def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

user_input = input("Enter a string: ")
print(is_palindrome(user_input))

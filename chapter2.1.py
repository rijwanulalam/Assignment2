inp_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'

# Extract numbers and letters from the input string
numbers = ''.join([char for char in inp_string if char.isdigit()])
letters = ''.join([char for char in inp_string if char.isalpha()])

# Extract even numbers from the string
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]

# Print all even numbers
print(', '.join(map(str, even_numbers)), "(even numbers)")

# Print all ASCII codes of the even numbers
print(', '.join([str(ord(str(number))) for number in even_numbers]), "(ASCII codes)")

print()

# Extract the uppercase letters from the string
uppercase_letters = [char for char in letters if char.isupper()]

# Print the uppercase letters
print(', '.join(uppercase_letters), "(uppercase_letters)")

# Print the ASCII codes of the uppercase letters with "(ASCII codes)" suffix
print(', '.join([str(ord(letter)) for letter in uppercase_letters]), "(ASCII codes)")

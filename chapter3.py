# 1. Fix the code
def decrypt(text, key):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):  # Wrap around for lowercase letters
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):  # Wrap around for uppercase letters
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabetic characters remain the same

    return decrypted_text

# 2. Encrypted code
encrypted_code = """
tybony_inenvoyr = 100
zl_vpqr = ['znl1', 'znl2', 'znl3', 'znl4', 'znl5']
qbfrf_ahoref(alnoref):
    tybony_inevnoyr = 5
    alnoref = [1, 2, 3, 4, 5]
    juvyr qbfrf_inenvoyr > 0:
        tybony_inenvoyr -= 1
        abenqf.erfhz(tybony_inenvoyr)
        tybony_inenvoyr -= 1
erghea ahzoref
zl_frq = [1, 2, 3, 4, 5, 4, 3, 2, 1]
enfrev = cebprff(alnoref(zl_frq))
qrs zbqvyl_svefg():
    tybony_inenvoyr = 10
    zl_vpqr['znl4'] = tybony_inenvoyr
zbxvsl_svefg(5)
qrs hqqre_tybony():
    tybony_tybony_inenvoyr
    tybony_inenvoyr += 10
    sve_va_enzrf():
        cneevat()
        v = 1
vs zl_frq vf abg abear naq zl_vpqr['znl4'] == 10:
    cnefr('Pbagnvab Zngn')
vs 5 abg va zl_pnge:
    cnefr('S s fubhyq abg gur qvpvqranel')
"""

# Use the decryption function with the correct key from question 2
key = 13
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

'''
# error code
global_varaible = 100  # should this be 'global_variable'

my_icde = ['may1', 'may2', 'may3', 'may4', 'may5']

# Function definition missing 'def' keyword
doses_nubers(nyabers):  # 'doses_nubers' should be 'doses_numbers'
    global_variable = 5  # Uses 'global_variable', but earlier 'global_varaible' was used
    nyabers = [1, 2, 3, 4, 5]

    while doses_varaible > 0:  # 'doses_varaible' should match 'global_variable'
        global_varaible -= 1  # Typo: 'global_varaible' should be 'global_variable'
        norads.resum(global_varaible)  # 'norads.resum()' is unclear, likely a placeholder for 'print' or other logic?
        global_varaible -= 1  # Typo: 'global_varaible' should be 'global_variable'

    return numbers  # 'numbers' is not defined anywhere within the function

my_sed = [1, 2, 3, 4, 5, 4, 3, 2, 1]

raseri = process(nyabers(my_sed))  # 'process' function is not defined, and function name 'nyabers' does not match earlier

def modily_first():
    global_varaible = 10  # Typo: 'global_varaible' should be 'global_variable'
    my_icde['may4'] = global_varaible  # Indexing error: 'my_icde' is a list, not a dictionary, should use integer index (3)

mokify_first(5)  # 'mokify_first' should be 'modify_first'

def udder_global():
    global_global_varaible  # 'global_global_varaible' likely should be 'global global_variable'
    global_varaible += 10  # 'global_varaible' should be 'global_variable'

'''
# 3. correct code with comments
global_variable = 100  # global_varaible -> global_variable

my_icde = ['may1', 'may2', 'may3', 'may4', 'may5']

# Added 'def' keyword to define the function and corrected the function name and variables
def doses_numbers(numbers):  # Fixed function name: doses_nubers -> doses_numbers
    global global_variable  # Use 'global' to modify the global variable
    global_variable = 5
    numbers = [1, 2, 3, 4, 5]

    # doses_varaible -> global_variable
    while global_variable > 0:
        global_variable -= 1
        print(global_variable)  # Replaced 'norads.resum' with print to display the value
        global_variable -= 1

    return numbers  # Now 'numbers' is defined correctly and returned

my_sed = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Corrected function call to match the defined function and arguments
result = doses_numbers(my_sed)  # Used 'doses_numbers' instead of 'nyabers' and passed 'my_sed'

# Corrected function name and logic
def modify_first():  # modily_first -> modify_first
    global global_variable  # Use 'global' to modify the global variable
    global_variable = 10
    my_icde[3] = global_variable  # Fixed indexing: lists use integer indices, so changed 'may4' to index 3

modify_first()  # mokify_first -> modify_first

# Corrected the function and variable names
def update_global():  # udder_global -> update_global
    global global_variable  # Use 'global' to modify the global variable
    global_variable += 10

    # Nested function definition for illustrative purposes
    def first_in_frames():
        print("Processing...")  # Replaced 'parring' with a valid print statement
        i = 1

# Corrected condition and indexing
if my_sed is not None and my_icde[3] == 10:  # norne -> None, and fixed list indexing for my_icde
    print('Containo Mata')  # Replaced 'parse' with 'print' for correct functionality

# Fixed condition and print statement
if 5 not in my_icde:  # Corrected 'my_catr' to 'my_icde' (list name)
    print('F f should not be in the dictionary')  # Replaced 'parse' with 'print'
 
# output
# 4
# 2
# 0
# Containo Mata
# F f should not be in the dictionary
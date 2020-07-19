import random

def check_valid_palindrome(w, x, y, z):
    """
    INPUT : This function will take user input w,x,y,z

    OUTPUT:
          this function would print
                if Valid :
                      "Valid palindrome" + stringPalindrome
                else:
                     "Input is not valid to create a Palindrome"
    """
    if x + y + z != w:
        print("Enter valid values of x y z whose sum is equal to w")
        return

    b_w = (w % 2 == 0)
    b_x = (x % 2 == 0)
    b_y = (y % 2 == 0)
    b_z = (z % 2 == 0)

    n_hx = x // 2
    n_hy = y // 2
    n_hz = z // 2

    rand_char = chr(random.randint(97, 122))
    rand_num = str(random.randint(0, 9))
    rand_spchar = chr(random.randint(33, 46))

    # For Even word length, only if all 3 types have even number
    if b_x and b_y and b_z:
        valid_palindrome = rand_char * n_hx + rand_num * n_hy + rand_spchar * z + rand_num * n_hy + rand_char * n_hx
        print("Valid Palindrome : " + valid_palindrome)
    # For Odd word length, only if one of the type has odd number and remaining two have even number
    elif (b_x and b_y and not b_z) or (b_x and not b_y and b_z) or (not b_x and b_y and b_z):
        if not b_x:
            valid_palindrome = rand_num * n_hy + rand_spchar * n_hz + rand_char * x + rand_spchar * n_hz + rand_num * n_hy
        elif not b_y:
            valid_palindrome = rand_char * n_hx + rand_spchar * n_hz + rand_num * y + rand_spchar * n_hz + rand_char * n_hx
        else:
            valid_palindrome = rand_char * n_hx + rand_num * n_hy + rand_spchar * z + rand_num * n_hy + rand_char * n_hx
        print("Valid Palindrome : " + valid_palindrome)
    else:
        print("Input is not valid to create a Palindrome")


if __name__ == '__main__':
    try:
        # Taking input from the user
        w = int(input('Enter word length w : '))
        x = int(input('     Enter number of alphabet x : '))
        y = int(input('     Enter number of numbers y : '))
        z = int(input('     Enter number of special characters z : '))
        # Calling the function and checking for a valid palindrome
        check_valid_palindrome(w, x, y, z)
    except ValueError as err:
        print("Enter a valid integer ", err)




'''Manual Test Scenarios for above logic'''

# Scenario 1 : w is Even -> all three x,y,z are even -> Valid Palindrome

# Scenario 2 : w is Even -> one of x,y,z is even and other two are odd -> Input is not valid to create a palindrome

# Scenario 3 : w is Odd -> all three x,y,z are odd -> Input is not valid to create a palindrome

# Scenario 4 : w is Odd -> one of x,y,z is odd and other two are even -> Valid Palindrome

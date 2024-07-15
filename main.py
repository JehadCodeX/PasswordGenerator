import random

letter = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = ["0","1","2","3","4","5","6","7","8","9"]
S_C = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "+", "=", "[", "]", "{", "}", ";", ":","'", "\"", ",", ".", "<", ">", "/", "?", "\\","|", "`", "~", " "]
Ln = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
Ls = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "+", "=", "[", "]", "{", "}", ";", ":","'", "\"", ",", ".", "<", ">", "/", "?", "\\","|", "`", "~", " "]
ns = ["0","1","2","3","4","5","6","7","8","9","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "+", "=", "[", "]", "{", "}", ";", ":","'", "\"", ",", ".", "<", ">", "/", "?", "\\","|", "`", "~", " "]
LnS = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","-", "_", "+", "=", "[", "]", "{", "}", ";", ":","'", "\"", ",", ".", "<", ">", "/", "?", "\\","|", "`", "~", " "]
letter_Q = input("do you want letters in your password y/n: ").lower()
nums_Q = input("do you want numbers in your password y/n: ").lower()
S_C_Q = input("do you want symbol in your password y/n: ").lower()

try:
    if letter_Q == "y" and nums_Q == "n" and S_C_Q == "n":
        letter_r = int(input("enter how many letter you want: "))

        for _ in range(letter_r):
            letter_G = random.choice(letter)
            print(letter_G, end="")
    elif nums_Q == "y" and letter_Q == "n" and S_C_Q == "n":
        nums_r = int(input("enter how many number you want: "))
        for _ in range(nums_r):
            nums_G = random.choice(nums)
            print(nums_G, end="")
    elif S_C_Q == "y" and letter_Q == "n" and nums_Q == "n":
        S_C_r = int(input("enter how many symbol you want: "))
        for _ in range(S_C_r):
            S_C_G = random.choice(S_C)
            print(S_C_G, end="")
    elif letter_Q == "y" and nums_Q == "y" and S_C_Q == "n":
        Ln_r = int(input("enter how many charter you want: "))
        for _ in range(Ln_r):
            Ln_G = random.choice(Ln)
            print(Ln_G, end="")
    elif letter_Q == "y" and nums_Q == "n" and S_C_Q == "y":
        Ls_r = int(input("enter how many charter you want: "))
        for _ in range(Ls_r):
            Ls_G = random.choice(Ls)
            print(Ls_G, end="")
    elif letter_Q == "n" and nums_Q == "y" and S_C_Q == "y":
        ns_r = int(input("enter how many charter you want: "))
        for _ in range(ns_r):
            ns_G = random.choice(ns)
            print(ns_G, end="")
    elif letter_Q == "y" and nums_Q == "y" and S_C_Q == "y":
        LnS_r = int(input("enter how many charter you want: "))
        for _ in range(LnS_r):
            LnS_G = random.choice(LnS)
            print(LnS_G, end="")
    else:
        print("you input something wrong Try to Rerun the app")
except Exception:
    print("there is an ERROR try to Rerun the app")

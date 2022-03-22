


#       // Sistema De Login  //                 



login = "ian"
password = "cacau"
Guess_login = ""
Guess_pasword = ""
error = 0
error_ps = 0
out_of_tries = 0
out_ps = 0



while Guess_login != login and out_of_tries < 3:
    if error == 0:
        error += 1
        Guess_login = input("Enter Login:")
        out_of_tries += 1
            
    else:
        print("wrong Login!")
        error += 1
        Guess_login = input("Enter Login:")
        if Guess_login == login:
            print()
        else:
            out_of_tries += 1
        
            
print()

while Guess_pasword != password and out_of_tries < 3 and out_ps < 3:
    out_of_tries = 1
    if Guess_pasword == password:
            out_of_tries = 4
    else:
        if error_ps == 0:
            Guess_pasword = input("Enter Password:")
            if Guess_pasword == password:
                out_of_tries = 4
            else:
                error_ps += 1
                out_ps += 1
            
        else:
            print("wrong password!")
            error_ps += 1
            Guess_pasword = input("Enter Password:")
            if Guess_pasword == password:
                out_of_tries = 4
            else:
                out_ps += 1


print()


if out_of_tries == 4 and out_ps < 3:
    print("Good job")

else:
    print("Out of tries")



#///////////////////////////////////////////////////////////////////////////////////////////

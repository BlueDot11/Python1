import random
n =9
to_be_guessed=int(n*random.random())+ 1
guess=9
while guess!=to_be_guessed:
    guess=int(input("New number:" ))
    if guess>0:
     if guess>to_be_guessed:
        print("Number too large")
     elif guess<to_be_guessed:
       print("Number too smalll")
    else:
        print("Sorry you are giving up!")
        break
else:
        print("Congraturation")

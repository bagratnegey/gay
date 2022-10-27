def hello_user():
    name = input("write your name")
    amount = input("choose amount of people on table")
    if amount == '4':
        print('hello',name,"your amount of people on table is",amount,"you can come to our restoraunt today in 6 pm")
    elif amount == "2":
        print('hello', name, "your amount of people on table is", amount,
              "you can come to our restoraunt today in 9 pm")
    else:
     print("sorry we dont have tables on",amount," people")
hello_user()
hello_user()





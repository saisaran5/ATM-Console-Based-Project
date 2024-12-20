#ATM [ Console Based ]
'''
1. withdraw
2. Deposit
3. Pin Generation
4. Mini statement
'''
Bank = {
    52896 : ["Saran","7860",10000,[15,6,2005]],
    46546 : ["Venky","5695",20000,[27,7,2002]] ,
    69656 : ["Sai",None,0,[30,11,1995]]
}
while True:
  print("Choose the required option: ")
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Pin Generation")
  print("4. Mini statement")
  print("5. Exit")
  n = int(input())
  if n == 1:
    print("")
    print("Withdraw")
    accno = int(input("Enter your account number: "))
    if accno not in Bank:
      print("Invalid Account number")
    else:
      print(f"Welcome {Bank[accno][0]}")
      pin = input("Enter your Pin: ")
      if pin != Bank[accno][1]:
        print("Invalid Pin")
      else:
        amt = int(input("Enter amount to withdraw: "))
        if amt > Bank[accno][2]:
          print("Insufficient Balance")
        else:
          Bank[accno][2] = Bank[accno][2] - amt
          print("Withdraw Successfull")
    print("")
  elif n == 2:
    print("")
    print("Deposit")
    accno = int(input("Enter your account number: "))
    if accno not in Bank:
      print("Invalid Account number")
    else:
      print(f"Welcome {Bank[accno][0]}")
      pin = input("Enter your Pin: ")
      if pin != Bank[accno][1]:
        print("Invalid Pin")
      else:
        amt = int(input("Enter amount to Deposit: "))
        Bank[accno][2] = Bank[accno][2] + amt
        print("Deposit Successfull")
    print("")
  elif n == 3:
    print("")
    print("Pin Generation")
    accno = int(input("Enter your account number: "))
    if accno not in Bank:
      print("Invalid Account number")
    else:
      print(f"Welcome {Bank[accno][0]}")
      if Bank[accno][1] != None:
        print("Pin already generated")
      else:
        print("Verify Date of Birth: ")
        date = int(input("Enter Birth Date: "))
        month = int(input("Enter Birth Month: "))
        year = int(input("Enter Birth Year: "))
        if date == Bank[accno][3][0] and month == Bank[accno][3][1] and year == Bank[accno][3][2]:
          pin = input("Enter your new Pin:")
          cpin = input("Confirm your Pin: ")
          if pin != cpin:
            print("Incorrect pin entered, try again")
          else:
            Bank[accno][1] = pin
            print("Pin Generated Sucessfully !")
        else:
          print("Incorrect Date of Birth Details")
          print("Try again !")
    print("")
  elif n == 4:
    print("")
    print("Mini statement")
    accno = int(input("Enter your account number: "))
    if accno not in Bank:
      print("Invalid Account number")
    else:
      print(f"Welcome {Bank[accno][0]}")
      pin = input("Enter Your Pin: ")
      if pin != Bank[accno][1]:
        print("Invalid Pin")
      else:
        print(f"Balance: {Bank[accno][2]}")
    print("")
  else:
    print("")
    print("Thank You")
    print("visit again")
    print("")
    break
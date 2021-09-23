print("Welcome to he Flarsheim Guesser!\n")

def getRemainder(num):
  while True:
    rem=int(input("What is the remainder when your number is devided by "+str(num)+" ?"))
    if rem<0:
      print("The value entered must be 0 or greater")
    elif rem>=num:
      print("The value entered must be less than",num)
    else:
      return rem

def getSecretNumber(rem3,rem5,rem7):
  for i in range(1,111):
    if i%3==rem3 and i%5==rem5 and i%7==rem7:
      return i

while True:
  print("Please think of a number between and including 100.\n")

  remainderOf3=getRemainder(3)
  print()
  remainderOf5=getRemainder(5)
  print()
  remainderOf7=getRemainder(7)

  secrectNum=getSecretNumber(remainderOf3,remainderOf5,remainderOf7)

  print("Your number was",secrectNum)
  print("How amazing is that?\n")

  while(True):
    again=input("Do you want to play again?Y to continue, N for quit==>")
    if(again=='y' or again=='Y' or again=='N' or again=='n'):
      break;
  if again=='n' or again=='N':
    break
  print()
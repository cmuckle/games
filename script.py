import random

money=100
#coin flip function
def coin_flip(bet,heads_tails):
  num = random.randint(1, 2)
  global money
  
  #determine win/loss
  if num==1:
    result="heads"
    money+=bet
  elif num==2:
    result="tails"
    money-=bet
  else: print("error")
  
  #return results
  if bet>money:
    return "You can't bet more than you have! You only have $"+str(money)
  if result=="heads" and heads_tails=="heads":
    return "You won $"+str(bet)+"! You now have $"+str(money)
  elif result=="tails" and heads_tails!="tails":
    return "You lost $"+str(bet)+"! You now have $"+str(money)
  else: return "Please enter 'heads' or 'tails'."

def cho_han(bet,odd_even):
  die1 = random.randint(1, 6)
  die2=random.randint(1, 6)
  global money
  
  #determine if roll is odd or even
  if (die1+die2)%2==0:
    roll="oven"
  else: roll="odd"
  
  #determine outcome  
  if bet>money:
    return "You can't bet more than you have! You only have $"+str(money)
  if roll==odd_even and (odd_even=="odd" or odd_even=="even"):
    money+=bet
    return "You won $"+str(bet)+"! You now have $"+str(money)  
  elif roll!=odd_even and (odd_even=="odd" or odd_even=="even"): 
    money-=bet
    return "You lost $"+str(bet)+"! You now have $"+str(money)
  else: return "Please enter 'odd' or 'even'."
 
#High Card, Low Card
def cards(bet):
  global money
  player_card = random.randint(1, 14)
  npc_card = random.randint(1, 14)
  if bet>money:
    return "You can't bet more than you have! You only have $"+str(money)
  if player_card>npc_card:
    money+=bet
    return "You won $"+str(bet)+"! You now have $"+str(money)
  elif player_card<npc_card:
    money-=bet
    return "You lost $"+str(bet)+"! You now have $"+str(money)
  else:
    return "It's a tie! Play again!"
#  
#Roulette
#
def roulette(bet,choice):
  result = random.randint(0, 36)
  global money
  if bet>money:
    return "You can't bet more than you have! You only have $"+str(money)
  if choice=="red" and result%2!=0:
    money+=bet
    return "You won $"+str(bet)+"! You now have $"+str(money)
  elif choice=="black" and result%2==0:
    money+=bet
    return "You won $"+str(bet)+"! You now have $"+str(money)
  elif choice==result or (choice=="green" and result==0): 
    money+=bet*35
    return "You won $"+str(bet*35)+"! You now have $"+str(money)
  else:
    money-=bet
    return "You lost $"+str(bet)+"! You now have $"+str(money)

    
    
  
#Calling game functions here
print(coin_flip(2,"heads"))
print(cho_han(10,"odd"))
print(cards(10))
try:
  print(roulette(10,"green"))
except NameError:
  print("wrong bet type")

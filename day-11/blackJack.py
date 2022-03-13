logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
import random

cards = [
  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
  "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

dealerCards = []
visibleDealerCards = []
playerCards = []

def dealCards(player):
  dealtCard = cards[random.randint(0, len(cards)-1)]
  if(player == "dealer" and len(dealerCards) == 0):
    dealerCards.append(dealtCard)
    visibleDealerCards.append(dealtCard)
  elif(player == "dealer"):
    dealerCards.append(dealtCard)
  else:
    playerCards.append(dealtCard)
  cards.remove(dealtCard)
  return player

def displayCards ():
  print("something")

def checkScore (cards):
  score = 0
  for card in cards:
    if(card == "Q" or card == "J" or card == "K" or card == "A"):
      score += 10
    elif(card == "A" and score <= 11):
      score += 10
    else:
      score += int(card)
  if("A" in cards and score > 21):
    score = score - 10 + 1
  return score

def initialDeal():
  dealCards("dealer")
  dealCards("dealer")
  dealCards("player")
  dealCards("player")


def gamePlay ():
  hitOrStand = "h"
  playerScore = checkScore(playerCards)
  dealerScore = checkScore(dealerCards)
  bust = False
  initialDeal()

  print(f"Dealer Cards: {visibleDealerCards}")
  print(f"Player Cards: {playerCards}")

  while hitOrStand == "h" and playerScore < 21:
    hitOrStand = input("Hit or Stand? ")
    hitOrStand = hitOrStand.lower()
    if hitOrStand == "hit" or hitOrStand == "h":
      dealCards("player")
      print(f"Player Cards: {playerCards} and Player Score: {checkScore(playerCards)}")
      playerScore = checkScore(playerCards)
    if(playerScore > 21):
      print("Player Busts")
      bust = True

  while (dealerScore) < checkScore(playerCards) and dealerScore < 22 and playerScore < 22 and bust != True:
    dealCards("dealer")
    dealerScore = checkScore(dealerCards)

  print(f"Player Cards: {playerCards} and Player Score: {checkScore(playerCards)}")
  print(f"Dealer Cards: {dealerCards} and Dealer Score: {checkScore(dealerCards)}")
  if(dealerScore > playerScore and dealerScore < 22 and playerScore < 22 or bust):
    print("Dealer Wins")
  else:
    print("Player Wins")

gamePlay()
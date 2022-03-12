logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}
isAuctionOver = False

print(logo)
print("Welcome to the section auction program!")
while isAuctionOver == False:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bids[name] = bid
  moreBids = input("Are there any other bidders? (Y or N) ")
  moreBids = moreBids.lower()
  if moreBids == "n":
    isAuctionOver = True

winner = max(bids, key=bids.get)
winningBid = bids.get(winner)
print(f"The winner is {winner} with a bid of {winningBid}")
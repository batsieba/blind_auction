from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

bid = True
bidders = []

while bid:
  player = {}
  name = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  player["name"] = name
  player["price"] = price
  bidders.append(player)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "no":
    bid = False
  else:
    bid = True
  clear()

max_bidder = bidders[0]["name"] 
max_bid = bidders[0]["price"]
for i in range(len(bidders)):
  if bidders[i]["price"] > max_bid:
    max_bidder = bidders[i]["name"]
    max_bid = bidders[i]["price"]


print(f"{max_bidder} has won the bid with {max_bid}")